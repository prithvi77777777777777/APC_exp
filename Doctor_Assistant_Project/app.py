"""Streamlit UI for the Doctor Assistant - Final Clinical Edition."""
import streamlit as st
import time
import hashlib
import json
from src.config import OLLAMA_MODEL, TOP_K, DISCLAIMER, DATA_RAW_DIR, DATA_PROCESSED_DIR
from src.rag_engine import AnswerStreamer
from src.embed_store import get_collection
from src import ingest as _ing
from src import embed_store as _es

st.set_page_config(page_title="Doctor Assistant (Liquid Glass)", page_icon="🩺", layout="wide")

# 1. Inject Advanced visionOS CSS (Fixed White Bars & Uploader)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        color: #f8fafc !important;
    }

    /* Background Mesh */
    .stApp {
        background: radial-gradient(circle at 15% 50%, rgba(76, 29, 149, 0.4), transparent 50%),
                    radial-gradient(circle at 85% 30%, rgba(14, 165, 233, 0.3), transparent 50%),
                    #09090b !important;
        background-attachment: fixed;
    }

    /* Transparent Top Header */
    header[data-testid="stHeader"] {
        background: transparent !important;
    }

    /* NUKE THE WHITE BOTTOM BAR */
    [data-testid="stBottomBlockContainer"], .stBottom, [data-testid="stAppViewBlockContainer"] {
        background: transparent !important;
        background-color: transparent !important;
    }

    /* 1. The outermost glass container */
    [data-testid="stChatInput"] {
        background: rgba(20, 20, 25, 0.7) !important;
        backdrop-filter: blur(20px) !important;
        -webkit-backdrop-filter: blur(20px) !important;
        border-radius: 30px !important;
        border: 1px solid rgba(255, 255, 255, 0.15) !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.4) !important;
    }

    /* 2. Kill the white background on ALL child wrappers */
    [data-testid="stChatInput"] * {
        background-color: transparent !important;
        background: transparent !important;
    }

    /* 3. Re-apply the dark background only to the main container (in case * killed it) */
    [data-testid="stChatInput"] {
        background-color: rgba(20, 20, 25, 0.7) !important;
    }

    /* 4. Style the actual typing area */
    [data-testid="stChatInput"] textarea {
        color: #ffffff !important;
        font-size: 1.05rem !important;
        caret-color: #a78bfa !important; /* Purple cursor */
        border: none !important;
        outline: none !important;
        box-shadow: none !important;
    }

    /* 5. Remove the red error/focus ring */
    [data-testid="stChatInput"] div[data-baseweb="base-input"],
    [data-testid="stChatInput"] div[data-baseweb="textarea"] {
        border: none !important;
        border-color: transparent !important;
        box-shadow: none !important;
        outline: none !important;
    }

    /* 6. Force text to stay white on focus */
    [data-testid="stChatInput"] textarea:focus {
        color: #ffffff !important;
        background-color: transparent !important;
    }

    /* 7. Fix text selection highlight */
    [data-testid="stChatInput"] textarea::selection {
        background-color: rgba(167, 139, 250, 0.6) !important;
        color: #ffffff !important;
    }
    
    /* FIX: When text is highlighted/selected, make background purple and text white */
    [data-testid="stChatInput"] textarea::selection {
        background-color: rgba(167, 139, 250, 0.5) !important; /* Purple highlight */
        color: #ffffff !important;
    }

    /* FIX: When the user actually focuses/clicks to type, force the background to stay dark glass */
    [data-testid="stChatInput"]:focus-within {
        background: rgba(20, 20, 25, 0.9) !important; /* Dark background */
        border: 1px solid rgba(167, 139, 250, 0.6) !important; /* Purple border glow */
    }
    
    /* FIX: When text is highlighted/selected, make background purple and text white */
    [data-testid="stChatInput"] textarea::selection {
        background-color: rgba(167, 139, 250, 0.5) !important; /* Purple highlight */
        color: #ffffff !important;
    }

    /* FIX: When the user actually focuses/clicks to type, force the background to stay dark glass */
    [data-testid="stChatInput"]:focus-within {
        background: rgba(20, 20, 25, 0.9) !important; /* Dark background */
        border: 1px solid rgba(167, 139, 250, 0.6) !important; /* Purple border glow */
    }
    
    /* FIX: When text is highlighted/selected, make background purple and text white */
    [data-testid="stChatInput"] textarea::selection {
        background-color: rgba(167, 139, 250, 0.5) !important; /* Purple highlight */
        color: #ffffff !important;
    }

    /* FIX: When the user actually focuses/clicks to type, force the background to stay dark glass */
    [data-testid="stChatInput"]:focus-within {
        background: rgba(20, 20, 25, 0.9) !important; /* Dark background */
        border: 1px solid rgba(167, 139, 250, 0.6) !important; /* Purple border glow */
    }

    /* Glass Sidebar */
    [data-testid="stSidebar"] {
        background: rgba(20, 20, 25, 0.4) !important;
        backdrop-filter: blur(24px) saturate(150%);
        -webkit-backdrop-filter: blur(24px) saturate(150%);
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Force File Uploader to be Dark Glass */
    [data-testid="stFileUploadDropzone"] {
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px dashed rgba(255, 255, 255, 0.2) !important;
        border-radius: 16px;
    }
    [data-testid="stFileUploadDropzone"] span, 
    [data-testid="stFileUploadDropzone"] div {
        color: #cbd5e1 !important;
    }
    [data-testid="stFileUploadDropzone"] button {
        background: rgba(255,255,255,0.1) !important;
        color: white !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
    }

    /* Glass Chat Messages */
    div[data-testid="stChatMessage"] {
        background: rgba(255, 255, 255, 0.05) !important;
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border-radius: 24px;
        padding: 1.2rem;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
        margin-bottom: 1.5rem;
    }

    /* Glass Buttons & Suggested Prompts */
    .stButton>button {
        background: rgba(255, 255, 255, 0.08) !important;
        color: #ffffff !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        border-radius: 12px;
        backdrop-filter: blur(10px);
        transition: all 0.3s ease;
        width: 100%;
    }
    .stButton>button:hover {
        background: rgba(255, 255, 255, 0.2) !important;
        box-shadow: 0 0 15px rgba(255,255,255,0.15);
    }

    /* Fix Disclaimer Box */
    [data-testid="stNotification"] {
        background: rgba(255, 150, 50, 0.1) !important;
        border: 1px solid rgba(255, 150, 50, 0.3) !important;
        border-radius: 12px;
        color: #fcd34d !important;
    }
    
    /* Typography */
    h1 {
        font-weight: 700 !important;
        background: -webkit-linear-gradient(45deg, #fff, #a78bfa);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 20px rgba(167, 139, 250, 0.3);
    }
    p, span {
        color: #e2e8f0 !important;
    }

    /* --- GLOBAL WHITE BACKGROUND FIXES --- */
    /* 1. Fix the white bar at the bottom of the screen */
    [data-testid='stBottomBlockContainer'], .stBottom, [data-testid='stAppViewBlockContainer'] {
        background: transparent !important;
        background-color: transparent !important;
    }

    /* 2. Nuke the white file uploader box */
    [data-testid='stFileUploadDropzone'] {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px dashed rgba(255, 255, 255, 0.2) !important;
    }
    [data-testid='stFileUploadDropzone'] span, 
    [data-testid='stFileUploadDropzone'] div,
    [data-testid='stFileUploadDropzone'] small {
        color: #cbd5e1 !important;
    }
    [data-testid='stFileUploadDropzone'] button {
        background-color: rgba(255,255,255,0.1) !important;
        color: white !important;
        border: 1px solid rgba(255,255,255,0.2) !important;
    }

    /* 3. Fix the white Export Answer & Clear Chat buttons */
    .stDownloadButton > button, .stButton > button {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: #ffffff !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
    }
    .stDownloadButton > button:hover, .stButton > button:hover {
        background-color: rgba(255, 255, 255, 0.2) !important;
    }
    
    /* 4. Fix text inside the chat messages (so it is not dark grey on dark glass) */
    [data-testid='stChatMessage'] p, 
    [data-testid='stChatMessage'] li,
    [data-testid='stChatMessage'] span {
        color: #e2e8f0 !important;
    }

    /* 5. Fix the sidebar warning box (Disclaimer) */
    [data-testid='stNotification'] {
        background-color: rgba(255, 150, 50, 0.1) !important;
        border: 1px solid rgba(255, 150, 50, 0.3) !important;
    }
    [data-testid='stNotification'] p {
        color: #fcd34d !important;
    }

    /* --- THE REAL WHITE BACKGROUND FIX --- */
    [data-testid='stBottomBlockContainer'], 
    [data-testid='stBottom'], 
    [data-testid='stAppViewBlockContainer'],
    .stBottom {
        background-color: transparent !important;
        background: transparent !important;
    }

    section[data-testid='stFileUploadDropzone'] {
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px dashed rgba(255, 255, 255, 0.2) !important;
    }
    section[data-testid='stFileUploadDropzone'] small, 
    section[data-testid='stFileUploadDropzone'] span {
        color: #94a3b8 !important;
    }
    section[data-testid='stFileUploadDropzone'] button {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: #ffffff !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
    }

    .stButton > button, 
    .stDownloadButton > button {
        background-color: rgba(255, 255, 255, 0.1) !important;
        color: #ffffff !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        width: 100%;
    }
    .stButton > button:hover, 
    .stDownloadButton > button:hover {
        background-color: rgba(255, 255, 255, 0.2) !important;
        color: #ffffff !important;
    }

    [data-testid='stChatInput'] textarea::selection {
        background-color: rgba(167, 139, 250, 0.5) !important;
        color: white !important;
    }
</style>


""", unsafe_allow_html=True)

# ---------------- Session state ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []
if "pending_prompt" not in st.session_state:
    st.session_state.pending_prompt = None

HASH_FILE = DATA_PROCESSED_DIR / "uploaded_hashes.json"

def load_hashes():
    if not HASH_FILE.exists(): return {}
    try: return json.loads(HASH_FILE.read_text(encoding="utf-8"))
    except: return {}

def save_hash(file_hash, filename):
    hashes = load_hashes()
    hashes[file_hash] = filename
    HASH_FILE.write_text(json.dumps(hashes, indent=2), encoding="utf-8")

# ---------------- Sidebar ----------------
with st.sidebar:
    st.title("🩺 Doctor AI")
    st.caption("Clinical Edition")
    
    st.markdown(f"**Model:** `{OLLAMA_MODEL}`")
    try:
        count = get_collection().count()
    except Exception as e:
        count = f"error ({e})"
    st.markdown(f"**Indexed chunks:** `{count}`")

    st.divider()
    st.subheader("Add a Book")
    
    uploaded_file = st.file_uploader("Upload a PDF textbook", type=["pdf"])
    
    if uploaded_file is not None:
        file_bytes = uploaded_file.getbuffer()
        file_hash = hashlib.sha256(file_bytes).hexdigest()
        existing_hashes = load_hashes()
        
        if file_hash in existing_hashes:
            st.warning(f"⚠️ '{existing_hashes[file_hash]}' is already indexed.")
        else:
            if st.button("Process Book"):
                status_text = st.empty()
                progress_bar = st.progress(0)
                
                try:
                    status_text.info("Saving PDF...")
                    progress_bar.progress(10)
                    save_path = DATA_RAW_DIR / uploaded_file.name
                    with open(save_path, "wb") as f:
                        f.write(file_bytes)
                    
                    status_text.info("Extracting text...")
                    progress_bar.progress(30)
                    _ing.ingest_all()
                    
                    status_text.info("Embedding chunks...")
                    def update_progress(batch, total):
                        pct = 30 + int((batch / total) * 70)
                        progress_bar.progress(min(pct, 100))
                        status_text.info(f"Embedding... ({batch}/{total})")

                    _es.build_store(reset=True, progress_callback=update_progress)
                    
                    save_hash(file_hash, uploaded_file.name)
                    progress_bar.progress(100)
                    status_text.success("✅ Success!")
                    time.sleep(2)
                    st.rerun() 
                except Exception as e:
                    status_text.error(f"❌ Error: {e}")

    st.divider()
    st.warning(DISCLAIMER)
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ---------------- Main UI ----------------
st.title("Doctor Assistant")
st.caption("Ask a clinical question. Answers are grounded strictly in the indexed textbooks.")

# --- NEW: Suggested Prompts on Empty Screen ---
if len(st.session_state.messages) == 0:
    st.markdown("### Suggested Clinical Queries")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Summarize the cardiac cycle"):
            st.session_state.pending_prompt = "Summarize the cardiac cycle."
    with col2:
        if st.button("Four primary tissue types?"):
            st.session_state.pending_prompt = "What are the four primary tissue types in the human body?"
    with col3:
        if st.button("Sliding filament theory"):
            st.session_state.pending_prompt = "Describe the sliding filament theory of muscle contraction."

# --- Render Chat History ---
for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])
        if m.get("sources"):
            with st.expander("📖 Sources", expanded=False):
                for s in m["sources"]:
                    st.markdown(f"- `{s['source']}` — page **{s['page']}**")
        if m["role"] == "assistant" and m.get("disclaimer"):
            st.caption(m["disclaimer"])
            # --- NEW: Export Button ---
            st.download_button(
                label="📥 Export Answer",
                data=m["content"],
                file_name="clinical_summary.txt",
                mime="text/plain",
                key=f"dl_{hash(m['content'])}"
            )

# --- Handle Inputs ---
prompt = st.chat_input("E.g. What is the function of the mitochondria?")
if st.session_state.pending_prompt:
    prompt = st.session_state.pending_prompt
    st.session_state.pending_prompt = None

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        streamer = AnswerStreamer(prompt)
        try:
            full_text = st.write_stream(streamer.stream())
        except Exception as e:
            st.error(f"RAG error: {e}")
            st.stop()

        with st.expander("📖 Sources", expanded=True):
            if streamer.sources:
                for s in streamer.sources:
                    st.markdown(f"- `{s['source']}` — page **{s['page']}**")
            else:
                st.markdown("_No sources retrieved._")
        st.caption(streamer.disclaimer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": full_text,
        "sources": streamer.sources,
        "disclaimer": streamer.disclaimer,
    })
    st.rerun() # Forces the export button to render immediately