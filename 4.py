from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
import os

try:
    print("Loading embedding model")
    model = SentenceTransformer("all-MiniLM-L6-v2")

    # Sample text
    document_text = "Dick stood on the coral ledge, looking toward the horizon. The lagoon behind him shimmered in the sun."

    # --- Create embedding ---
    print("Generating embedding")
    embedding = model.encode(document_text)

    # --- Setup ChromaDB ---
    print("📦 Setting up ChromaDB client...")
    chroma_client = chromadb.Client(Settings(persist_directory="./chroma_storage", chroma_db_impl="duckdb+parquet"))

    collection = chroma_client.get_or_create_collection("book_chapters")

    collection.add(
        documents=[document_text],
        metadatas=[{"chapter": "1", "source": "test_script"}],
        ids=["doc1"]
    )

    print("Document stored in ChromaDB with embedding.")

except Exception as e:
    print("error", e)

