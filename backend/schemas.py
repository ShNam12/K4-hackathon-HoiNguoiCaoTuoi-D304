"""Pydantic schemas for POST /api/analyze. Contract source: PLAN_10_GIO.md §3."""

from __future__ import annotations

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field

SCHEMA_VERSION = "1.0"


class Intent(str, Enum):
    clarify_concept = "clarify_concept"
    compare = "compare"
    need_example = "need_example"
    apply_practice = "apply_practice"
    logistics = "logistics"
    off_topic = "off_topic"
    unknown = "unknown"


class Confidence(str, Enum):
    high = "high"
    medium = "medium"
    low = "low"


class Status(str, Enum):
    auto_grouped = "auto_grouped"
    needs_review = "needs_review"
    unmatched = "unmatched"
    error = "error"


class QuestionIn(BaseModel):
    question_id: str
    student_id: str
    text: str
    created_at: datetime


class AnalyzeRequest(BaseModel):
    schema_version: str = SCHEMA_VERSION
    session_id: str
    questions: list[QuestionIn]


class EvidenceRef(BaseModel):
    file_id: str
    line: int


class Alternative(BaseModel):
    topic_id: str
    topic_title: str


class ClassificationResult(BaseModel):
    question_id: str
    topic_id: str | None
    topic_title: str | None
    intent: Intent
    confidence: Confidence
    status: Status
    matched_terms: list[str] = Field(default_factory=list)
    evidence_refs: list[EvidenceRef] = Field(default_factory=list)
    alternatives: list[Alternative] = Field(default_factory=list)
    rationale: str = ""


class GroupQuestion(BaseModel):
    question_id: str
    student_id: str
    text: str
    intent: Intent
    confidence: Confidence
    evidence_refs: list[EvidenceRef] = Field(default_factory=list)


class ConfidenceBreakdown(BaseModel):
    high: int = 0
    medium: int = 0
    low: int = 0


class QuestionGroup(BaseModel):
    topic_id: str
    topic_title: str
    question_count: int
    unique_student_count: int
    dominant_intent: Intent
    summary: str
    supported_question_ids: list[str]
    confidence_breakdown: ConfidenceBreakdown
    questions: list[GroupQuestion]


class ReviewItem(BaseModel):
    question_id: str
    student_id: str
    text: str
    status: Status
    confidence: Confidence
    alternatives: list[Alternative] = Field(default_factory=list)
    rationale: str = ""


class Trace(BaseModel):
    matcher_type: str
    matcher_prompt_version: str
    summary_prompt_version: str
    model: str


class AnalyzeResponse(BaseModel):
    schema_version: str = SCHEMA_VERSION
    analysis_id: str
    session_id: str
    generated_at: datetime
    groups: list[QuestionGroup] = Field(default_factory=list)
    review_queue: list[ReviewItem] = Field(default_factory=list)
    unmatched: list[ReviewItem] = Field(default_factory=list)
    trace: Trace
