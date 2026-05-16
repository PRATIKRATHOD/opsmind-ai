from typing import TypedDict

from langgraph.graph import StateGraph, END

from app.agents.monitoring_agent import monitoring_agent
from app.agents.log_analysis_agent import log_analysis_agent
from app.agents.vector_knowledge_agent import (
    vector_knowledge_agent
)
from app.agents.llm_analysis_agent import llm_analysis_agent
from app.safety.guardrails import validate_ai_recommendation
from app.reliability.retry_handler import execute_with_retry


class IncidentState(TypedDict):

    incident: dict

    monitoring_result: dict

    log_result: dict

    knowledge_result: dict

    llm_result: str

    safety_result: dict


def monitoring_node(state):
    print("Running Monitoring Node")

    result = monitoring_agent(state["incident"])

    state["monitoring_result"] = result

    return state


def log_analysis_node(state):
    print("Running Log Node")

    result = log_analysis_agent(state["incident"])

    state["log_result"] = result

    return state

#Descoped as we moved to vector DB semantic search
# def knowledge_node(state):
#     print("Running Knowledge Node")

#     result = knowledge_agent(state["log_result"])

#     state["knowledge_result"] = result

#     return state

def knowledge_node(state):

    print("Running Knowledge Node")

    query = f"""
    Application Name:
    {state["incident"]["application"]}

    Incident Category:
    {state["incident"]["issue"]}

    Monitoring Signals:
    {state["monitoring_result"]["status"]}

    Monitoring Details:
    {state["monitoring_result"]["details"]}

    Log Analysis:
    {state["log_result"]["details"]}

    Find the most operationally relevant troubleshooting runbook.
    """

    result = vector_knowledge_agent(query)

    state["knowledge_result"] = result

    return state

def llm_node(state):

    print("Running LLM Node")

    knowledge_result = state.get(
        "knowledge_result",
        {
            "status": "SKIPPED",
            "recommendation": "Knowledge retrieval skipped"
        }
    )

    try:

        result = execute_with_retry(
            lambda: llm_analysis_agent(
                state["incident"],
                state["monitoring_result"],
                state["log_result"],
                knowledge_result
            )
        )

    except Exception as error:

        result = f"""
        LLM analysis failed after retries.

        Error:
        {str(error)}

        Fallback response generated.
        """

    state["llm_result"] = result

    return state


def safety_node(state):
    print("Running Safty Node")

    result = validate_ai_recommendation(
        state["llm_result"]
    )

    state["safety_result"] = result

    return state

# def route_after_logs(state):

#     log_status = state["log_result"]["status"]

#     if log_status == "OOM_ERROR_DETECTED":
#         return "knowledge"

#     return "llm"

workflow = StateGraph(IncidentState)

workflow.add_node("monitoring", monitoring_node)

workflow.add_node("logs", log_analysis_node)

workflow.add_node("knowledge", knowledge_node)

workflow.add_node("llm", llm_node)

workflow.add_node("safety", safety_node)

workflow.set_entry_point("monitoring")

workflow.add_edge("monitoring", "logs")

workflow.add_edge("logs", "knowledge")

# Adding Conditional Edge
# workflow.add_conditional_edges(
#     "logs",
#     route_after_logs
# )

workflow.add_edge("knowledge", "llm")

workflow.add_edge("llm", "safety")

workflow.add_edge("safety", END)

graph = workflow.compile()