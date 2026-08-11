from pathlib import Path
import sys
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

load_dotenv()

sys.path.append(str(Path(__file__).resolve().parent))

try:
    from .rag_pipeline import answer_query
except ImportError:
    from rag_pipeline import answer_query

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    question: str
    history: list= []

@app.get("/")
def root():
    return {"status": "Backend is running"}

@app.post("/ask")
def ask(q: Query):
    answer = answer_query(q.question,q.history)
    return {"answer": answer}
