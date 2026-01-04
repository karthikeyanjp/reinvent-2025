"""Fetch transcripts from YouTube videos using yt-dlp."""

import subprocess
import json
import tempfile
import os
from pathlib import Path


class TranscriptError(Exception):
    """Video transcript unavailable."""
    pass


def fetch_transcript(video_id: str, languages: list[str] | None = None) -> str:
    """Fetch transcript using yt-dlp. Returns joined text."""
    url = f"https://www.youtube.com/watch?v={video_id}"

    with tempfile.TemporaryDirectory() as tmpdir:
        output_path = Path(tmpdir) / "subtitle"

        # yt-dlp command to extract subtitles only
        cmd = [
            "yt-dlp",
            "--skip-download",
            "--write-auto-sub",
            "--write-sub",
            "--sub-lang", "en",
            "--sub-format", "json3",
            "--cookies-from-browser", "chrome",
            "--output", str(output_path),
            url,
        ]

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=60,
            )
        except subprocess.TimeoutExpired:
            raise TranscriptError(f"Timeout fetching transcript: {video_id}")
        except Exception as e:
            raise TranscriptError(f"Error running yt-dlp: {e}")

        # Look for the subtitle file
        sub_files = list(Path(tmpdir).glob("*.json3"))

        if not sub_files:
            # Try vtt format as fallback
            cmd[7] = "vtt"  # change --sub-format
            try:
                subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            except:
                pass

            vtt_files = list(Path(tmpdir).glob("*.vtt"))
            if vtt_files:
                return _parse_vtt(vtt_files[0])

            raise TranscriptError(f"No subtitles found for: {video_id}")

        return _parse_json3(sub_files[0])


def _parse_json3(filepath: Path) -> str:
    """Parse json3 subtitle format."""
    try:
        data = json.loads(filepath.read_text())
        events = data.get("events", [])

        texts = []
        for event in events:
            segs = event.get("segs", [])
            for seg in segs:
                text = seg.get("utf8", "").strip()
                if text and text != "\n":
                    texts.append(text)

        return " ".join(texts)
    except Exception as e:
        raise TranscriptError(f"Error parsing subtitle: {e}")


def _parse_vtt(filepath: Path) -> str:
    """Parse VTT subtitle format."""
    try:
        content = filepath.read_text()
        lines = content.split("\n")

        texts = []
        for line in lines:
            line = line.strip()
            # Skip timing lines, headers, empty lines
            if not line or line.startswith("WEBVTT") or "-->" in line:
                continue
            if line.isdigit():
                continue
            # Remove HTML-like tags
            import re
            clean = re.sub(r"<[^>]+>", "", line)
            if clean:
                texts.append(clean)

        return " ".join(texts)
    except Exception as e:
        raise TranscriptError(f"Error parsing VTT: {e}")
