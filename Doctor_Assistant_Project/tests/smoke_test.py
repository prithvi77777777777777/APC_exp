"""Smoke test: ingest -> embed -> retrieve -> answer, all in one command."""
import sys
from pathlib import Path

# Ensure project root is on path when run as `python tests/smoke_test.py`
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.config import DATA_RAW_DIR, COLLECTION_NAME
from src import ingest, embed_store
from src.rag_engine import retrieve, answer


def main() -> int:
    print("[1/4] ingest...")
    ingest.ingest_all()

    print("[2/4] embed...")
    embed_store.build_store(reset=False)

    from src.embed_store import get_collection
    count = get_collection().count()
    print(f"       collection '{COLLECTION_NAME}' count = {count}")
    if count == 0:
        print("FAIL: collection is empty")
        return 1

    print("[3/4] retrieve...")
    hits = retrieve("What is hypertension?", top_k=3)
    print(f"       hits = {len(hits)}")
    if not hits:
        print("FAIL: no hits retrieved")
        return 1

    print("[4/4] answer (calls Ollama)...")
    out = answer("What is hypertension?", top_k=3)
    if "answer" not in out or not out["answer"]:
        print("FAIL: empty answer")
        return 1
    if "disclaimer" not in out or not out["disclaimer"]:
        print("FAIL: missing disclaimer")
        return 1
    if "sources" not in out or not out["sources"]:
        print("FAIL: missing sources")
        return 1

    print("       answer[:80] =", out["answer"][:80].replace("\n", " "))
    print("       sources     =", out["sources"])
    print("\nSMOKE TEST PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())