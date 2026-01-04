"""Generate markdown files for video summaries."""

import re
from pathlib import Path
from datetime import datetime


def sanitize_filename(title: str) -> str:
    """Create safe filename from title."""
    safe = re.sub(r"[^\w\s-]", "", title)
    safe = re.sub(r"\s+", "-", safe)
    return safe[:50].strip("-")


def generate_markdown(video: dict, output_dir: Path) -> Path:
    """Generate markdown file for a video summary."""
    filename = f"{video['video_id']}-{sanitize_filename(video['title'])}.md"
    filepath = output_dir / filename

    tags_str = " ".join(f"`{tag}`" for tag in video.get("tags", []))
    insights_str = "\n".join(
        f"- {insight}" for insight in video.get("key_insights", [])
    )
    services_str = ", ".join(video.get("services_mentioned", [])) or "None mentioned"
    keywords_str = ", ".join(video.get("keywords", [])) or "None"

    content = f"""# {video['title']}

**URL**: [{video['url']}]({video['url']})
**Channel**: {video.get('channel', 'Unknown')}
**Difficulty**: {video.get('difficulty', 'intermediate')}
**Platform Eng Relevance**: {video.get('relevance_score', 5)}/10

## Tags
{tags_str}

## Key Insights

{insights_str}

## Summary

{video.get('summary', 'No summary available.')}

## AWS/Cloud Services Mentioned
{services_str}

## Keywords
{keywords_str}

---
*Generated on {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}*
"""

    filepath.write_text(content)
    return filepath
