"""Claude API integration for video summarization."""

import json
import re
from anthropic import Anthropic, RateLimitError
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type,
)
from .prompts import PLATFORM_ENG_SYSTEM_PROMPT, SUMMARY_USER_PROMPT


class ClaudeSummarizer:
    def __init__(self, api_key: str, model: str = "claude-sonnet-4-20250514"):
        self.client = Anthropic(api_key=api_key)
        self.model = model

    @retry(
        retry=retry_if_exception_type(RateLimitError),
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=2, min=4, max=120),
    )
    def summarize(self, transcript: str, video_title: str) -> dict:
        """Generate summary with key insights and tags."""
        # Truncate transcript if too long (keep ~80k chars for safety)
        max_chars = 80000
        if len(transcript) > max_chars:
            transcript = transcript[:max_chars] + "... [truncated]"

        response = self.client.messages.create(
            model=self.model,
            max_tokens=2500,
            system=PLATFORM_ENG_SYSTEM_PROMPT,
            messages=[
                {
                    "role": "user",
                    "content": SUMMARY_USER_PROMPT.format(
                        title=video_title, transcript=transcript
                    ),
                }
            ],
        )

        return self._parse_response(response.content[0].text)

    def _parse_response(self, text: str) -> dict:
        """Parse JSON response from Claude."""
        # Try to extract JSON from response
        text = text.strip()

        # Remove markdown code blocks if present
        if text.startswith("```"):
            text = re.sub(r"^```(?:json)?\n?", "", text)
            text = re.sub(r"\n?```$", "", text)

        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            # Try to find JSON object in text
            match = re.search(r"\{[\s\S]*\}", text)
            if match:
                data = json.loads(match.group())
            else:
                raise ValueError(f"Could not parse JSON from response: {text[:200]}")

        # Validate required fields
        required = ["key_insights", "summary", "tags", "keywords"]
        for field in required:
            if field not in data:
                data[field] = [] if field != "summary" else "No summary generated."

        # Set defaults for optional fields
        data.setdefault("difficulty", "intermediate")
        data.setdefault("services_mentioned", [])
        data.setdefault("relevance_score", 5)

        return data
