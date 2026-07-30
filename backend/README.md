Backend — Question Taxonomy Analyzer
=====================================

FastAPI service implementing `POST /api/analyze` per the contract in
`PLAN_10_GIO.md` §3. No MongoDB/vector DB dependency — taxonomy is loaded
from `data/vlearn-pack/slides/knowledge-tree-day-chapter.json`.

Files
- `backend_app.py`: FastAPI app — `GET /health`, `POST /api/analyze`.
- `schemas.py`: Pydantic request/response models, schema version `1.0`.
- `fixtures/demo_request.json`, `fixtures/demo_response.json`: contract examples; frontend can develop against these without a running backend.
- `services/`: taxonomy loader/matcher (owned by P3), question grouper/summarizer (owned by P4).
- `tests/`: contract and health tests (owned by P5); service-level tests owned by P3/P4.

Quick start

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env
.\.venv\Scripts\python.exe -m uvicorn backend.backend_app:app --reload --port 8000
```

Example requests

```powershell
Invoke-RestMethod -Method Get -Uri "http://localhost:8000/health"

$body = Get-Content -Raw -Encoding utf8 "backend/fixtures/demo_request.json"
Invoke-RestMethod -Method Post -Uri "http://localhost:8000/api/analyze" -ContentType "application/json" -Body $body
```

Tests

```powershell
.\.venv\Scripts\python.exe -m pytest backend/tests -q
```

Notes
- Until P3/P4's pipeline is wired in (`PLAN_10_GIO.md` §5 Giai đoạn 3), `POST /api/analyze` returns the fixture response for any valid request.
- Keep API keys in `.env` only; never commit `.env`.
- Do not commit raw student data; follow the data rules in the root README.
