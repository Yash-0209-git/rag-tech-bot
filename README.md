# 🤖 RAG-Tech Bot

A high-performance **Retrieval-Augmented Generation (RAG)** technical support assistant built with **FastAPI**, **FAISS**, **Sentence Transformers**, **Cross-Encoder Reranking**, and **Groq Llama-3.3-70B API**, paired with an interactive **React + Three.js** modern Web UI.

---

## ✨ Features

- 🔍 **Semantic Search**: Powered by FAISS vector index (`distiluse-base-multilingual-cased-v2`, 512 dimensions).
- ⚡ **Groq LLM Acceleration**: Fast response generation using Groq's `llama-3.3-70b-versatile` API.
- 🎯 **Cross-Encoder Reranking**: Re-ranks top context documents using `cross-encoder/ms-marco-MiniLM-L-6-v2`.
- 🚀 **Query Expansion**: Automatically expands short queries into comprehensive technical questions.
- 🛡️ **Context Booster**: Category-aware Context Boosting (Windows, Linux, Networking, Active Directory, Hardware, Devices).
- 💬 **Conversational Memory**: Maintains multi-turn context throughout chat sessions.
- 🎤 **Voice Input & 🔊 Text-to-Speech**: Web Speech API integration for voice command input and audio response playback.
- 🌌 **Futuristic Web Interface**: Responsive React UI featuring glassmorphism design and an interactive 3D Three.js visual avatar.

---

## 🛠️ Architecture & Workflow

```text
               ┌───────────────────────┐
               │      User Query       │
               └───────────┬───────────┘
                           │
                           ▼
               ┌───────────────────────┐
               │    Query Expansion    │
               └───────────┬───────────┘
                           │
                           ▼
               ┌───────────────────────┐
               │ Semantic Retrieval    │
               │   (FAISS Vector DB)   │
               └───────────┬───────────┘
                           │
                           ▼
               ┌───────────────────────┐
               │ Cross-Encoder Rerank  │
               └───────────┬───────────┘
                           │
                           ▼
               ┌───────────────────────┐
               │   Context Booster     │
               └───────────┬───────────┘
                           │
                           ▼
               ┌───────────────────────┐
               │ Prompt Construction & │
               │ Conversational Memory │
               └───────────┬───────────┘
                           │
                           ▼
               ┌───────────────────────┐
               │  Groq LLM Generation  │
               │ (Llama 3.3-70B Engine)│
               └───────────┬───────────┘
                           │
                           ▼
               ┌───────────────────────┐
               │   Structured Answer   │
               └───────────────────────┘
```

---

## 📂 Project Structure

```text
rag-tech-bot/
├── backend/
│   ├── app.py                # FastAPI application endpoints
│   ├── rag_pipeline.py       # Full RAG execution pipeline
│   ├── retriever.py          # Vector search retriever
│   ├── reranker.py           # Cross-encoder document reranker
│   ├── generator.py          # Groq LLM answer generator
│   ├── context_booster.py    # Category-based domain context booster
│   ├── query_expander.py     # LLM query expansion module
│   ├── translator.py         # Multi-language translation utility
│   ├── retrieve.py           # Standalone retrieval interface
│   └── requirements.txt      # Python dependencies
├── docs/                     # Technical documentation knowledge base
├── ingest/
│   ├── chunker.py            # Optimized semantic text chunker
│   └── ingest_and_index.py   # Document loading & FAISS index builder
├── vectors/
│   ├── faiss.index           # Generated FAISS vector index
│   └── meta.pkl              # Metadata pickle file
├── rag-tech-frontend/        # React + Vite + Three.js web application
├── .env.example              # Sample environment variables configuration
├── start_backend.py          # FastAPI backend server launcher script
└── README.md
```

---

## 🚀 Quick Start Guide

### 1. Clone Repository

```bash
git clone https://github.com/Yash-0209-git/rag-tech-bot.git
cd rag-tech-bot
```

### 2. Environment Setup

Copy `.env.example` to `.env` in the root directory and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
MODEL_NAME=llama-3.3-70b-versatile
```

### 3. Backend Setup

Initialize virtual environment and install dependencies:

**Windows**:
```powershell
python -m venv venv
.\venv\Scripts\activate
pip install -r backend/requirements.txt
```

**Linux / macOS**:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt
```

### 4. Build Document Index

To process knowledge base files in `docs/` and build/update the vector index:

```bash
python ingest/ingest_and_index.py
```

### 5. Launch Backend Server

Run the backend FastAPI server (runs on `http://127.0.0.1:8000`):

```bash
python start_backend.py
```

### 6. Launch Frontend Interface

Open another terminal and start the Vite dev server (runs on `http://localhost:5173`):

```bash
cd rag-tech-frontend
npm install
npm run dev
```

---

## 💬 Example Technical Queries

- *"How to reset a Windows user password?"*
- *"How to troubleshoot DNS resolution issues on Linux?"*
- *"What are common Active Directory Group Policy troubleshooting steps?"*
- *"How to check open network ports and active connections?"*

---

## 🛠️ Tech Stack Summary

- **Core Engine**: Python 3.12, FastAPI, PyTorch, Hugging Face Transformers
- **Vector Search**: FAISS, Sentence-Transformers (`distiluse-base-multilingual-cased-v2`)
- **Reranker**: Cross-Encoder (`ms-marco-MiniLM-L-6-v2`)
- **LLM Provider**: Groq API (`llama-3.3-70b-versatile`, `llama-3.1-8b-instant`)
- **Frontend**: React 18, Vite, Three.js (`@react-three/fiber`), Tailwind CSS

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

**Yashwanth**  
GitHub: [@Yash-0209-git](https://github.com/Yash-0209-git)