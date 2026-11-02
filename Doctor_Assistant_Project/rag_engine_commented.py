"""
RAG Engine (Commented Version): Retrieve from Chroma -> prompt -> Ollama -> citation + disclaimer.
This file explains the Retrieval-Augmented Generation (RAG) process step-by-step.
"""
from __future__ import annotations
from typing import Any
import ollama

from src.config import (
    OLLAMA_MODEL, OLLAMA_HOST, LLM_TEMPERATURE, LLM_NUM_CTX,
    TOP_K, DISCLAIMER,
)
from src.embed_store import get_collection


# ---------------------------------------------------------
# 1. THE SYSTEM PROMPT (The Guardrails)
# ---------------------------------------------------------
# This text is sent to the AI first. It acts as a strict rulebook.
# It forces the AI to answer ONLY from the textbook excerpts, and explicitly tells it to 
# admit when it doesn't know the answer. This is the primary defense against AI hallucinations.
SYSTEM_PROMPT = (
    "You are a medical reference assistant for qualified doctors. "
    "Answer STRICTLY using the provided textbook excerpts. "
    "If the excerpts do not contain the answer, say: "
    "'The provided textbook excerpts do not cover this.' "
    "Do not invent facts, do not use outside knowledge, do not give "
    "patient-specific advice. Be concise, use clinical terminology, "
    "and structure the answer with short bullet points where helpful."
)


# ---------------------------------------------------------
# 2. FORMATTING THE CONTEXT
# ---------------------------------------------------------
def _format_context(hits: list[dict[str, Any]]) -> str:
    """
    Takes the raw text chunks retrieved from ChromaDB and formats them nicely.
    It numbers them (Excerpt 1, Excerpt 2) and includes the source book and page number
    so the AI knows exactly where the text came from.
    """
    lines = []
    for i, h in enumerate(hits, start=1):
        lines.append(
            f"[Excerpt {i}] Source: {h['source']} (page {h['page']})\n{h['text']}"
        )
    return "\n\n".join(lines)


# ---------------------------------------------------------
# 3. BUILDING THE PROMPT
# ---------------------------------------------------------
def _build_prompt(question: str, hits: list[dict[str, Any]]) -> str:
    """
    Combines everything into one giant string to send to the AI.
    Structure: [Rules] + [Textbook Excerpts] + [Doctor's Question] + [Answer Trigger]
    """
    return (
        f"{SYSTEM_PROMPT}\n\n"
        f"=== TEXTBOOK EXCERPTS ===\n{_format_context(hits)}\n\n"
        f"=== DOCTOR'S QUESTION ===\n{question}\n\n"
        f"=== ANSWER (grounded in excerpts above) ==="
    )


# ---------------------------------------------------------
# 4. CLEANING SOURCES
# ---------------------------------------------------------
def _dedupe_sources(hits: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    If the system retrieved three different chunks from Page 45, this function 
    removes the duplicates so the UI only shows 'Page 45' once. Keeps the source list clean.
    """
    seen, out = set(), []
    for h in hits:
        key = (h["source"], h["page"])
        if key not in seen:
            seen.add(key)
            out.append({"source": h["source"], "page": h["page"]})
    return out


# ---------------------------------------------------------
# 5. RETRIEVAL (Searching the Database)
# ---------------------------------------------------------
def retrieve(question: str, top_k: int = TOP_K) -> list[dict[str, Any]]:
    """
    The 'R' in RAG.
    Takes the user's question, converts it to a vector, and searches ChromaDB 
    for the `top_k` (default 4) most mathematically similar paragraphs.
    Includes a safety check to ensure the database isn't empty.
    """
    col = get_collection()
    if col.count() == 0:
        return []
    res = col.query(query_texts=[question], n_results=top_k)
    docs = res.get("documents", [[]])[0]
    metas = res.get("metadatas", [[]])[0]
    hits = []
    for doc, meta in zip(docs, metas):
        hits.append({
            "text": doc,
            "source": meta.get("source", "unknown"),
            "page": meta.get("page", 0),
        })
    return hits


# ---------------------------------------------------------
# 6. GENERATION (Standard Non-Streaming Method)
# ---------------------------------------------------------
def answer(question: str, top_k: int = TOP_K) -> dict[str, Any]:
    """
    The 'G' in RAG (Standard version).
    Retrieves the text, builds the prompt, and sends it to Ollama.
    It waits for the AI to finish the entire answer before returning it.
    It includes a try/except block to catch errors if the Ollama server is turned off.
    """
    hits = retrieve(question, top_k=top_k)
    if not hits:
        return {
            "answer": "No relevant excerpts found in the indexed textbooks.",
            "sources": [],
            "disclaimer": DISCLAIMER,
        }

    prompt = _build_prompt(question, hits)
    try:
        client = ollama.Client(host=OLLAMA_HOST)
        resp = client.chat(
            model=OLLAMA_MODEL,
            messages=[{"role": "user", "content": prompt}],
            options={"temperature": LLM_TEMPERATURE, "num_ctx": LLM_NUM_CTX},
        )
        answer_text = resp["message"]["content"].strip()
    except Exception as e:
        # Graceful fallback if Ollama is down
        return {
            "answer": f"Ollama error: {e}. Is the server running? Try: ollama serve",
            "sources": _dedupe_sources(hits),
            "disclaimer": DISCLAIMER,
        }

    return {
        "answer": answer_text,
        "sources": _dedupe_sources(hits),
        "disclaimer": DISCLAIMER,
    }


# ---------------------------------------------------------
# 7. STREAMING API (Used by the Streamlit UI)
# ---------------------------------------------------------
class AnswerStreamer:
    """
    This class is what powers the web UI. 
    Instead of waiting 10 seconds for the AI to finish, it streams the text 
    word-by-word (token-by-token) using Python's `yield` generator.
    This creates the 'typing' effect on the screen.
    """

    def __init__(self, question: str, top_k: int = TOP_K):
        self.question = question
        self.top_k = top_k
        self.sources: list[dict] = []
        self.disclaimer: str = DISCLAIMER
        self.error = None
        # Retrieve the context immediately when the class is created
        self._hits = retrieve(question, top_k=top_k)

    def stream(self):
        """
        The generator that yields the text chunks to the UI.
        """
        if not self._hits:
            self.sources = []
            yield "No relevant excerpts found in the indexed textbooks."
            return

        self.sources = _dedupe_sources(self._hits)
        prompt = _build_prompt(self.question, self._hits)

        try:
            client = ollama.Client(host=OLLAMA_HOST)
            # The magic happens here: stream=True
            for chunk in client.chat(
                model=OLLAMA_MODEL,
                messages=[{"role": "user", "content": prompt}],
                options={"temperature": LLM_TEMPERATURE, "num_ctx": LLM_NUM_CTX},
                stream=True,
            ):
                piece = chunk.get("message", {}).get("content", "")
                if piece:
                    yield piece
        except Exception as e:
            self.error = str(e)
            yield f"Ollama error: {e}. Is the server running? Try: ollama serve"
