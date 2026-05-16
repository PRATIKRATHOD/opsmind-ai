# OpsMind-AI v2.2

## Release Summary

OpsMind-AI v2.2 introduces Metadata-Aware Retrieval Intelligence. This release improves RAG accuracy by categorizing runbooks during vector store indexing and applying category-based ChromaDB metadata filters during retrieval.

v2.2 is an architecture refinement, not an orchestration redesign. It preserves the existing Planner Agent, Dynamic Tool Execution, historical memory search, LLM RCA generation, safety validation, and persistent incident storage flow.

## Major Improvements

* Added metadata categorization during vector store indexing.
* Added category-aware retrieval filtering in `vector_knowledge_agent.py`.
* Added `detect_category()` in `build_vector_store.py`.
* Added `detect_query_category()` in `vector_knowledge_agent.py`.
* Updated ChromaDB retrieval to use `where={"category": category}`.
* Rebuilt the vector database with runbook metadata.
* Removed `retrieval_query_agent` from the active RAG execution path.
* Replaced LLM-based retrieval query rewriting with deterministic structured queries.
* Reduced unnecessary LLM calls to improve latency and retrieval determinism.
* Reduced semantic retrieval drift across unrelated operational domains.

## Architecture Evolution

Final v2.2 flow:

```text
Planner Agent
-> Dynamic Tool Execution
-> Monitoring + Logs + Metadata-Aware RAG
-> Historical Incident Memory Search
-> LLM RCA Generation
-> Safety Validation
-> Persistent Incident Storage
```

The retrieval layer now uses operational categories to keep semantic search focused:

* performance
* database
* security
* infrastructure
* streaming
* general

## Validation

Release validation completed:

```text
python -m compileall app tests
python -m pytest -q
```

Results:

* `compileall` completed successfully.
* `pytest` passed with 2 tests and 1 dependency deprecation warning from ChromaDB.
* Metadata retrieval validation found 11 indexed runbooks.
* All indexed runbooks include category metadata.
* No indexed runbooks are missing category values.

Metadata retrieval validation covered:

* Indexed runbooks include `source` and `category` metadata.
* Queries resolve to one of the supported operational categories.
* ChromaDB retrieval applies `where={"category": category}`.
* RAG responses stay within the intended operational domain.

## Version History

* v2.0 - Autonomous Tool Planning
* v2.1 - Incident Memory Intelligence
* v2.1.1 - Stability & Reliability Improvements
* v2.2 - Metadata-Aware Retrieval Intelligence

## Migration Notes

* Rebuild the vector database after upgrading so existing runbook embeddings include category metadata.
* The active RAG path no longer uses `retrieval_query_agent`.
* Existing incident submission APIs and LangGraph orchestration remain unchanged.
* Existing memory storage and historical incident retrieval remain compatible.

## Future Roadmap Hints

* Add retrieval evaluation cases for every operational category.
* Track retrieval precision by category.
* Add confidence scores or fallback behavior for low-signal queries.
* Expand metadata dimensions beyond category, such as application, severity, or platform.

## GitHub Release Notes

OpsMind-AI v2.2 adds Metadata-Aware Retrieval Intelligence for more accurate and deterministic RAG.

Highlights:

* Category-aware ChromaDB filtering for operational runbooks.
* Reduced semantic retrieval drift across unrelated domains.
* Deterministic structured RAG queries replacing LLM query rewriting.
* Removed `retrieval_query_agent` from active tool execution to reduce latency and complexity.
* Preserved the existing v2 Planner -> Tools -> Memory -> RCA architecture.
