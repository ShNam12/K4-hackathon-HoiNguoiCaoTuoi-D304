import json
from pathlib import Path

from fastapi.testclient import TestClient

from backend.backend_app import app
from backend.schemas import SCHEMA_VERSION, AnalyzeResponse

client = TestClient(app)
FIXTURES_DIR = Path(__file__).resolve().parent.parent / "fixtures"


def load_fixture(name: str) -> dict:
    return json.loads((FIXTURES_DIR / name).read_text(encoding="utf-8"))


def test_demo_request_fixture_validates():
    from backend.schemas import AnalyzeRequest

    AnalyzeRequest.model_validate(load_fixture("demo_request.json"))


def test_demo_response_fixture_validates():
    AnalyzeResponse.model_validate(load_fixture("demo_response.json"))


def test_analyze_returns_schema_version():
    payload = load_fixture("demo_request.json")
    response = client.post("/api/analyze", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert body["schema_version"] == SCHEMA_VERSION
    assert body["session_id"] == payload["session_id"]


def test_analyze_missing_question_id_returns_422():
    payload = load_fixture("demo_request.json")
    del payload["questions"][0]["question_id"]
    response = client.post("/api/analyze", json=payload)
    assert response.status_code == 422


def test_analyze_empty_batch_does_not_crash():
    payload = {
        "schema_version": SCHEMA_VERSION,
        "session_id": "DAY_01",
        "questions": [],
    }
    response = client.post("/api/analyze", json=payload)
    assert response.status_code == 200
