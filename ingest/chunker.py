import re

# -----------------------------------------------------
# OPTIMIZED SEMANTIC CHUNKER
# -----------------------------------------------------
def chunk_text(
    text: str,
    min_chunk_size: int = 300,
    max_chunk_size: int = 800,
    overlap: int = 120
):
    """
    Smart chunker:
    - splits by paragraphs
    - merges small paragraphs
    - prevents giant chunks
    - adds overlap for smoother context
    """

    # -----------------------------------------------------
    # 1. CLEAN RAW TEXT
    # -----------------------------------------------------
    text = text.replace("\t", " ")
    text = re.sub(r"\n{3,}", "\n\n", text)  # remove huge gaps
    text = text.strip()

    # Split paragraphs
    raw_parts = [p.strip() for p in text.split("\n\n") if p.strip()]

    cleaned_parts = []
    for p in raw_parts:
        # remove extra spaces
        p = re.sub(r"\s+", " ", p).strip()
        if len(p) > 30:  # ignore extremely small paragraphs
            cleaned_parts.append(p)

    # -----------------------------------------------------
    # 2. MERGE PARAGRAPHS INTO CHUNKS
    # -----------------------------------------------------
    chunks = []
    buffer = ""

    for part in cleaned_parts:
        if len(buffer) + len(part) < max_chunk_size:
            buffer += part + " "
        else:
            chunks.append(buffer.strip())
            buffer = part + " "

    if buffer.strip():
        chunks.append(buffer.strip())

    # -----------------------------------------------------
    # 3. ENFORCE MINIMUM CHUNK SIZE
    # (merge tiny chunks into previous)
    # -----------------------------------------------------
    final_chunks = []
    for c in chunks:
        if final_chunks and len(c) < min_chunk_size:
            final_chunks[-1] += " " + c
        else:
            final_chunks.append(c)

    # -----------------------------------------------------
    # 4. ADD SLIDING WINDOW OVERLAP
    # -----------------------------------------------------
    overlapped = []
    for c in final_chunks:
        if len(c) <= max_chunk_size:
            overlapped.append(c)
        else:
            # break giant chunk using sliding window
            words = c.split()
            start = 0
            step = max_chunk_size - overlap

            while start < len(words):
                window = " ".join(words[start:start + max_chunk_size])
                overlapped.append(window)
                start += step

    return overlapped
