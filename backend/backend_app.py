import os
from fastapi import FastAPI, HTTPException, Path
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from typing import List
from .mongo_models import QuestionIn, ClusterSummaryIn
from pydantic import BaseModel


MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = os.getenv("MONGO_DB", "hackathon")


def get_db_client():
    return AsyncIOMotorClient(MONGO_URI)


app = FastAPI(title="Questions Clustering MVP")
client = get_db_client()
db = client[DB_NAME]

# Allow CORS for frontend during development. In production, restrict origins.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class IDResponse(BaseModel):
    id: str


@app.on_event("shutdown")
async def shutdown_db_client():
    client.close()


@app.post("/questions", response_model=IDResponse, status_code=201)
async def ingest_question(q: QuestionIn):
    # Minimal cleaning; real pipeline should do normalization/tokenization
    cleaned = q.raw_text.strip()
    doc = {
        "student_id": q.student_id,
        "raw_text": q.raw_text,
        "cleaned_text": cleaned,
        "subject": None,
        "intent": None,
        "priority": 0,
        "source_file": q.source_file,
        "source_line": q.source_line,
    }
    res = await db.questions.insert_one(doc)
    return {"id": str(res.inserted_id)}


@app.get("/clusters")
async def list_clusters(limit: int = 100):
    cursor = db.clusters.find().sort("created_at", -1).limit(limit)
    items = []
    async for c in cursor:
        c["id"] = str(c.pop("_id"))
        items.append(c)
    return items


@app.post("/clusters/{cluster_id}/summarize")
async def summarize_cluster(cluster_id: str = Path(...), payload: ClusterSummaryIn = None):
    # Load cluster and member questions
    try:
        oid = ObjectId(cluster_id)
    except Exception:
        raise HTTPException(status_code=400, detail="invalid cluster_id")

    cluster = await db.clusters.find_one({"_id": oid})
    if not cluster:
        raise HTTPException(status_code=404, detail="cluster not found")

    # fetch example questions
    q_cursor = db.cluster_examples.find({"cluster_id": oid}).sort("example_order", 1)
    q_ids = []
    async for ce in q_cursor:
        q_ids.append(ce.get("question_id"))

    questions = []
    for qid in q_ids:
        q = await db.questions.find_one({"_id": qid})
        if q:
            questions.append(q.get("cleaned_text") or q.get("raw_text"))

    # Placeholder summarization - replace with LLM call
    summary = "; ".join(questions[:5])[:800] if questions else "No examples"
    confidence = 0.7

    await db.clusters.update_one({"_id": oid}, {"$set": {"summary": summary, "confidence": confidence}})

    return {"summary": summary, "confidence": confidence}
