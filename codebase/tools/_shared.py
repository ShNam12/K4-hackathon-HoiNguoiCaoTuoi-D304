from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]  # codebase/
DEFAULT_TOPICS_PATH = ROOT / "out" / "turns_topics.jsonl"


def err(tool: str, exc: Exception) -> dict[str, Any]:
    return {"tool": tool, "error": type(exc).__name__, "message": str(exc)}


def topics_path() -> Path:
    return Path(os.environ.get("TURNS_TOPICS_PATH", DEFAULT_TOPICS_PATH))


def load_topics_records() -> list[dict[str, Any]]:
    path = topics_path()
    if not path.exists():
        raise FileNotFoundError(f"Chưa có {path} — chạy classify_turns.py trước (xem README.md).")
    with path.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]
