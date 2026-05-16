# OpsMind-AI Architecture

# Current High-Level Workflow

```text
Client/API Request
        |
FastAPI REST API
        |
Pydantic Validation
        |
LangGraph Workflow Orchestration
        |
Planner Agent
        |
Dynamic Tool Execution
        |
Monitoring + Logs + Metadata-Aware RAG
        |
Historical Incident Memory Search
        |
LLM RCA Generation
        |
Safety Validation
        |
Persistent Incident Storage
        |
Final Incident Response
```

---

# Core Components

## FastAPI

Handles REST API requests and Swagger documentation.

## LangGraph

Controls workflow orchestration, shared state management, and agent execution flow.

## Planner Agent

Uses Ollama + Mistral to determine which operational tools are required for a given incident.

## Tool Registry and Tool Executor

The tool registry maps selected tool names to operational tool functions. The tool executor dynamically invokes those tools and enriches shared workflow state.

## Monitoring Agent

Simulates infrastructure and application monitoring analysis.

## Log Analysis Agent

Parses realistic production logs and operational stack traces.

## Vector Knowledge Agent

Performs semantic similarity search against operational runbooks using embeddings and category-aware metadata filters.

## Metadata-Aware Retrieval Layer

Runbooks are categorized during vector store indexing. Each ChromaDB document receives metadata containing its source file and operational category.

```python
metadata = {
    "source": file.name,
    "category": category
}
```

At query time, `vector_knowledge_agent.py` detects the incident category and filters ChromaDB retrieval:

```python
where={"category": category}
```

This narrows search to the most relevant operational domain and reduces semantic retrieval drift between unrelated categories.

## ChromaDB

Stores vector embeddings, semantic indexes, and runbook metadata used for category-filtered retrieval.

## SentenceTransformers

Generates embeddings for semantic retrieval.

## Ollama + Mistral

Provides local LLM-based reasoning and RCA generation.

## Retry Handler

Provides fault tolerance and retry mechanisms for unstable operations.

## Guardrails

Validates AI-generated outputs for operational safety.

## Persistent Memory

Stores incident history and RCA outputs, and supports historical incident retrieval during RCA generation.

---

# Agent Interaction Flow

```text
Planner Agent
        |
Dynamic Tool Execution
        |
Monitoring + Logs + Metadata-Aware RAG
        |
Historical Incident Memory Search
        |
LLM RCA Generation
        |
Safety Validation
        |
Persistent Incident Storage
```

---

# Metadata-Aware RAG

## Operational Categories

* performance
* database
* security
* infrastructure
* streaming
* general

## Current Runbook Corpus

* api-latency-runbook.txt
* auth-token-runbook.txt
* cpu-spike-runbook.txt
* database-connection-runbook.txt
* disk-space-runbook.txt
* jvm-memory-runbook.txt
* kafka-consumer-lag-runbook.txt
* payment-service-runbook.txt
* pod-crashloop-runbook.txt
* spring-security-runbook.txt
* thread-deadlock-runbook.txt

## Simplified Retrieval Flow

The active RAG path intentionally removes `retrieval_query_agent` from tool execution. Instead of calling an additional LLM to rewrite the retrieval query, `tool_executor.py` builds a deterministic structured query from incident fields and sends it directly to the Vector Knowledge Agent.

This improves determinism, reduces latency, and keeps retrieval behavior easier to reason about while preserving the existing Planner Agent and Tool Registry architecture.

---

# Version History

## v2.0 - Autonomous Tool Planning

Introduced LLM-driven planning, dynamic tool selection, the tool registry, and dynamic tool execution.

## v2.1 - Incident Memory Intelligence

Added historical incident memory search so similar past incidents can inform RCA generation.

## v2.1.1 - Stability & Reliability Improvements

Improved repeatability, safe workflow defaults, incident memory upserts, and test coverage without changing architecture.

## v2.2 - Metadata-Aware Retrieval Intelligence

Adds category-based vector filtering for runbooks, reduces retrieval drift across unrelated operational domains, removes `retrieval_query_agent` from the active RAG path, and improves retrieval determinism and latency without introducing new agents or redesigning orchestration.
