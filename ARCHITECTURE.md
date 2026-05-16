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



# OpsMind-AI v2.0 Architecture

## Autonomous Agentic Workflow

```text
Client/API Request
        ↓
FastAPI REST API
        ↓
LangGraph Orchestrator
        ↓
Planner Agent (LLM)
        ↓
Dynamic Tool Selection
        ↓
Tool Registry
        ↓
Dynamic Tool Execution
        ↓
Monitoring / Logs / RAG
        ↓
Shared Workflow State Enrichment
        ↓
LLM RCA Analysis
        ↓
Safety Validation
        ↓
Persistent Incident Memory
```

---

## Planner Agent

The Planner Agent uses Ollama + Mistral to dynamically determine which operational tools should execute for a given incident.

Example tool selection:

```json
{
  "selected_tools": [
    "monitoring",
    "logs",
    "rag"
  ]
}
```

---

## Tool Registry

The tool registry enables dynamic lookup and execution of operational tools.

Example:

```python
TOOLS = {
    "monitoring": monitoring_agent,
    "logs": log_analysis_agent,
    "rag": vector_knowledge_agent
}
```

---

## Dynamic Tool Executor

The Tool Executor dynamically invokes selected tools and enriches shared workflow state during runtime.

---

# OpsMind-AI v2.1.1 Architecture Note

v2.1.1 is a stabilization patch for the v2.1 Incident Memory Intelligence release. The architecture remains unchanged.

The patch improves reliability in the existing flow by:

* Making incident memory writes repeatable through ChromaDB upserts.
* Lazy-loading the incident memory vector store and embedding model.
* Providing safe LLM workflow defaults when planner-selected tool outputs are absent.
* Keeping historical incident retrieval as part of the established LangGraph workflow.

No new agents, orchestration layers, or architectural responsibilities are introduced in v2.1.1.
