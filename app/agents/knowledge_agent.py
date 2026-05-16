from pathlib import Path


def knowledge_agent(log_result):

    kb_file = Path("knowledge_base/payment-service-runbook.txt")

    if not kb_file.exists():
        return {
            "status": "KNOWLEDGE_NOT_FOUND",
            "recommendation": "No runbook available"
        }

    content = kb_file.read_text()

    if log_result["status"] == "OOM_ERROR_DETECTED":
        return {
            "status": "RUNBOOK_FOUND",
            "recommendation": content
        }

    return {
        "status": "NO_RECOMMENDATION",
        "recommendation": "No matching knowledge found"
    }