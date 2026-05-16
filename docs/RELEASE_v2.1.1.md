# OpsMind-AI v2.1.1

## Release Type

Patch release for OpsMind-AI v2.1 Incident Memory Intelligence.

## Summary

v2.1.1 delivers stabilization and reliability improvements for the v2.1 incident memory workflow. This release does not introduce a new architecture or redesign the existing orchestration flow.

## Fixes

* Stabilized incident memory writes by using ChromaDB upserts for repeatable ticket processing.
* Improved memory agent reliability with lazy initialization for ChromaDB and SentenceTransformers.
* Added safe fallback values for missing monitoring or log results when planner-selected tools vary.
* Fixed vector runbook recommendation truncation to cap returned text correctly.
* Replaced script-style memory validation with executable pytest coverage.
* Added pytest dependencies and ignored pytest cache artifacts.
* Cleaned README rendering for release documentation consistency.

## Validation

```text
python -m compileall app tests
python -m pytest -q
```

Both checks pass for v2.1.1.
