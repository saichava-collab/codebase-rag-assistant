import pickle
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from config import *


class RAG:
    def __init__(self):
        print("→ Loading FAISS index...")
        self.index = faiss.read_index(INDEX_PATH)

        print("→ Loading metadata...")
        data = pickle.load(open(META_PATH, "rb"))
        self.metadata = data["meta"]
        self.chunks = data["chunks"]

        print("→ Loading embedding model...")
        self.embedder = SentenceTransformer(EMBED_MODEL)

        print("✔ RAG engine initialized.")

    def search(self, query, k=3):
        """
        Returns the top-k relevant code chunks from the vector DB.
        """
        q_emb = self.embedder.encode([query])
        distances, idxs = self.index.search(np.array(q_emb), k)

        results = []
        for dist, idx in zip(distances[0], idxs[0]):
            results.append(
                {
                    "file": self.metadata[idx]["file"],
                    "score": float(dist),
                    "chunk": self.chunks[idx],
                }
            )
        return results

    def answer(self, query):
        """
        Returns a human-readable answer containing relevant code snippets.
        """
        hits = self.search(query)

        response = "Relevant code snippets:\n\n"
        for h in hits:
            response += f"📄 File: {h['file']}\n"
            response += f"----------------------------------------\n"
            response += h["chunk"] + "\n\n"

        return response
