# Codebase Q&A Assistant (RAG Project)

A Retrieval-Augmented Generation tool that lets you ask natural-language questions about a codebase and instantly retrieve relevant code snippets.

This project includes:
- Python backend
- FastAPI API server
- FAISS vector store for embeddings
- SentenceTransformers for embeddings
- LangChain text splitters
- Streamlit frontend UI

## Project Structure
```
codebase-rag-assistant/
│
├── backend/
│   ├── ingest.py
│   ├── rag.py
│   ├── main.py
│   ├── config.py
│   ├── requirements.txt
│   ├── data/
│   │     └── (your code files go here)
│   ├── faiss.index (auto-created)
│   ├── metadata.pkl (auto-created)
│   └── venv/ (virtual environment)
│
└── frontend/
    ├── app.py
    ├── helper.py
    └── requirements.txt
```

## Setup Instructions

### 1. Install Python 3.10 or above
```
python3 --version
```

### 2. Setup Backend Environment
```
cd codebase-rag-assistant/backend
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Backend Dependencies
```
pip install -r requirements.txt
```

### 4. Add Code Files for Ingestion
Place files inside:
```
backend/data/
```

### 5. Run Ingestion Script
```
python ingest.py
```

### 6. Run Backend Server
```
uvicorn main:app --reload --port 8000
```

### 7. Run Frontend UI
Open new terminal:
```
cd codebase-rag-assistant/frontend
source ../backend/venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Access UI at:
```
http://localhost:8501
```

### 8. Ask Questions
Example:
```
Where is the add function defined?
```
