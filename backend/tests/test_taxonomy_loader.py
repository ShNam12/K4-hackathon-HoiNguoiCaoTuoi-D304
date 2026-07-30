import json

import pytest

from backend.services.taxonomy_loader import TaxonomyError, load_session_taxonomy


def test_load_day_01_successfully():
    taxonomy = load_session_taxonomy("DAY_01")

    assert taxonomy["day_id"] == "DAY_01"
    assert taxonomy["chapters"]


def test_loader_returns_only_canonical_chapters():
    taxonomy = load_session_taxonomy("DAY_01")

    assert all(chapter["is_canonical"] is True for chapter in taxonomy["chapters"])


def test_missing_session_returns_controlled_error():
    with pytest.raises(TaxonomyError, match="Session not found"):
        load_session_taxonomy("DAY_UNKNOWN")


def test_loader_detects_duplicate_chapter_id(tmp_path):
    taxonomy_path = tmp_path / "taxonomy.json"
    taxonomy_path.write_text(
        json.dumps(
            {
                "days": [
                    {
                        "day_id": "DAY_01",
                        "chapters": [
                            {"chapter_id": "DAY_01_CH_01", "is_canonical": True},
                            {"chapter_id": "DAY_01_CH_01", "is_canonical": True},
                        ],
                    }
                ]
            }
        ),
        encoding="utf-8",
    )

    with pytest.raises(TaxonomyError, match="duplicate chapter_id"):
        load_session_taxonomy("DAY_01", taxonomy_path)


def test_loader_return_does_not_mutate_source():
    first = load_session_taxonomy("DAY_01")
    original_title = first["chapters"][0]["chapter_title"]
    first["chapters"][0]["chapter_title"] = "changed by caller"

    second = load_session_taxonomy("DAY_01")

    assert second["chapters"][0]["chapter_title"] == original_title

