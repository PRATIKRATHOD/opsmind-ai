# OpsMind-AI

OpsMind-AI is an AI-powered incident investigation and Root Cause Analysis (RCA) platform built using FastAPI, LangGraph, Ollama, ChromaDB, and Retrieval-Augmented Generation (RAG).

The system simulates enterprise-grade operational incident workflows by combining:

* Monitoring analysis
* Log analysis
* Semantic runbook retrieval
* AI-generated RCA
* Retry and reliability handling
* AI safety guardrails
* Persistent incident memory

---

# Features

* Multi-agent AI orchestration using LangGraph
* Shared workflow state management
* Vector RAG using ChromaDB
* Semantic retrieval using SentenceTransformers
* Local LLM inference using Ollama + Mistral
* Incident memory persistence
* Retry/fault tolerance handling
* AI safety validation
* Realistic enterprise operational logs and runbooks

---

# Tech Stack

* Python
* FastAPI
* LangGraph
* ChromaDB
* SentenceTransformers
* Ollama
* Mistral
* Pydantic

---

# Project Structure

```text
opsmind-ai/
│
├── app/
├── knowledge_base/
├── logs/
├── chroma_db/
├── memory_store.json
├── README.md
├── ARCHITECTURE.md
├── SKILLS_LEARNED.md
└── requirements.txt
```

---

# Run Application

Activate virtual environment:

```powershell
venv\Scripts\activate
```

Run FastAPI server:

```powershell
uvicorn app.main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

# Example Incident Request

```json
{
  "ticket_id": "INC3001",
  "severity": "P2",
  "application": "api-gateway",
  "issue": "High API response latency during peak traffic"
}
```
# Screenshots

## Swagger UI

![Swagger UI](screenshots/Swagger%20UI.png)

## Successful RCA Response

![RCA Response](screenshots/successful%20RCA%20response.png)

## Workflow Execution Logs

![Workflow Logs](screenshots/terminal%20workflow%20logs.png)
