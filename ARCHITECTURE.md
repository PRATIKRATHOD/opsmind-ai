# OpsMind-AI Architecture

# High-Level Workflow

```text
Client/API Request
        ↓
FastAPI REST API
        ↓
Pydantic Validation
        ↓
LangGraph Workflow Orchestration
        ↓
Monitoring Agent
        ↓
Log Analysis Agent
        ↓
Vector RAG Knowledge Retrieval
        ↓
ChromaDB Semantic Search
        ↓
LLM RCA Analysis (Ollama + Mistral)
        ↓
Retry/Reliability Layer
        ↓
Safety Guardrails
        ↓
Persistent Memory Storage
        ↓
Final Incident Response
```

---

# Core Components

## FastAPI

Handles REST API requests and Swagger documentation.

## LangGraph

Controls workflow orchestration, shared state management, and agent execution flow.

## Monitoring Agent

Simulates infrastructure and application monitoring analysis.

## Log Analysis Agent

Parses realistic production logs and operational stack traces.

## Vector Knowledge Agent

Performs semantic similarity search against operational runbooks using embeddings.

## ChromaDB

Stores vector embeddings and semantic indexes.

## SentenceTransformers

Generates embeddings for semantic retrieval.

## Ollama + Mistral

Provides local LLM-based reasoning and RCA generation.

## Retry Handler

Provides fault tolerance and retry mechanisms for unstable operations.

## Guardrails

Validates AI-generated outputs for operational safety.

## Persistent Memory

Stores incident history and RCA outputs in memory_store.json.
