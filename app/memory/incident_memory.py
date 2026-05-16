import json
from pathlib import Path


MEMORY_FILE = Path("memory_store.json")


def load_memory():

    if not MEMORY_FILE.exists():
        return []

    try:

        with open(MEMORY_FILE, "r") as file:
            return json.load(file)

    except Exception:

        return []


def save_incident(incident_data):

    memory = load_memory()

    memory.append(incident_data)

    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)


def get_all_incidents():

    return load_memory()


def get_incident_by_ticket(ticket_id):

    memory = load_memory()

    for incident in memory:

        incident_ticket = incident["incident"]["ticket_id"]

        if incident_ticket == ticket_id:
            return incident

    return None