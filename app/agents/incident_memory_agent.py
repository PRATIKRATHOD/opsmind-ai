import json
from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer


model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_or_create_collection(
    name="incident_memory"
)


MEMORY_FILE = Path("memory_store.json")


def store_incident_memory(state):

    incident = state["incident"]

    llm_result = state.get(
        "llm_result",
        "No RCA available"
    )

    memory_text = f"""
    Application:
    {incident["application"]}

    Issue:
    {incident["issue"]}

    RCA:
    {llm_result}
    """

    embedding = model.encode(
        memory_text
    ).tolist()

    collection.add(
        documents=[memory_text],
        embeddings=[embedding],
        ids=[incident["ticket_id"]]
    )

    print(
        f"Stored incident memory: "
        f'{incident["ticket_id"]}'
    )

    return {
        "status": "MEMORY_STORED"
    }


def search_similar_incidents(query):

    embedding = model.encode(
        query
    ).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=2
    )

    documents = results["documents"][0]

    if not documents:

        return {
            "status": "NO_SIMILAR_INCIDENTS"
        }

    return {
        "status": "SIMILAR_INCIDENTS_FOUND",
        "matches": documents
    }