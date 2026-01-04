"""Extract video metadata from YouTube playlists."""

from dataclasses import dataclass
from typing import Iterator
import yt_dlp


@dataclass
class VideoInfo:
    video_id: str
    title: str
    url: str
    duration: int
    channel: str


def extract_playlist_videos(playlist_url: str) -> Iterator[VideoInfo]:
    """Extract video metadata from playlist using yt-dlp."""
    ydl_opts = {
        "quiet": True,
        "extract_flat": True,
        "force_generic_extractor": False,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        playlist_info = ydl.extract_info(playlist_url, download=False)

        for entry in playlist_info.get("entries", []):
            if entry is None:
                continue
            yield VideoInfo(
                video_id=entry["id"],
                title=entry.get("title", "Unknown"),
                url=f"https://www.youtube.com/watch?v={entry['id']}",
                duration=entry.get("duration", 0) or 0,
                channel=entry.get("channel", "Unknown") or "Unknown",
            )
