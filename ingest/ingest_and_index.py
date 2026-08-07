# ingest/ingest_and_index.py
import os
import pickle
from sentence_transformers import SentenceTransformer
import faiss
from chunker import chunk_text

MODEL = "sentence-transformers/distiluse-base-multilingual-cased-v2"
EMB_DIM = 512

def load_documents(docs_dir="docs"):
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

    os.makedirs("vectors", exist_ok=True)

    faiss.write_index(index, "vectors/faiss.index")

    with open("vectors/meta.pkl", "wb") as f:
        pickle.dump(docs, f)

    print("Index built and saved successfully.")

if __name__ == "__main__":
    docs = load_documents("docs")
    build_index(docs)
