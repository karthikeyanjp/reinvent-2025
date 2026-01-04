"""Search index for tags and keywords."""

import json
from pathlib import Path
from collections import defaultdict


class SearchIndex:
    """Inverted index for tags, keywords, and services."""

    def __init__(self, index_path: Path):
        self.index_path = index_path
        self.index = self._load_or_create()

    def _load_or_create(self) -> dict:
        if self.index_path.exists():
            data = json.loads(self.index_path.read_text())
            # Convert lists back to defaultdict
            data["tags"] = defaultdict(list, data.get("tags", {}))
            data["keywords"] = defaultdict(list, data.get("keywords", {}))
            data["services"] = defaultdict(list, data.get("services", {}))
            return data
        return {
            "videos": {},
            "tags": defaultdict(list),
            "keywords": defaultdict(list),
            "services": defaultdict(list),
        }

    def add_video(self, video_id: str, metadata: dict):
        """Add or update video in index."""
        self.index["videos"][video_id] = {
            "title": metadata.get("title", "Unknown"),
            "url": metadata.get("url", ""),
            "tags": metadata.get("tags", []),
            "keywords": metadata.get("keywords", []),
            "services": metadata.get("services_mentioned", []),
            "relevance": metadata.get("relevance_score", 5),
            "difficulty": metadata.get("difficulty", "intermediate"),
            "channel": metadata.get("channel", "Unknown"),
        }

        # Update inverted indices
        for tag in metadata.get("tags", []):
            tag_lower = tag.lower()
            if video_id not in self.index["tags"][tag_lower]:
                self.index["tags"][tag_lower].append(video_id)

        for kw in metadata.get("keywords", []):
            kw_lower = kw.lower()
            if video_id not in self.index["keywords"][kw_lower]:
                self.index["keywords"][kw_lower].append(video_id)

        for svc in metadata.get("services_mentioned", []):
            svc_lower = svc.lower()
            if video_id not in self.index["services"][svc_lower]:
                self.index["services"][svc_lower].append(video_id)

    def save(self):
        """Save index to disk."""
        # Convert defaultdicts to regular dicts for JSON serialization
        data = {
            "videos": self.index["videos"],
            "tags": dict(self.index["tags"]),
            "keywords": dict(self.index["keywords"]),
            "services": dict(self.index["services"]),
        }
        self.index_path.write_text(json.dumps(data, indent=2))

    def search(self, query: str) -> list[dict]:
        """Search across tags, keywords, services, and titles."""
        query_lower = query.lower()
        matching_ids = set()

        # Exact matches in tags/keywords/services
        matching_ids.update(self.index["tags"].get(query_lower, []))
        matching_ids.update(self.index["keywords"].get(query_lower, []))
        matching_ids.update(self.index["services"].get(query_lower, []))

        # Partial matches
        for tag, vids in self.index["tags"].items():
            if query_lower in tag:
                matching_ids.update(vids)

        for kw, vids in self.index["keywords"].items():
            if query_lower in kw:
                matching_ids.update(vids)

        for svc, vids in self.index["services"].items():
            if query_lower in svc:
                matching_ids.update(vids)

        # Title matches
        for vid, meta in self.index["videos"].items():
            if query_lower in meta["title"].lower():
                matching_ids.add(vid)

        return [
            {**self.index["videos"][vid], "video_id": vid}
            for vid in matching_ids
            if vid in self.index["videos"]
        ]

    def get_all_tags(self) -> list[str]:
        """Get all unique tags sorted by frequency."""
        return sorted(
            self.index["tags"].keys(), key=lambda t: len(self.index["tags"][t]), reverse=True
        )

    def get_all_videos(self) -> list[dict]:
        """Get all videos sorted by relevance."""
        videos = [
            {**meta, "video_id": vid}
            for vid, meta in self.index["videos"].items()
        ]
        return sorted(videos, key=lambda v: v.get("relevance", 0), reverse=True)
