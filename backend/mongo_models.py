from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class QuestionIn(BaseModel):
    student_id: Optional[str]
    raw_text: str
    source_file: Optional[str]
    source_line: Optional[int]


class Question(BaseModel):
    id: Optional[str]
    student_id: Optional[str]
    raw_text: str
    cleaned_text: Optional[str]
    subject: Optional[str]
    intent: Optional[str]
    priority: Optional[int] = 0
    source_file: Optional[str]
    source_line: Optional[int]
    created_at: Optional[datetime]


class ClusterSummaryIn(BaseModel):
    prompt_context: Optional[str]


class Cluster(BaseModel):
    id: Optional[str]
    title: Optional[str]
    summary: Optional[str]
    confidence: Optional[float]
    topic: Optional[str]
    priority: Optional[int] = 0
    created_at: Optional[datetime]
