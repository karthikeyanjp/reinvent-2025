"""SQLite cache to track processed videos."""

import sqlite3
import json
from pathlib import Path
from datetime import datetime


class ProcessingCache:
    """SQLite cache to avoid reprocessing videos."""

    def __init__(self, db_path: Path):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS processed_videos (
                    video_id TEXT PRIMARY KEY,
                    title TEXT,
                    processed_at TEXT,
                    summary_json TEXT,
                    has_transcript BOOLEAN,
                    error_message TEXT
                )
            """)

    def is_processed(self, video_id: str) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.execute(
                "SELECT 1 FROM processed_videos WHERE video_id = ?", (video_id,)
            )
            return cur.fetchone() is not None

    def get_cached(self, video_id: str) -> dict | None:
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.execute(
                "SELECT summary_json FROM processed_videos WHERE video_id = ? AND has_transcript = 1",
                (video_id,),
            )
            row = cur.fetchone()
            return json.loads(row[0]) if row and row[0] else None

    def save(
        self,
        video_id: str,
        title: str,
        summary: dict | None,
        has_transcript: bool,
        error: str | None = None,
    ):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                INSERT OR REPLACE INTO processed_videos
                (video_id, title, processed_at, summary_json, has_transcript, error_message)
                VALUES (?, ?, ?, ?, ?, ?)
            """,
                (
                    video_id,
                    title,
                    datetime.utcnow().isoformat(),
                    json.dumps(summary) if summary else None,
                    has_transcript,
                    error,
                ),
            )

    def get_all_processed(self) -> list[dict]:
        """Get all successfully processed videos."""
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.execute(
                "SELECT video_id, title, summary_json FROM processed_videos WHERE has_transcript = 1"
            )
            results = []
            for row in cur.fetchall():
                if row[2]:
                    summary = json.loads(row[2])
                    summary["video_id"] = row[0]
                    summary["title"] = row[1]
                    results.append(summary)
            return results
