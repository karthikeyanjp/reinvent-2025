"""CLI commands using Typer."""

from pathlib import Path
import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(help="YouTube Playlist Summarizer - Platform Engineering Focus")
console = Console()


@app.command()
def process(
    playlist_url: str = typer.Argument(..., help="YouTube playlist URL"),
    output_dir: Path = typer.Option(
        Path("./output"), "--output", "-o", help="Output directory"
    ),
    force: bool = typer.Option(
        False, "--force", "-f", help="Force reprocess all videos"
    ),
    limit: int = typer.Option(
        None, "--limit", "-l", help="Max videos to process"
    ),
):
    """Process a YouTube playlist and generate summaries."""
    from ..main import process_playlist

    console.print(f"[bold cyan]Processing playlist: {playlist_url}")
    console.print(f"[dim]Output: {output_dir.absolute()}")

    try:
        results = process_playlist(playlist_url, output_dir, force=force, limit=limit)

        console.print()
        console.print(f"[bold green]Processed: {results['processed']} videos")
        console.print(f"[yellow]Cached (skipped): {results['cached']}")
        console.print(f"[red]Failed (no transcript): {results['failed']}")

        if results["errors"]:
            console.print()
            console.print("[dim]Errors:")
            for err in results["errors"][:5]:
                console.print(f"  [dim red]{err[:80]}")

        console.print()
        console.print(f"[green]Summaries saved to: {output_dir / 'summaries'}")
        console.print(f"[green]Search index: {output_dir / 'search_index.json'}")

    except Exception as e:
        console.print(f"[bold red]Error: {e}")
        raise typer.Exit(1)


@app.command()
def search(
    query: str = typer.Argument(..., help="Search query (tag, keyword, or title)"),
    output_dir: Path = typer.Option(
        Path("./output"), "--output", "-o", help="Output directory"
    ),
    limit: int = typer.Option(10, "--limit", "-l", help="Max results"),
):
    """Search summaries by tag, keyword, or title."""
    from ..storage.index import SearchIndex

    index_path = output_dir / "search_index.json"
    if not index_path.exists():
        console.print("[red]No search index found. Run 'process' first.")
        raise typer.Exit(1)

    idx = SearchIndex(index_path)
    results = idx.search(query)

    if not results:
        console.print(f"[yellow]No results for: {query}")
        return

    # Sort by relevance
    results = sorted(results, key=lambda x: x.get("relevance", 0), reverse=True)[:limit]

    table = Table(title=f"Search: '{query}' ({len(results)} results)")
    table.add_column("Title", style="cyan", max_width=50)
    table.add_column("Tags", style="green", max_width=30)
    table.add_column("Rel", justify="center")
    table.add_column("URL", style="dim")

    for r in results:
        table.add_row(
            r["title"][:50],
            ", ".join(r.get("tags", [])[:4]),
            str(r.get("relevance", "?")),
            r.get("url", ""),
        )

    console.print(table)


@app.command()
def tags(
    output_dir: Path = typer.Option(
        Path("./output"), "--output", "-o", help="Output directory"
    ),
):
    """List all tags with video counts."""
    from ..storage.index import SearchIndex

    index_path = output_dir / "search_index.json"
    if not index_path.exists():
        console.print("[red]No search index found. Run 'process' first.")
        raise typer.Exit(1)

    idx = SearchIndex(index_path)

    table = Table(title="All Tags")
    table.add_column("Tag", style="cyan")
    table.add_column("Videos", justify="right")

    for tag in idx.get_all_tags()[:30]:
        count = len(idx.index["tags"][tag])
        table.add_row(tag, str(count))

    console.print(table)


@app.command()
def serve(
    port: int = typer.Option(5000, "--port", "-p", help="Port number"),
    output_dir: Path = typer.Option(
        Path("./output"), "--output", "-o", help="Output directory"
    ),
):
    """Start local web UI for browsing summaries."""
    from ..web.app import create_app

    if not (output_dir / "search_index.json").exists():
        console.print("[red]No search index found. Run 'process' first.")
        raise typer.Exit(1)

    console.print(f"[bold green]Starting web UI at http://localhost:{port}")
    console.print("[dim]Press Ctrl+C to stop")

    app = create_app(output_dir)
    app.run(host="127.0.0.1", port=port, debug=False)


@app.command()
def rebuild_index(
    output_dir: Path = typer.Option(
        Path("./output"), "--output", "-o", help="Output directory"
    ),
):
    """Rebuild search index from cache."""
    from ..main import rebuild_index as do_rebuild

    count = do_rebuild(output_dir)
    console.print(f"[green]Rebuilt index with {count} videos")


@app.command()
def cheatsheet(
    output_dir: Path = typer.Option(
        Path("./output"), "--output", "-o", help="Output directory"
    ),
):
    """Generate conversation cheatsheet from all summaries."""
    from ..config import Settings
    from ..summarizers.cheatsheet import CheatsheetGenerator

    summaries_dir = output_dir / "summaries"
    if not summaries_dir.exists() or not list(summaries_dir.glob("*.md")):
        console.print("[red]No summaries found. Run 'process' first.")
        raise typer.Exit(1)

    console.print("[bold cyan]Generating cheatsheet from summaries...")

    try:
        settings = Settings()
        generator = CheatsheetGenerator(settings.anthropic_api_key, settings.model)

        count = len(list(summaries_dir.glob("*.md")))
        console.print(f"[dim]Reading {count} summaries...")

        output_path = output_dir / "cheatsheet.md"
        generator.generate(summaries_dir, output_path)

        console.print(f"[bold green]Cheatsheet saved to: {output_path}")

    except Exception as e:
        console.print(f"[bold red]Error: {e}")
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
