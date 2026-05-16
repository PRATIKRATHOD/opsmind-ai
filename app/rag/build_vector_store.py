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

for file in files:

    print("Reading:", file.name)

    content = file.read_text(
        encoding="utf-8",
        errors="ignore"
    )

    embedding = model.encode(content).tolist()

    collection.add(
        documents=[content],
        embeddings=[embedding],
        ids=[file.stem]
    )

    print("Indexed:", file.name)

print("Vector store build complete")