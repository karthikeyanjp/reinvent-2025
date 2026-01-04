"""Cheatsheet generator - extracts memorable facts from summaries."""

import json
import re
from pathlib import Path
from anthropic import Anthropic, RateLimitError
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)
from .prompts import CHEATSHEET_SYSTEM_PROMPT, CHEATSHEET_USER_PROMPT


class CheatsheetGenerator:
    def __init__(self, api_key: str, model: str = "claude-sonnet-4-20250514"):
        self.client = Anthropic(api_key=api_key)
        self.model = model

    def load_summaries(self, summaries_dir: Path) -> str:
        """Load all markdown summaries into a single string."""
        summaries = []
        for md_file in sorted(summaries_dir.glob("*.md")):
            content = md_file.read_text()
            summaries.append(f"--- VIDEO: {md_file.stem} ---\n{content}\n")
        return "\n".join(summaries)

    @retry(
        retry=retry_if_exception_type(RateLimitError),
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=2, min=4, max=120),
    )
    def extract(self, summaries_text: str) -> dict:
        """Extract memorable facts from summaries."""
        response = self.client.messages.create(
            model=self.model,
            max_tokens=4000,
            system=CHEATSHEET_SYSTEM_PROMPT,
            messages=[
                {
                    "role": "user",
                    "content": CHEATSHEET_USER_PROMPT.format(summaries=summaries_text),
                }
            ],
        )
        return self._parse_response(response.content[0].text)

    def _parse_response(self, text: str) -> dict:
        """Parse JSON response from Claude."""
        text = text.strip()
        if text.startswith("```"):
            text = re.sub(r"^```(?:json)?\n?", "", text)
            text = re.sub(r"\n?```$", "", text)

        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            match = re.search(r"\{[\s\S]*\}", text)
            if match:
                data = json.loads(match.group())
            else:
                raise ValueError(f"Could not parse JSON: {text[:200]}")

        return data

    def render_markdown(self, data: dict) -> str:
        """Render cheatsheet as markdown."""
        lines = ["# AWS re:Invent 2025 Cheatsheet", ""]
        lines.append("> Bite-sized knowledge for everyday conversations")
        lines.append("")

        # Stats
        lines.append("## Stats That Impress")
        lines.append("")
        for item in data.get("stats_that_impress", []):
            lines.append(f"- **{item['stat']}**: {item['context']}")
            lines.append(f"  - *Use when: {item['when_to_mention']}*")
            lines.append("")

        # Concepts
        lines.append("## Concepts to Know")
        lines.append("")
        for item in data.get("concepts_to_know", []):
            lines.append(f"- **{item['term']}**: {item['explanation']}")
            lines.append(f"  - *Why it matters: {item['why_it_matters']}*")
            lines.append("")

        # Hot takes
        lines.append("## Hot Takes")
        lines.append("")
        for item in data.get("hot_takes", []):
            lines.append(f"- {item['statement']}")
            lines.append(f"  - *Evidence: {item['evidence']}*")
            lines.append("")

        # Products
        lines.append("## Products to Name-Drop")
        lines.append("")
        for item in data.get("products_to_name_drop", []):
            lines.append(f"- **{item['name']}**: {item['what_it_does']}")
            lines.append(f"  - *Notable: {item['why_notable']}*")
            lines.append("")

        # Surprising facts
        lines.append("## Surprising Facts")
        lines.append("")
        for item in data.get("surprising_facts", []):
            lines.append(f"- {item['fact']}")
            lines.append(f"  - *{item['context']}*")
            lines.append("")

        return "\n".join(lines)

    def generate(self, summaries_dir: Path, output_path: Path) -> Path:
        """Generate cheatsheet from all summaries."""
        summaries_text = self.load_summaries(summaries_dir)
        data = self.extract(summaries_text)
        markdown = self.render_markdown(data)
        output_path.write_text(markdown)
        return output_path
