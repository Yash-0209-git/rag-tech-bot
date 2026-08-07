# 🤖 RAG-Tech Bot

A Retrieval-Augmented Generation (RAG) chatbot capable of answering technical questions using a local knowledge base. The project combines semantic search, reranking, and Groq's LLM to generate accurate, context-aware responses through a modern React interface.

---

## ✨ Features

- 🔍 Semantic search using FAISS
- 🧠 Context-aware Retrieval-Augmented Generation (RAG)
- ⚡ Groq Llama 3.3-70B for fast response generation
- 📚 Supports custom technical knowledge bases
- 🎯 Context reranking for improved retrieval accuracy
- 🚀 Query expansion for better handling of short queries
- 💬 Conversational memory within a chat session
- 🎤 Voice input
- 🔊 Text-to-Speech (optional)
- 🌌 Modern React UI with Three.js avatar and glassmorphism design

---

## 🛠 Tech Stack

### Backend
- Python
- FastAPI
- FAISS
- Sentence Transformers
- Groq API
- Transformers
- PyTorch

### Frontend
- React
- Vite
- Three.js
- Tailwind CSS

---

# Project Structure

```
rag-tech-bot/
│
├── backend/
│   ├── app.py
│   ├── rag_pipeline.py
│   ├── retriever.py
│   ├── reranker.py
│   ├── generator.py
│   ├── context_booster.py
│   ├── query_expander.py
│   ├── translator.py
│   └── requirements.txt
│
├── docs/
│
├── ingest/
│
├── vectors/
│
├── rag-tech-frontend/
│
├── README.md
└── .gitignore
```

---

# Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/rag-tech-bot.git

cd rag-tech-bot
```

---

## 2. Backend Setup

Navigate to the backend directory.

```bash
cd backend
```

Create a virtual environment.

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

Install the required dependencies.

```bash
pip install -r requirements.txt
```

---

## 3. Create Environment Variables

Create a file named

```
.env
```

inside the backend folder.

Add your Groq API key.

```env
GROQ_API_KEY=your_groq_api_key_here
MODEL_NAME=llama-3.3-70b-versatile
```

---

## 4. Run the Backend

```bash
uvicorn app:app --reload
```

Backend runs on

```
http://127.0.0.1:8000
```

---

## 5. Frontend Setup

Open another terminal.

```bash
cd rag-tech-frontend

npm install

npm run dev
```

Frontend runs on

```
http://localhost:5173
```

---

# Building the Knowledge Base

Place your text documents inside the appropriate data folder used by the ingestion pipeline.

Then rebuild the vector database.

Example:

```bash
python ingest/build_index.py
```

*(Update the command according to your ingestion script.)*

---

# How It Works

```
User Query
     │
     ▼
Query Expansion
     │
     ▼
Semantic Retrieval (FAISS)
     │
     ▼
Reranking
     │
     ▼
Context Booster
     │
     ▼
Prompt Construction
     │
     ▼
Groq Llama 3.3
     │
     ▼
Final Response
```

---

# Example Queries

- What is DNS?
- How does TCP three-way handshake work?
- Difference between HTTP and HTTPS
- Explain operating system scheduling
- What causes slow WiFi?
- What is SQL Injection?
- Explain REST APIs
- What is Docker?

---

# Future Improvements

- User authentication
- Multi-user conversations
- Persistent long-term memory
- PDF upload from UI
- Streaming responses
- Source citation support
- Cloud deployment
- Admin dashboard for knowledge base management

---

# License

This project is released under the MIT License.

---

# Acknowledgements

- FastAPI
- React
- FAISS
- Hugging Face
- Groq
- Three.js

---

## Author

**Yashwanth**

If you found this project useful, consider giving it a ⭐ on GitHub.