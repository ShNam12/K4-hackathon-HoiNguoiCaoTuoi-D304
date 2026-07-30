"""
Vòng lặp agent: giảng viên hỏi tự do bằng tiếng Việt → model tự chọn tool (get_topic_digest /
get_topic_examples / list_available_dates) → tool chạy trên turns_topics.jsonl thật → model
viết câu trả lời cuối dựa THUẦN TUÝ trên kết quả tool. Mirror `run_model_tool_loop` của dự án
tham khảo K4-Day04-D304-B3 (chat.py), thu gọn cho một provider (OpenRouter).

Dùng trực tiếp: `python agent.py "5 chủ đề sinh viên hôm nay chưa hiểu hết"`
Hoặc qua chat.py để hỏi nhiều lượt.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from llm_client import ChatResult, LLMError, ToolCall, complete_with_tools
from tools import TOOL_FUNCTIONS, load_tool_declarations, to_openai_tools

ARTIFACTS_DIR = Path(__file__).resolve().parent / "artifacts"
DEFAULT_SYSTEM_PROMPT_PATH = ARTIFACTS_DIR / "system_prompt.md"
DEFAULT_TOOLS_PATH = ARTIFACTS_DIR / "tools.yaml"


def execute_tool_call(call: ToolCall) -> dict[str, Any]:
    func = TOOL_FUNCTIONS.get(call.name)
    if not func:
        return {"tool": call.name, "args": call.args, "result": {"error": "unknown_tool", "message": f"Không có implementation cho '{call.name}'"}}
    try:
        result = func(**call.args)
    except Exception as exc:  # tool lỗi là dữ liệu, không được làm sập vòng lặp
        result = {"error": type(exc).__name__, "message": str(exc)}
    return {"tool": call.name, "args": call.args, "result": result}


def _tool_results_message(events: list[dict[str, Any]]) -> dict[str, str]:
    return {
        "role": "user",
        "content": (
            "TOOL_RESULTS_JSON:\n"
            f"{json.dumps(events, ensure_ascii=False, indent=2, default=str)}\n\n"
            "Chỉ dùng đúng những số liệu trong JSON trên để trả lời giảng viên. Không tự thêm số liệu khác."
        ),
    }


def _assistant_tool_message(text: str | None, calls: list[ToolCall]) -> dict[str, str]:
    summary = [{"name": c.name, "args": c.args} for c in calls]
    content = text or "Đang gọi tool để lấy số liệu."
    return {"role": "assistant", "content": f"{content}\n\nTOOL_CALLS_JSON:\n{json.dumps(summary, ensure_ascii=False)}"}


def run_agent_turn(
    messages: list[dict[str, str]],
    *,
    tools: list[dict[str, Any]],
    model: str | None = None,
    max_tool_rounds: int = 4,
) -> dict[str, Any]:
    """Chạy tối đa `max_tool_rounds` vòng gọi model/tool cho một lượt hỏi, trả về câu trả lời cuối + trace."""
    working_messages = list(messages)
    rounds: list[dict[str, Any]] = []
    all_tool_events: list[dict[str, Any]] = []

    for round_index in range(1, max_tool_rounds + 1):
        try:
            response: ChatResult = complete_with_tools(working_messages, tools, model=model, temperature=0.0)
        except LLMError as exc:
            rounds.append({"round": round_index, "error": str(exc)})
            return {"status": "llm_error", "assistant_text": f"Không gọi được model: {exc}", "rounds": rounds, "tool_events": all_tool_events}

        calls = response.tool_calls
        round_record: dict[str, Any] = {
            "round": round_index,
            "assistant_text": response.text,
            "tool_calls": [{"name": c.name, "args": c.args} for c in calls],
            "tool_results": [],
        }

        if not calls:
            rounds.append(round_record)
            return {"status": "answered", "assistant_text": response.text or "", "rounds": rounds, "tool_events": all_tool_events}

        working_messages.append(_assistant_tool_message(response.text, calls))
        for call in calls:
            event = execute_tool_call(call)
            round_record["tool_results"].append(event)
            all_tool_events.append(event)

        rounds.append(round_record)
        working_messages.append(_tool_results_message(round_record["tool_results"]))

    return {
        "status": "max_tool_rounds",
        "assistant_text": f"Dừng sau {max_tool_rounds} vòng gọi tool — xem trace để biết chi tiết.",
        "rounds": rounds,
        "tool_events": all_tool_events,
    }


def ask(
    user_text: str,
    *,
    history: list[dict[str, str]] | None = None,
    system_prompt_path: Path = DEFAULT_SYSTEM_PROMPT_PATH,
    tools_path: Path = DEFAULT_TOOLS_PATH,
    model: str | None = None,
) -> dict[str, Any]:
    """Tiện ích 1 lượt hỏi — nạp system prompt + tools.yaml, chạy run_agent_turn."""
    system_prompt = system_prompt_path.read_text(encoding="utf-8")
    tool_declarations = load_tool_declarations(tools_path)
    openai_tools = to_openai_tools(tool_declarations)

    messages = [{"role": "system", "content": system_prompt}, *(history or []), {"role": "user", "content": user_text}]
    return run_agent_turn(messages, tools=openai_tools, model=model)


if __name__ == "__main__":
    import sys

    question = " ".join(sys.argv[1:]) or "5 chủ đề sinh viên hôm nay chưa hiểu hết"
    result = ask(question)
    print(f"Giảng viên> {question}")
    print(f"\nAgent> {result['assistant_text']}")
    if result["tool_events"]:
        print("\n--- Tool trace ---")
        print(json.dumps(result["tool_events"], ensure_ascii=False, indent=2, default=str))
