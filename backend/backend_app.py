"""FastAPI app for POST /api/analyze. Contract source: PLAN_10_GIO.md §3.

For the first hours this returns the fixture response so P2 can integrate
against a real HTTP endpoint before the taxonomy/grouping pipeline (P3/P4)
is wired in (see PLAN_10_GIO.md §5 Giai đoạn 3).
"""

from __future__ import annotations

import json
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.schemas import AnalyzeRequest, AnalyzeResponse

FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"

app = FastAPI(title="Question Taxonomy Analyzer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest) -> AnalyzeResponse:
    demo_response = json.loads((FIXTURES_DIR / "demo_response.json").read_text(encoding="utf-8"))
    demo_response["session_id"] = request.session_id
    return AnalyzeResponse.model_validate(demo_response)
