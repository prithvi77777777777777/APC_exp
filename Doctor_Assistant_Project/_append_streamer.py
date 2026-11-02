import pathlib

ADD = r"""

# ---------------- Streaming API (for Streamlit) ----------------
class AnswerStreamer:
    """Wraps Ollama streaming. Call .stream() for tokens; after exhaustion,
    .sources and .disclaimer hold the citations and disclaimer."""

    def __init__(self, question: str, top_k: int = TOP_K):
        self.question = question
        self.top_k = top_k
        self.sources: list[dict] = []
        self.disclaimer: str = DISCLAIMER
        self.error = None
        self._hits = retrieve(question, top_k=top_k)

    def stream(self):
        if not self._hits:
            self.sources = []
            yield "No relevant excerpts found in the indexed textbooks."
            return

        self.sources = _dedupe_sources(self._hits)
        prompt = _build_prompt(self.question, self._hits)

        try:
            client = ollama.Client(host=OLLAMA_HOST)
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
"""

p = pathlib.Path("src/rag_engine.py")
src = p.read_text(encoding="utf-8")
p.write_text(src + ADD, encoding="utf-8")
print("appended", len(ADD), "chars")
