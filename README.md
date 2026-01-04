# Playlist Summarizer

YouTube playlist summarizer using Claude AI. Designed for AWS re:Invent content with platform engineering focus.

## Features

- Extract videos from YouTube playlists via yt-dlp
- Fetch transcripts (JSON3/VTT formats)
- Summarize with Claude Sonnet 4
- Generate searchable markdown docs
- Flask web UI for browsing/search
- SQLite caching to avoid reprocessing

## Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              CLI (Typer)                                    │
│   process | search | tags | serve | rebuild_index                          │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                           Core Pipeline                                     │
│                          (main.py)                                          │
└─────────────────────────────────────────────────────────────────────────────┘
          │                         │                         │
          ▼                         ▼                         ▼
┌──────────────────┐    ┌──────────────────┐    ┌──────────────────────────┐
│    Extractors    │    │   Summarizers    │    │        Storage           │
│                  │    │                  │    │                          │
│  ┌────────────┐  │    │  ┌────────────┐  │    │  ┌────────────────────┐  │
│  │  playlist  │  │    │  │   claude   │  │    │  │    cache.py        │  │
│  │  (yt-dlp)  │  │    │  │ (Anthropic)│  │    │  │    (SQLite)        │  │
│  └────────────┘  │    │  └────────────┘  │    │  └────────────────────┘  │
│  ┌────────────┐  │    │  ┌────────────┐  │    │  ┌────────────────────┐  │
│  │ transcript │  │    │  │  prompts   │  │    │  │    index.py        │  │
│  │  (yt-dlp)  │  │    │  │            │  │    │  │  (search index)    │  │
│  └────────────┘  │    │  └────────────┘  │    │  └────────────────────┘  │
└──────────────────┘    └──────────────────┘    │  ┌────────────────────┐  │
                                                │  │   markdown.py      │  │
                                                │  │   (md generator)   │  │
                                                │  └────────────────────┘  │
                                                └──────────────────────────┘
                                                            │
                                                            ▼
                                                ┌──────────────────────────┐
                                                │        Web (Flask)       │
                                                │                          │
                                                │  Routes:                 │
                                                │  /           - home      │
                                                │  /api/search - search    │
                                                │  /api/tag    - by tag    │
                                                │  /video/:id  - detail    │
                                                └──────────────────────────┘
```

## Data Flow

```
YouTube Playlist URL
        │
        ▼
   ┌─────────┐
   │ yt-dlp  │──────► VideoInfo (id, title, url, duration, channel)
   └─────────┘
        │
        ▼
   ┌─────────┐
   │  Cache  │──────► Skip if already processed
   └─────────┘
        │
        ▼
   ┌─────────┐
   │Transcript│─────► Raw text from captions
   └─────────┘
        │
        ▼
   ┌─────────┐
   │ Claude  │──────► JSON: insights, summary, tags, keywords,
   └─────────┘        difficulty, services, relevance_score
        │
        ▼
   ┌─────────────────────────────────────┐
   │              Output                  │
   │  • cache.db (SQLite)                │
   │  • summaries/*.md                   │
   │  • search_index.json                │
   └─────────────────────────────────────┘
```

## Components

| Component | File | Purpose |
|-----------|------|---------|
| CLI | `cli/commands.py` | Typer commands: process, search, tags, serve |
| Playlist Extractor | `extractors/playlist.py` | Extract video metadata via yt-dlp |
| Transcript Extractor | `extractors/transcript.py` | Fetch captions (JSON3/VTT fallback) |
| Claude Summarizer | `summarizers/claude.py` | API integration, retry logic |
| Prompts | `summarizers/prompts.py` | Platform eng focused prompts |
| Cache | `storage/cache.py` | SQLite for processed videos |
| Search Index | `storage/index.py` | Inverted indices (tags, keywords, services) |
| Markdown Generator | `storage/markdown.py` | Generate .md files from summaries |
| Web App | `web/app.py` | Flask UI for browsing/search |

## Project Structure

```
├── src/playlist_summarizer/
│   ├── config.py           # Settings (API key, model, paths)
│   ├── main.py             # Core pipeline
│   ├── cli/commands.py     # CLI commands
│   ├── extractors/
│   │   ├── playlist.py     # Video extraction
│   │   └── transcript.py   # Transcript fetching
│   ├── summarizers/
│   │   ├── claude.py       # Claude API
│   │   └── prompts.py      # System/user prompts
│   ├── storage/
│   │   ├── cache.py        # SQLite cache
│   │   ├── index.py        # Search index
│   │   └── markdown.py     # MD generation
│   └── web/
│       ├── app.py          # Flask app
│       ├── templates/      # Jinja2 templates
│       └── static/         # CSS/JS
├── output/
│   ├── cache.db            # Processed videos cache
│   ├── search_index.json   # Inverted search index
│   └── summaries/          # Generated markdown files
├── pyproject.toml
└── .env                    # ANTHROPIC_API_KEY
```

## Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.11+ |
| YouTube | yt-dlp, youtube-transcript-api |
| LLM | Claude Sonnet 4 (claude-sonnet-4-20250514) |
| CLI | Typer, Rich |
| Web | Flask, Jinja2 |
| Database | SQLite |
| Validation | Pydantic |
| Retry | Tenacity |
| Build | Hatchling |

## Installation

```bash
# Clone and install
pip install -e .

# Set API key
cp .env.example .env
# Edit .env with your ANTHROPIC_API_KEY
```

## Usage

```bash
# Process a playlist
playlist-summarizer process "https://youtube.com/playlist?list=..."

# Search summaries
playlist-summarizer search "kubernetes"

# List tags
playlist-summarizer tags

# Start web UI
playlist-summarizer serve

# Rebuild search index
playlist-summarizer rebuild_index
```

## Configuration

| Env Variable | Required | Default | Description |
|--------------|----------|---------|-------------|
| `ANTHROPIC_API_KEY` | Yes | - | Claude API key |
| `OUTPUT_DIR` | No | `./output` | Output directory |

## Output Format

Each summary includes:
- **Key Insights**: Bullet points of main takeaways
- **Summary**: Comprehensive overview
- **Tags**: Categorization labels
- **Keywords**: Searchable terms
- **Difficulty**: Beginner/Intermediate/Advanced
- **AWS Services**: Services mentioned
- **Relevance Score**: 1-10 platform eng relevance

## License

MIT
