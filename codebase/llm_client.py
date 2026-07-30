"""
Client gọi OpenRouter qua SDK `openai` (OpenRouter expose endpoint tương thích
OpenAI Chat Completions — cùng cách providers/openai_provider.py của dự án
tham khảo K4-Day04-D304-B3 dùng cho OpenRouterProvider).

Hai kiểu gọi:
  chat_json()          — ép trả JSON object, dùng cho classify_turns.py/daily_digest.py
                          (phân loại chủ đề, viết bản tin) — không cần tool-calling.
  complete_with_tools() — có khai báo tool (function calling), dùng cho agent.py khi
                          giảng viên hỏi tự do và agent cần tự chọn tool.

Đây là nơi phát ra lời gọi AI CHẠY THẬT bắt buộc theo luật hackathon (01-de-bai.md,
ràng buộc #1).
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

DEFAULT_MODEL = "openai/gpt-4o-mini"
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"


class LLMError(RuntimeError):
    """Lỗi gọi model — luôn bắt ở nơi gọi (pipeline/agent), không để crash."""


def _load_dotenv_once(env_path: Path | None = None) -> None:
    """Nạp .env thủ công (không thêm dependency python-dotenv). Không ghi đè biến đã set."""
    path = env_path or Path(__file__).resolve().parent / ".env"
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key, value = key.strip(), value.strip()
        if key and key not in os.environ:
            os.environ[key] = value


_load_dotenv_once()


def _client():
    try:
        from openai import OpenAI
    except ImportError as exc:
        raise LLMError("Chưa cài SDK 'openai' — chạy: pip install -r requirements.txt") from exc

    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise LLMError("Thiếu OPENROUTER_API_KEY — điền vào codebase/.env (xem .env.example).")
    return OpenAI(api_key=api_key, base_url=OPENROUTER_BASE_URL)


def _model_name(model: str | None) -> str:
    return model or os.environ.get("OPENROUTER_MODEL", DEFAULT_MODEL)


def chat_json(system: str, user: str, *, model: str | None = None, temperature: float = 0.0) -> dict:
    """Gọi model, ép trả JSON object, parse và trả về dict. Raise LLMError nếu lỗi ở bất kỳ bước nào."""
    client = _client()
    try:
        resp = client.chat.completions.create(
            model=_model_name(model),
            temperature=temperature,
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        )
    except Exception as exc:
        raise LLMError(f"Gọi OpenRouter thất bại: {exc}") from exc

    content = resp.choices[0].message.content
    try:
        return json.loads(content)
    except (json.JSONDecodeError, TypeError) as exc:
        raise LLMError(f"Model không trả JSON hợp lệ: {content!r:.300}") from exc


@dataclass
class ToolCall:
    name: str
    args: dict[str, Any]


@dataclass
class ChatResult:
    text: str | None = None
    tool_calls: list[ToolCall] = field(default_factory=list)


def complete_with_tools(
    messages: list[dict[str, str]],
    tools: list[dict[str, Any]] | None = None,
    *,
    model: str | None = None,
    temperature: float = 0.0,
) -> ChatResult:
    """Gọi model có khai báo tool (function calling), trả về text hoặc danh sách tool_calls đã chuẩn hoá."""
    client = _client()
    kwargs: dict[str, Any] = {
        "model": _model_name(model),
        "messages": messages,
        "temperature": temperature,
    }
    if tools:
        kwargs["tools"] = tools
    try:
        resp = client.chat.completions.create(**kwargs)
    except Exception as exc:
        raise LLMError(f"Gọi OpenRouter thất bại: {exc}") from exc

    msg = resp.choices[0].message
    calls: list[ToolCall] = []
    for call in msg.tool_calls or []:
        try:
            args = json.loads(call.function.arguments or "{}")
        except json.JSONDecodeError:
            args = {}
        calls.append(ToolCall(name=call.function.name, args=args))
    return ChatResult(text=msg.content, tool_calls=calls)
