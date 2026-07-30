"""
Chat nhiều lượt với agent (giảng viên hỏi tự do, model tự chọn tool). Ghi transcript
JSON mỗi lượt — bằng chứng cho R5/demo. Mirror chat.py của dự án tham khảo
K4-Day04-D304-B3, thu gọn cho một provider (OpenRouter) và 3 tool cố định.

Chạy: python chat.py
Gõ /exit để thoát.
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Any

from agent import DEFAULT_SYSTEM_PROMPT_PATH, DEFAULT_TOOLS_PATH, run_agent_turn
from tools import load_tool_declarations, to_openai_tools

ROOT = Path(__file__).resolve().parent


def now_iso() -> str:
    return datetime.now().isoformat(timespec="seconds")


def safe_slug(value: str) -> str:
    slug = re.sub(r"[^A-Za-z0-9_.-]+", "_", value.strip())
    return slug.strip("_") or "chat"


def trim_history(history: list[dict[str, str]], window: int) -> list[dict[str, str]]:
    if window <= 0:
        return []
    return history[-window * 2:]


def write_transcript(path: Path, transcript: dict[str, Any]) -> None:
    transcript["updated_at"] = now_iso()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(transcript, ensure_ascii=False, indent=2, default=str), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--model", default=None, help="Override model OpenRouter (mặc định OPENROUTER_MODEL trong .env)")
    parser.add_argument("--system-prompt", type=Path, default=DEFAULT_SYSTEM_PROMPT_PATH)
    parser.add_argument("--tools", type=Path, default=DEFAULT_TOOLS_PATH)
    parser.add_argument("--transcripts-dir", type=Path, default=ROOT / "transcripts")
    parser.add_argument("--history-window", type=int, default=5, help="Giữ N cặp user/assistant gần nhất trong context")
    parser.add_argument("--max-tool-rounds", type=int, default=4)
    args = parser.parse_args()

    system_prompt = args.system_prompt.read_text(encoding="utf-8")
    openai_tools = to_openai_tools(load_tool_declarations(args.tools))

    timestamp = datetime.now().strftime("%Y%m%dT%H%M%S%f")
    transcript_path = args.transcripts_dir / f"{safe_slug(args.model or 'openrouter')}_{timestamp}.transcript.json"
    transcript: dict[str, Any] = {
        "model": args.model,
        "system_prompt": str(args.system_prompt),
        "tools": str(args.tools),
        "created_at": now_iso(),
        "updated_at": now_iso(),
        "turns": [],
    }

    print("Agent thống kê chủ đề cho giảng viên. Gõ /exit để thoát.")

    history: list[dict[str, str]] = []
    turn_index = 0
    while True:
        try:
            user_text = input("\nGiảng viên> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not user_text:
            continue
        if user_text in {"/exit", "/quit"}:
            break

        turn_index += 1
        messages = [
            {"role": "system", "content": system_prompt},
            *trim_history(history, args.history_window),
            {"role": "user", "content": user_text},
        ]

        turn_record: dict[str, Any] = {"turn_index": turn_index, "started_at": now_iso(), "user": user_text}
        result = run_agent_turn(messages, tools=openai_tools, model=args.model, max_tool_rounds=args.max_tool_rounds)
        turn_record.update(result)
        turn_record["ended_at"] = now_iso()

        assistant_text = result["assistant_text"]
        print(f"\nAgent> {assistant_text}")
        history.append({"role": "user", "content": user_text})
        history.append({"role": "assistant", "content": assistant_text})

        transcript["turns"].append(turn_record)
        write_transcript(transcript_path, transcript)

    write_transcript(transcript_path, transcript)
    print(f"\nTranscript đã lưu: {transcript_path}")


if __name__ == "__main__":
    main()
