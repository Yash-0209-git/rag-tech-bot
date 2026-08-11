# ingest/ingest_and_index.py
import os
import pickle
import sys
from pathlib import Path
from sentence_transformers import SentenceTransformer
import faiss

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(Path(__file__).resolve().parent))
sys.path.append(str(BASE_DIR))

try:
    from chunker import chunk_text
except ImportError:
    from ingest.chunker import chunk_text

MODEL = "sentence-transformers/distiluse-base-multilingual-cased-v2"
EMB_DIM = 512

def load_documents(docs_dir=None):
    if docs_dir is None:
        docs_dir = str(BASE_DIR / "docs")
    docs = []
    for root, _, files in os.walk(docs_dir):
        for file in files:
            if file.endswith(".txt"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    text = f.read()
                chunks = chunk_text(text)
                for c in chunks:
                    docs.append({"content": c, "source": path})
    return docs

def build_index(docs):
    model = SentenceTransformer(MODEL)
    texts = [d["content"] for d in docs]

    print("Number of docs:", len(docs))
    print("Number of texts:", len(texts))

    embeddings = model.encode(texts, convert_to_numpy=True, show_progress_bar=True)

    print("Embeddings shape:", embeddings.shape)

    # -------------------------
    # FAISS INDEX BUILDING
    # -------------------------
    dim = EMB_DIM
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)

    vectors_dir = BASE_DIR / "vectors"
    os.makedirs(vectors_dir, exist_ok=True)

    faiss_path = str(vectors_dir / "faiss.index")
    meta_path = str(vectors_dir / "meta.pkl")

    faiss.write_index(index, faiss_path)

    with open(meta_path, "wb") as f:
        pickle.dump(docs, f)

    print(f"Index built and saved successfully to {faiss_path} and {meta_path}.")

if __name__ == "__main__":
    docs = load_documents()
    build_index(docs)

