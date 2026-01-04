"""Configuration and settings."""

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


class Settings:
    def __init__(self):
        self.anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
        if not self.anthropic_api_key:
            raise ValueError("ANTHROPIC_API_KEY not set")

        self.model = "claude-sonnet-4-20250514"
        self.output_dir = Path(os.getenv("OUTPUT_DIR", "./output"))
        self.rate_limit_delay = 1.0  # seconds between API calls
