"""Embed chunks and store in persistent ChromaDB."""
import json
import sys
import chromadb
import torch
from chromadb.utils import embedding_functions

from src.config import (
    DATA_PROCESSED_DIR, CHROMA_DIR, COLLECTION_NAME, EMBEDDING_MODEL
)


def _embedder():
    # The `device="cpu"` flag fixes the "meta tensor" Windows bug
    return embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=EMBEDDING_MODEL,
        device="cpu" 
    )


def get_client():
    return chromadb.PersistentClient(
        path=str(CHROMA_DIR), 
        settings=chromadb.Settings(anonymized_telemetry=False)
    )


def get_collection(reset: bool = False):
    client = get_client()
    if reset:
        try:
            client.delete_collection(COLLECTION_NAME)
            print(f"[reset] dropped collection: {COLLECTION_NAME}")
        except Exception:
            pass
    return client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=_embedder(),
        metadata={"hnsw:space": "cosine"},
    )


def build_store(reset: bool = False, progress_callback=None) -> None:
    chunks_path = DATA_PROCESSED_DIR / "chunks.json"
    if not chunks_path.exists():
        print(f"[error] missing {chunks_path}. Run: python -m src.ingest")
        return

    chunks = json.loads(chunks_path.read_text(encoding="utf-8"))
    if not chunks:
        print("[warn] chunks.json is empty")
        return

    col = get_collection(reset=reset)

    ids = [c["chunk_id"] for c in chunks]
    docs = [c["text"] for c in chunks]
    metas = [{"source": c["source"], "page": c["page"]} for c in chunks]

    BATCH = 64
    total_batches = (len(ids) + BATCH - 1) // BATCH
    
    for i in range(0, len(ids), BATCH):
        col.upsert(
            ids=ids[i:i+BATCH],
            documents=docs[i:i+BATCH],
            metadatas=metas[i:i+BATCH],
        )
        
        if progress_callback:
            current_batch = (i // BATCH) + 1
            progress_callback(current_batch, total_batches)
        else:
            print(f"[upsert] {min(i+BATCH, len(ids))}/{len(ids)}")

    if not progress_callback:
        print(f"[done] collection '{COLLECTION_NAME}' count = {col.count()}")


if __name__ == "__main__":
    build_store(reset=("--reset" in sys.argv))