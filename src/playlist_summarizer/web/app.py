"""Flask web application."""

from pathlib import Path
from flask import Flask, render_template, jsonify, request
import markdown


def create_app(output_dir: Path):
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config["OUTPUT_DIR"] = Path(output_dir)

    from ..storage.index import SearchIndex

    index = SearchIndex(app.config["OUTPUT_DIR"] / "search_index.json")

    @app.route("/")
    def home():
        videos = index.get_all_videos()
        all_tags = index.get_all_tags()[:20]
        return render_template("index.html", videos=videos, tags=all_tags)

    @app.route("/api/search")
    def api_search():
        query = request.args.get("q", "").strip()
        if not query:
            return jsonify([])
        results = index.search(query)
        results = sorted(results, key=lambda x: x.get("relevance", 0), reverse=True)
        return jsonify(results[:20])

    @app.route("/api/tag/<tag>")
    def api_tag(tag: str):
        video_ids = index.index["tags"].get(tag.lower(), [])
        videos = [
            {**index.index["videos"][vid], "video_id": vid}
            for vid in video_ids
            if vid in index.index["videos"]
        ]
        videos = sorted(videos, key=lambda x: x.get("relevance", 0), reverse=True)
        return jsonify(videos)

    @app.route("/video/<video_id>")
    def video_detail(video_id: str):
        summaries_dir = app.config["OUTPUT_DIR"] / "summaries"
        md_files = list(summaries_dir.glob(f"{video_id}-*.md"))

        if not md_files:
            return "Video not found", 404

        content = md_files[0].read_text()
        html_content = markdown.markdown(content, extensions=["fenced_code", "tables"])
        video_meta = index.index["videos"].get(video_id, {})

        return render_template(
            "video.html",
            content=html_content,
            video_id=video_id,
            video=video_meta,
        )

    @app.route("/api/videos")
    def api_videos():
        videos = index.get_all_videos()
        return jsonify(videos)

    return app
