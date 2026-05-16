# OpsMind-AI

OpsMind-AI is an AI-powered incident investigation and Root Cause Analysis (RCA) platform built using FastAPI, LangGraph, Ollama, ChromaDB, and Retrieval-Augmented Generation (RAG).

The system simulates enterprise-grade operational incident workflows by combining:

* Monitoring analysis
* Log analysis
* Metadata-aware semantic runbook retrieval
* AI-generated RCA
* Retry and reliability handling
* AI safety guardrails
* Persistent incident memory

---

# Features

* Multi-agent AI orchestration using LangGraph
* Shared workflow state management
* Vector RAG using ChromaDB
* Metadata-aware retrieval filtering
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
|-- app/
|-- docs/
|-- knowledge_base/
|-- logs/
|-- chroma_db/
|-- memory_store.json
|-- README.md
|-- ARCHITECTURE.md
|-- SKILLS_LEARNED.md
`-- requirements.txt
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

# Current v2.2 Workflow

```text
Planner Agent
-> Dynamic Tool Execution
-> Monitoring + Logs + Metadata-Aware RAG
-> Historical Incident Memory Search
-> LLM RCA Generation
-> Safety Validation
-> Persistent Incident Storage
```

# OpsMind-AI v2.2 - Metadata-Aware Retrieval Intelligence

OpsMind-AI v2.2 improves RAG retrieval accuracy by adding metadata-aware filtering to the vector retrieval path. Runbooks are categorized during vector store indexing, and incident queries are mapped to operational categories before ChromaDB search.

## Metadata-Aware Retrieval

The vector store now indexes runbooks with a `category` metadata field. During retrieval, the Vector Knowledge Agent detects the incident category and applies a ChromaDB metadata filter:

```python
where={"category": category}
```

This reduces semantic retrieval drift across unrelated operational domains and keeps database, security, streaming, infrastructure, and performance incidents focused on the right runbook set.

## Retrieval Simplification

The active RAG flow no longer depends on `retrieval_query_agent`. Tool execution now builds deterministic structured RAG queries directly from incident fields, reducing unnecessary LLM calls, improving retrieval determinism, and lowering latency.

## Current Retrieval Categories

* performance
* database
* security
* infrastructure
* streaming
* general

## v2.2 Validation

```text
python -m compileall app tests
python -m pytest -q
```

Metadata retrieval validation confirmed 11 indexed runbooks, category metadata on every indexed document, and no missing category values.

# Version History

* v2.0 - Autonomous Tool Planning
* v2.1 - Incident Memory Intelligence
* v2.1.1 - Stability & Reliability Improvements
* v2.2 - Metadata-Aware Retrieval Intelligence

# Previous Release Notes

## OpsMind-AI v2.0 - Autonomous Tool Planning

OpsMind-AI v2.0 introduced autonomous tool-planning capabilities using LLM-driven orchestration.

## OpsMind-AI v2.1 - Incident Memory Intelligence

OpsMind-AI v2.1 introduced historical incident memory search into the RCA workflow. Similar past incidents can be retrieved and provided to the LLM as additional RCA context before safety validation and memory persistence.

## OpsMind-AI v2.1.1 - Stabilization Patch

OpsMind-AI v2.1.1 focused on reliability, repeatable tests, and release hygiene without changing the architecture.
