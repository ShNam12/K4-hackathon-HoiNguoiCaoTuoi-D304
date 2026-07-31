from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from .get_topic_digest.tool import get_topic_digest
from .get_topic_examples.tool import get_topic_examples
from .list_available_dates.tool import list_available_dates

from .compare_periods.tool import compare_periods
from .search_by_keyword.tool import search_by_keyword

# Đổi tên tool phải sync đồng bộ: artifacts/tools.yaml -> dict này -> thư mục tools/<tool_name>/.
TOOL_FUNCTIONS = {
    "get_topic_digest": get_topic_digest,
    "get_topic_examples": get_topic_examples,
    "list_available_dates": list_available_dates,
    "compare_periods": compare_periods,
    "search_by_keyword": search_by_keyword,
}


def load_tool_declarations(path: Path) -> list[dict[str, Any]]:
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))["tools"]


def to_openai_tools(declarations: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [{
        "type": "function",
        "function": {
            "name": item["name"],
            "description": item.get("description", ""),
            "parameters": item.get("parameters", {"type": "object", "properties": {}}),
        },
    } for item in declarations]
