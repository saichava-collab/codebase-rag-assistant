import os, glob, pickle
import numpy as np
import faiss

from sentence_transformers import SentenceTransformer
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import *


def load_code_files(path):
    """
    Recursively loads code files from the given directory.
    Supports multiple common programming language extensions.
    """
    exts = ["*.py", "*.js", "*.ts", "*.java", "*.cpp", "*.cc", "*.c", "*.cs"]
    files = []

    for e in exts:
        files.extend(glob.glob(os.path.join(path, "**", e), recursive=True))

    return files


def ingest():
    print("→ Loading code files...")
    files = load_code_files(DATA_PATH)

    if not files:
        print("❌ No code files found in data directory. Add files to ./data/")
        return

    chunks = []
    metadata = []

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=200
    )

    print(f"→ Found {len(files)} code files. Splitting into chunks...")

    for f in files:
        try:
            with open(f, "r", errors="ignore") as fp:
                text = fp.read()

            for chunk in splitter.split_text(text):
                chunks.append(chunk)
                metadata.append({"file": f})

        except Exception as e:
            print(f"⚠️ Skipping {f}: {e}")

    print(f"→ Total chunks created: {len(chunks)}")

    print("→ Loading embedding model...")
    model = SentenceTransformer(EMBED_MODEL)

    print("→ Creating embeddings...")
    embeddings = model.encode(chunks)

    print("→ Building FAISS index...")
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))

    print("→ Saving FAISS index and metadata...")
    faiss.write_index(index, INDEX_PATH)
    pickle.dump(
        {"meta": metadata, "chunks": chunks},
        open(META_PATH, "wb")
    )

    print("✔ SUCCESS! Vector database created.")
    print("✔ You can now run the RAG backend.")


if __name__ == "__main__":
    ingest()

