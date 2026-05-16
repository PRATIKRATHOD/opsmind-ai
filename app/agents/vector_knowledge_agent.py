import chromadb

from sentence_transformers import SentenceTransformer


client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_collection(
    name="incident_runbooks"
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def detect_query_category(query):

    lower = query.lower()

    if (
        "latency" in lower
        or "timeout" in lower
        or "performance" in lower
        or "cpu" in lower
    ):
        return "performance"

    if (
        "database" in lower
        or "pool" in lower
        or "sql" in lower
    ):
        return "database"

    if (
        "auth" in lower
        or "jwt" in lower
        or "security" in lower
    ):
        return "security"

    if (
        "disk" in lower
        or "pod" in lower
        or "kubernetes" in lower
    ):
        return "infrastructure"

    if "kafka" in lower:
        return "streaming"

    return "general"

def vector_knowledge_agent(query):

    print("Running Vector Knowledge Search")
    category = detect_query_category(
        query
    )

    print(f"Detected category: {category}")

    embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=1,
        where={"category": category}
    )

    documents = results["documents"][0]

    if documents:

        return {
            "status": "VECTOR_MATCH_FOUND",
            "recommendation": documents[0][:1000]
        }

    return {
        "status": "NO_VECTOR_MATCH",
        "recommendation": "No relevant runbook found"
    }
