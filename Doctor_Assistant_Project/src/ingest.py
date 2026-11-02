"""Ingestion: PDF/TXT -> text -> chunks -> JSON in data/processed/."""
import json
from pathlib import Path
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.config import (
    DATA_RAW_DIR, DATA_PROCESSED_DIR, CHUNK_SIZE, CHUNK_OVERLAP
)


def extract_pdf(path: Path) -> list[dict]:
    """Return list of {text, page} per page."""
    reader = PdfReader(str(path))
    pages = []
    for i, page in enumerate(reader.pages, start=1):
        txt = (page.extract_text() or "").strip()
        if txt:
            pages.append({"text": txt, "page": i})
    return pages


def extract_txt(path: Path) -> list[dict]:
    txt = path.read_text(encoding="utf-8", errors="ignore").strip()
    return [{"text": txt, "page": 1}] if txt else []


def chunk_pages(pages: list[dict], source: str) -> list[dict]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    chunks = []
    for p in pages:
        for j, c in enumerate(splitter.split_text(p["text"])):
            chunks.append({
                "text": c,
                "source": source,
                "page": p["page"],
                "chunk_id": f"{source}::p{p['page']}::c{j}",
            })
    return chunks


def ingest_file(path: Path) -> list[dict]:
    ext = path.suffix.lower()
    if ext == ".pdf":
        pages = extract_pdf(path)
    elif ext in (".txt", ".md"):
        pages = extract_txt(path)
    else:
        print(f"[skip] unsupported: {path.name}")
        return []
    chunks = chunk_pages(pages, path.name)
    print(f"[ok] {path.name}: {len(pages)} pages -> {len(chunks)} chunks")
    return chunks


def ingest_all() -> None:
    files = [p for p in DATA_RAW_DIR.iterdir() if p.is_file()]
    if not files:
        print(f"[warn] no files in {DATA_RAW_DIR}")
        return
    all_chunks = []
    for f in files:
        all_chunks.extend(ingest_file(f))
    out = DATA_PROCESSED_DIR / "chunks.json"
    out.write_text(json.dumps(all_chunks, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[done] wrote {len(all_chunks)} chunks -> {out}")


if __name__ == "__main__":
    ingest_all()
