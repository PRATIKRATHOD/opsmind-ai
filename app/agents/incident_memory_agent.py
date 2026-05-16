import chromadb
from sentence_transformers import SentenceTransformer


_model = None
_collection = None


def _get_model():

    global _model

    if _model is None:
        _model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

    return _model


def _get_collection():

    global _collection

    if _collection is None:
        client = chromadb.PersistentClient(
            path="chroma_db"
        )

        _collection = client.get_or_create_collection(
            name="incident_memory"
        )

    return _collection


def _encode_text(text):

    embedding = _get_model().encode(
        text
    )

    if hasattr(embedding, "tolist"):
        return embedding.tolist()

    return list(embedding)


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

    embedding = _encode_text(
        memory_text
    )

    _get_collection().upsert(
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

    embedding = _encode_text(
        query
    )

    results = _get_collection().query(
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
