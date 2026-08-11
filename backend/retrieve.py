# backend/retrieve.py
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent))

try:
    from .retriever import Retriever
except ImportError:
    from retriever import Retriever

if __name__ == "__main__":
    r = Retriever()
    q = "how to reset a Windows password?"
    print(r.search(q, k=5))

