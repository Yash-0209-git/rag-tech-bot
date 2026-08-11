from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent))

try:
    from .retriever import Retriever
    from .reranker import Reranker
    from .context_booster import ContextBooster
    from .generator import generate_answer
    from .query_expander import QueryExpander
except ImportError:
    from retriever import Retriever
    from reranker import Reranker
    from context_booster import ContextBooster
    from generator import generate_answer
    from query_expander import QueryExpander


retriever = Retriever()
reranker = Reranker()
booster = ContextBooster()
expander = QueryExpander()


def build_memory(history: list) -> str:
    """
    Convert previous chat messages into a readable conversation context.
    Only uses the last 6 messages for relevance.
    """
    if not history:
        return ""

    memory = ""

    for msg in history[-6:]:
        role = msg.get("role", "").lower()
        text = msg.get("text", "")

        if not text:
            continue

        if role == "user":
            memory += f"User: {text}\n"
        elif role == "assistant":
            memory += f"Assistant: {text}\n"

    return memory.strip()


def answer_query(query: str, history: list) -> str:
    """
    Full RAG pipeline:
    1. Use conversation memory
    2. Normalize & clean user query
    3. Expand weak queries
    4. Retrieve knowledge-base chunks
    5. Rerank them
    6. Apply context boosting
    7. Build combined prompt (memory + RAG + query)
    8. Generate answer
    """

    # -------------------------
    # 1. Build conversation memory
    # -------------------------
    memory_context = build_memory(history)

    # -------------------------
    # 2. Clean / normalize query
    # -------------------------
    eng_query = query.strip()

    # -------------------------
    # 3. Expand short queries
    # -------------------------
    if len(eng_query.split()) <= 3:
        eng_query = expander.expand(eng_query)

    # -------------------------
    # 4. Retrieve RAG documents
    # -------------------------
    docs = retriever.search(eng_query, k=15)

    # Weak retrieval? Retry with expanded query
    if len(docs) < 2:
        improved = expander.expand(eng_query)
        docs = retriever.search(improved, k=15)
        eng_query = improved

    # -------------------------
    # 5. Rerank retrieved docs
    # -------------------------
    docs = reranker.rerank(eng_query, docs)

    # -------------------------
    # 6. Boost context (Windows/Linux/Networking)
    # -------------------------
    docs = booster.boost(eng_query, docs)

    # -------------------------
    # 7. Build final RAG context
    # -------------------------
    if docs:
        kb_context = "\n\n".join(d["content"] for d in docs[:3])
    else:
        kb_context = "No relevant technical context found."

    # -------------------------
    # 8. Construct final prompt
    # -------------------------
    final_prompt = f"""
You are a highly accurate technical assistant.

Below is the conversation so far:
{memory_context}

Here is relevant knowledge from your database:
{kb_context}

User's current question:
{eng_query}

Give a clear, precise, step-by-step answer based ONLY on:
- the conversation history
- the knowledge base (context)
- common technical reasoning

Do NOT hallucinate anything outside the provided context.
"""

    # -------------------------
    # 9. Generate answer via LLM
    # -------------------------
    answer = generate_answer(final_prompt, kb_context)

    return answer
