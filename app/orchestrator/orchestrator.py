from app.orchestrator.graph import graph
from app.memory.incident_memory import save_incident


def run_incident_workflow(incident):

    initial_state = {
        "incident": incident.model_dump()
    }

    result = graph.invoke(initial_state)

    save_incident(result)

    return result