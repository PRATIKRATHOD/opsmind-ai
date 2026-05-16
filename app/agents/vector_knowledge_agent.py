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


def vector_knowledge_agent(query):

    print("Running Vector Knowledge Search")

    embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=1
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
