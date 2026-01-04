"""Main processing pipeline."""

import time
from pathlib import Path
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.console import Console

from .config import Settings
from .extractors.playlist import extract_playlist_videos
from .extractors.transcript import fetch_transcript, TranscriptError
from .summarizers.claude import ClaudeSummarizer
from .storage.cache import ProcessingCache
from .storage.markdown import generate_markdown
from .storage.index import SearchIndex

console = Console()


def process_playlist(
    playlist_url: str,
    output_dir: Path,
    force: bool = False,
    limit: int | None = None,
) -> dict:
    """Process YouTube playlist and generate summaries."""
    settings = Settings()
    output_dir = Path(output_dir)
    summaries_dir = output_dir / "summaries"
    summaries_dir.mkdir(parents=True, exist_ok=True)

    cache = ProcessingCache(output_dir / "cache.db")
    index = SearchIndex(output_dir / "search_index.json")
    summarizer = ClaudeSummarizer(settings.anthropic_api_key, settings.model)

    stats = {"processed": 0, "cached": 0, "failed": 0, "errors": []}

    # Extract playlist videos
    console.print("[cyan]Extracting playlist videos...")
    videos = list(extract_playlist_videos(playlist_url))
    console.print(f"[green]Found {len(videos)} videos")

    if limit:
        videos = videos[:limit]
        console.print(f"[yellow]Limiting to {limit} videos")

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("[cyan]Processing videos...", total=len(videos))

        for video in videos:
            progress.update(task, description=f"[cyan]{video.title[:40]}...")

            # Check cache (unless force reprocess)
            if not force and cache.is_processed(video.video_id):
                cached = cache.get_cached(video.video_id)
                if cached:
                    # Still add to index (in case index was deleted)
                    cached["url"] = video.url
                    cached["channel"] = video.channel
                    index.add_video(video.video_id, cached)
                    stats["cached"] += 1
                    progress.advance(task)
                    continue

            # Fetch transcript
            try:
                transcript = fetch_transcript(video.video_id)
            except TranscriptError as e:
                cache.save(video.video_id, video.title, None, False, str(e))
                stats["failed"] += 1
                stats["errors"].append(f"{video.title}: {e}")
                progress.advance(task)
                continue

            # Generate summary with Claude
            try:
                summary = summarizer.summarize(transcript, video.title)
                summary["title"] = video.title
                summary["url"] = video.url
                summary["video_id"] = video.video_id
                summary["channel"] = video.channel

                # Save to cache, markdown, and index
                cache.save(video.video_id, video.title, summary, True)
                generate_markdown(summary, summaries_dir)
                index.add_video(video.video_id, summary)

                stats["processed"] += 1

                # Rate limit
                time.sleep(settings.rate_limit_delay)

            except Exception as e:
                cache.save(video.video_id, video.title, None, True, str(e))
                stats["failed"] += 1
                stats["errors"].append(f"{video.title}: {e}")

            progress.advance(task)

    index.save()
    return stats


def rebuild_index(output_dir: Path) -> int:
    """Rebuild search index from cache."""
    cache = ProcessingCache(output_dir / "cache.db")
    index = SearchIndex(output_dir / "search_index.json")

    videos = cache.get_all_processed()
    for video in videos:
        index.add_video(video["video_id"], video)

    index.save()
    return len(videos)
