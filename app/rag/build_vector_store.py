import chromadb
from sentence_transformers import SentenceTransformer
from pathlib import Path

client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_or_create_collection(
    name="incident_runbooks"
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

knowledge_path = Path("knowledge_base")

files = knowledge_path.glob("*.txt")

def detect_category(file_name):

    lower = file_name.lower()

    if (
        "latency" in lower
        or "cpu" in lower
        or "memory" in lower
        or "deadlock" in lower
    ):
        return "performance"

    if (
        "database" in lower
        or "payment" in lower
    ):
        return "database"

    if (
        "auth" in lower
        or "security" in lower
    ):
        return "security"

    if (
        "disk" in lower
        or "pod" in lower
    ):
        return "infrastructure"

    if "kafka" in lower:
        return "streaming"

    return "general"

for file in files:

    print("Reading:", file.name)

    content = file.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    embedding = model.encode(content).tolist()

    category = detect_category(
        file.name
    )

    metadata = {
        "source": file.name,
        "category": category
    }

    collection.upsert(
        documents=[content],
        embeddings=[embedding],
        metadatas=[metadata],
        ids=[file.stem]
    )

    print("Indexed:", file.name)

print("Vector store build complete")