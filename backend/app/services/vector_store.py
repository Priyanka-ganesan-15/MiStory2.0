import faiss
import numpy as np
from typing import List, Dict

from app.services.embeddings import get_embedding

DIM = 384

index = faiss.IndexFlatL2(DIM)

# enriched memory store
memory_store: List[Dict] = []


def add_entry(entry_id: int, text: str):
    vector = np.array(get_embedding(text)).astype("float32").reshape(1, -1)

    index.add(vector)

    memory_store.append({
        "id": entry_id,
        "text": text
    })


def search(query: str, k: int = 5):
    if len(memory_store) == 0:
        return []

    query_vec = np.array(get_embedding(query)).astype("float32").reshape(1, -1)

    distances, indices = index.search(query_vec, k)

    results = []

    for i in indices[0]:
        if i < len(memory_store):
            results.append(memory_store[i])

    return results