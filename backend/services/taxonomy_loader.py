"""Load and filter the course taxonomy for a selected session."""

from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Any


DEFAULT_TAXONOMY_PATH = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "vlearn-pack"
    / "slides"
    / "knowledge-tree-day-chapter.json"
)


class TaxonomyError(ValueError):
    """Raised when taxonomy data cannot be loaded safely."""


def load_taxonomy(taxonomy_path: str | Path = DEFAULT_TAXONOMY_PATH) -> dict[str, Any]:
    """Read the full taxonomy JSON as UTF-8 without mutating it."""

    path = Path(taxonomy_path)
    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError as exc:
        raise TaxonomyError(f"Taxonomy file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise TaxonomyError(f"Taxonomy file is not valid JSON: {path}") from exc

    if not isinstance(data, dict) or not isinstance(data.get("days"), list):
        raise TaxonomyError("Taxonomy must contain a top-level 'days' list.")

    return data


def load_session_taxonomy(
    session_id: str,
    taxonomy_path: str | Path = DEFAULT_TAXONOMY_PATH,
) -> dict[str, Any]:
    """Return one session with only canonical chapters.

    The returned object is a deep copy so caller-side edits cannot change the
    loaded taxonomy for later requests.
    """

    full_taxonomy = load_taxonomy(taxonomy_path)
    day = _find_day(full_taxonomy, session_id)
    chapters = day.get("chapters")
    if not isinstance(chapters, list):
        raise TaxonomyError(f"Session {session_id!r} does not contain chapters.")

    _ensure_unique_chapter_ids(chapters, session_id)

    canonical_chapters = [
        copy.deepcopy(chapter)
        for chapter in chapters
        if chapter.get("is_canonical") is True
    ]

    session_taxonomy = {
        "schema_version": full_taxonomy.get("schema_version"),
        "normalization": copy.deepcopy(full_taxonomy.get("normalization", {})),
        "matching": copy.deepcopy(full_taxonomy.get("matching", {})),
        "sources": copy.deepcopy(full_taxonomy.get("sources", [])),
        "day_id": day.get("day_id"),
        "session_id": day.get("day_id"),
        "day_title": day.get("day_title"),
        "day_subtitle": day.get("day_subtitle"),
        "day_aliases": copy.deepcopy(day.get("day_aliases", [])),
        "day_keywords": copy.deepcopy(day.get("day_keywords", [])),
        "source_files": copy.deepcopy(day.get("source_files", [])),
        "chapters": canonical_chapters,
    }
    return session_taxonomy


def _find_day(taxonomy: dict[str, Any], session_id: str) -> dict[str, Any]:
    for day in taxonomy["days"]:
        if day.get("day_id") == session_id:
            return day
    raise TaxonomyError(f"Session not found in taxonomy: {session_id}")


def _ensure_unique_chapter_ids(chapters: list[dict[str, Any]], session_id: str) -> None:
    seen: set[str] = set()
    duplicates: set[str] = set()

    for chapter in chapters:
        chapter_id = chapter.get("chapter_id")
        if not chapter_id:
            raise TaxonomyError(f"Session {session_id!r} has a chapter without chapter_id.")
        if chapter_id in seen:
            duplicates.add(chapter_id)
        seen.add(chapter_id)

    if duplicates:
        duplicate_list = ", ".join(sorted(duplicates))
        raise TaxonomyError(
            f"Session {session_id!r} has duplicate chapter_id values: {duplicate_list}"
        )

