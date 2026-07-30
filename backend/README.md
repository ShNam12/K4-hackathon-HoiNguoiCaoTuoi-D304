Backend integration and API notes
================================

This folder contains the MongoDB-backed FastAPI service for the Questions Clustering MVP.

Files
- `backend_app.py`: FastAPI endpoints for ingesting questions, listing clusters, and generating summaries.
- `mongo_models.py`: Pydantic request/response models.
- `openapi.yaml`: API contract for frontend/backend integration.

Quick start (local, minimal)

1. Create a virtual environment and install requirements:

```bash
python -m venv .venv
# Windows PowerShell
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
pip install -r requirements.txt
```

2. Start MongoDB and set environment variables:

```bash
# macOS / Linux
export MONGO_URI="mongodb://localhost:27017"
export MONGO_DB="hackathon"

# Windows PowerShell
set MONGO_URI="mongodb://localhost:27017"
set MONGO_DB="hackathon"
```

3. Run the FastAPI app:

```bash
cd backend
uvicorn backend_app:app --reload --port 8000
```

API endpoints
- `POST /questions`: ingest a new question.
- `GET /clusters`: list clusters.
- `POST /clusters/{cluster_id}/summarize`: generate or refresh a summary for one cluster.

Example requests

```bash
curl -X POST http://localhost:8000/questions \
  -H "Content-Type: application/json" \
  -d '{"student_id":"U123","raw_text":"Câu hỏi về phần 3","source_file":"transcript-02.md","source_line":120}'
```

```bash
curl http://localhost:8000/clusters
```

Notes
- This backend uses MongoDB via `motor` (async driver). The collections are `questions`, `clusters`, and `cluster_examples`.
- CORS is enabled for development so the browser-based frontend can call the API.
- The summarization endpoint is a placeholder and should be replaced with a controlled LLM call. Keep API keys in environment variables and never commit them.
- Do not commit raw data or personal student information; follow the hackathon data rules in the root README.
