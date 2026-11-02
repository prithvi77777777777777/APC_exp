# 🩺 Medicare Assistant - Local RAG Edition

A fully offline, privacy-first AI clinical assistant designed specifically for medical students and trainee doctors. 

Unlike standard chatbots that rely on external cloud APIs, this system utilizes a **Local Retrieval-Augmented Generation (RAG)** architecture. Users can upload standard medical textbooks (PDFs) directly into the application, and the AI will answer clinical questions strictly based on the provided literature, complete with page citations and a safety disclaimer.

## ✨ Key Features

- **100% Offline & Private:** Runs entirely on your local machine using Ollama. No patient data or queries ever leave your computer.
- **Apple visionOS / Liquid Glass UI:** A highly polished, glassmorphism web interface built with Streamlit and custom CSS, featuring deep mesh gradients and frosted glass panels.
- **Dynamic PDF Ingestion:** Drag and drop medical textbooks directly into the UI. The system automatically parses, chunks, and embeds them with a real-time progress bar.
- **Duplicate Prevention:** Uses SHA-256 file hashing to ensure you do not waste CPU/GPU power re-indexing books you already uploaded.
- **Verifiable Citations:** Every answer includes the exact textbook name and page number, eliminating AI hallucinations.
- **Real-time Streaming:** Answers are generated token-by-token for a fast, fluid reading experience.
- **Export to Text:** Save the AI clinical summaries to your local drive with one click.

---

## ⚙️ Step-by-Step Setup Guide

Follow these instructions to run the project on your local machine.

### Step 1: Install Prerequisites
1. **Python 3.11** is required (Do not use 3.12+ or 3.14, as PyTorch dependencies will break). [Download Python 3.11](https://www.python.org/downloads/release/python-3119/).
2. **Ollama** is required to run the local AI model. [Download Ollama](https://ollama.com/).
3. Open a terminal (PowerShell) and pull the required model:
   ```bash
   ollama pull llama3.1:8b

   .\.venv\Scripts\Activate.ps1