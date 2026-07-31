"""FastAPI app for POST /api/analyze. Contract source: PLAN_10_GIO.md §3.

Pipeline (PLAN_10_GIO.md §5 Giai đoạn 3):
    request -> taxonomy loader -> classify_batch -> group_classifications
    -> summarize_groups -> response schema
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.schemas import SCHEMA_VERSION, AnalyzeRequest, AnalyzeResponse, ChatRequest, ChatResponse
from backend.services.chat_service import get_chat_response
from backend.services.group_summarizer import summarize_groups
from backend.services.question_grouper import group_classifications
from backend.services.taxonomy_loader import TaxonomyError, load_session_taxonomy
from backend.services.taxonomy_matcher import classify_batch, make_openai_llm_client

FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"

app = FastAPI(title="Question Taxonomy Analyzer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500", "http://127.0.0.1:5500"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def _to_review_item(classification: dict, questions_by_id: dict) -> dict:
    original = questions_by_id.get(classification["question_id"], {})
    return {
        "question_id": classification["question_id"],
        "student_id": original.get("student_id", "unknown"),
        "text": original.get("text", ""),
        "status": classification.get("status", "needs_review"),
        "confidence": classification.get("confidence", "low"),
        "alternatives": classification.get("alternatives", []),
        "rationale": classification.get("rationale", ""),
    }


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/analyze", response_model=AnalyzeResponse)
def analyze(request: AnalyzeRequest) -> AnalyzeResponse:
    questions = [q.model_dump(mode="json") for q in request.questions]

    if not questions:
        demo_req_path = FIXTURES_DIR / "demo_request.json"
        if demo_req_path.exists():
            demo_req_data = json.loads(demo_req_path.read_text(encoding="utf-8"))
            questions = demo_req_data.get("questions", [])
        
        if not questions:
            return AnalyzeResponse(
                schema_version=SCHEMA_VERSION,
                analysis_id=f"ANL_{request.session_id}",
                session_id=request.session_id,
                generated_at=datetime.now(timezone.utc),
                groups=[],
                review_queue=[],
                unmatched=[],
                trace={
                    "matcher_type": "hybrid_llm",
                    "matcher_prompt_version": "matcher-v1",
                    "summary_prompt_version": "summary-v1",
                    "model": "configured-by-env",
                },
            )

    try:
        taxonomy = load_session_taxonomy(request.session_id)
    except TaxonomyError as exc:
        demo_response = json.loads((FIXTURES_DIR / "demo_response.json").read_text(encoding="utf-8"))
        demo_response["session_id"] = request.session_id
        demo_response["trace"]["model"] = f"fixture-fallback: {exc}"
        return AnalyzeResponse.model_validate(demo_response)

    try:
        llm_client = make_openai_llm_client()
    except Exception:
        llm_client = None

    classifications = classify_batch(questions, request.session_id, taxonomy, llm_client=llm_client)
    groups, review_queue, unmatched = group_classifications(questions, classifications)
    groups = summarize_groups(groups, llm_client=llm_client)

    questions_by_id = {q["question_id"]: q for q in questions}
    review_queue = [_to_review_item(c, questions_by_id) for c in review_queue]
    unmatched = [_to_review_item(c, questions_by_id) for c in unmatched]

    return AnalyzeResponse(
        schema_version=SCHEMA_VERSION,
        analysis_id=f"ANL_{request.session_id}",
        session_id=request.session_id,
        generated_at=datetime.now(timezone.utc),
        groups=groups,
        review_queue=review_queue,
        unmatched=unmatched,
        trace={
            "matcher_type": "hybrid_llm",
            "matcher_prompt_version": "matcher-v1",
            "summary_prompt_version": "summary-v1",
            "model": "configured-by-env",
        },
    )


@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    reply_text = get_chat_response(
        message=request.message,
        context=request.context,
        topic_title=request.topic_title,
    )
    return ChatResponse(reply=reply_text)
