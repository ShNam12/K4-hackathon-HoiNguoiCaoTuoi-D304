"""Shared OpenAI-compatible LLM client, configured from LLM_PROVIDER/LLM_MODEL/LLM_API_KEY."""

from __future__ import annotations

import json
import os
from typing import Any, Callable

PROVIDER_BASE_URLS = {
    "openai": None,
    "openrouter": "https://openrouter.ai/api/v1",
    "gemini": "https://generativelanguage.googleapis.com/v1beta/openai/",
}

DEFAULT_MODELS = {
    "openai": "gpt-4o-mini",
    "openrouter": "openai/gpt-4o-mini",
    "gemini": "gemini-flash-latest",
}


class LLMError(RuntimeError):
    pass


def get_llm_client() -> Callable[[str, str], dict[str, Any]] | None:
    """Build a `call_llm(system, user) -> dict` client from env vars, or None if unconfigured."""

    api_key = os.environ.get("LLM_API_KEY")
    if not api_key:
        return None

    provider = (os.environ.get("LLM_PROVIDER") or "openai").strip().lower()
    if provider not in PROVIDER_BASE_URLS:
        raise LLMError(f"Unknown LLM_PROVIDER: {provider!r}")

    model = (os.environ.get("LLM_MODEL") or "").strip() or DEFAULT_MODELS[provider]
    base_url = PROVIDER_BASE_URLS[provider]

    try:
        from openai import OpenAI
    except ImportError as exc:
        raise LLMError("Missing 'openai' package — run: pip install openai") from exc

    client = OpenAI(api_key=api_key, base_url=base_url) if base_url else OpenAI(api_key=api_key)

    def call_llm(system: str, user: str) -> dict[str, Any]:
        try:
            response = client.chat.completions.create(
                model=model,
                temperature=0.2,
                response_format={"type": "json_object"},
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
            )
        except Exception as exc:
            raise LLMError(f"LLM call failed: {exc}") from exc

        content = response.choices[0].message.content
        try:
            return json.loads(content)
        except (json.JSONDecodeError, TypeError) as exc:
            raise LLMError(f"LLM returned invalid JSON: {content!r:.300}") from exc

    return call_llm


def get_taxonomy_matcher_client() -> Callable[[dict], str] | None:
    """Adapter for taxonomy_matcher.LLMClient, which expects payload -> raw JSON string."""

    call_llm = get_llm_client()
    if call_llm is None:
        return None

    def client(payload: dict) -> str:
        system = payload["prompt"]
        user = json.dumps(payload, ensure_ascii=False)
        result = call_llm(system, user)
        return json.dumps(result, ensure_ascii=False)

    return client
