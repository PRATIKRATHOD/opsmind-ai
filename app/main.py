from fastapi import FastAPI
from app.models.incident import Incident
from app.orchestrator.orchestrator import run_incident_workflow
from app.memory.incident_memory import (
    get_all_incidents,
    get_incident_by_ticket
)

app = FastAPI(title="OpsMind AI")


@app.get("/")
def home():
    return {
        "message": "OpsMind AI is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/incident")
def create_incident(incident: Incident):

    result = run_incident_workflow(incident)

    return result

@app.get("/incidents")
def get_incidents():

    return get_all_incidents()
 

@app.get("/incident/{ticket_id}")
def get_incident(ticket_id: str):

    result = get_incident_by_ticket(ticket_id)

    if result:
        return result

    return {
        "message": "Incident not found"
    }