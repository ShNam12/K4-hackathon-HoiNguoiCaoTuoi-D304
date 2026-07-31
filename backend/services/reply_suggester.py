"""Generate a suggested teacher reply to a topic's student questions."""

from __future__ import annotations

from pathlib import Path

from backend.services.llm_client import LLMError, get_llm_client

PROMPT_PATH = Path(__file__).resolve().parent.parent / "prompts" / "reply_suggestion.md"


def suggest_reply(
    topic_title: str,
    questions: list[dict],
    *,
    llm_client: callable | None = None,
) -> str:
    if llm_client is None:
        try:
            llm_client = get_llm_client()
        except LLMError:
            return _fallback_reply(topic_title)
        if llm_client is None:
            return _fallback_reply(topic_title)

    system_prompt = PROMPT_PATH.read_text(encoding="utf-8")
    question_lines = "\n".join(f"- {q['text']}" for q in questions) or "(không có câu hỏi cụ thể)"
    user_prompt = f"Chủ đề: {topic_title}\nCâu hỏi của sinh viên:\n{question_lines}"

    try:
        result = llm_client(system_prompt, user_prompt)
    except LLMError:
        return _fallback_reply(topic_title)

    reply = (result.get("reply") or "").strip()
    return reply or _fallback_reply(topic_title)


def _fallback_reply(topic_title: str) -> str:
    return (
        f"Chào các em, Thầy/Cô đã ghi nhận các câu hỏi về \"{topic_title}\" "
        "và sẽ phản hồi chi tiết trong buổi học tới."
    )
