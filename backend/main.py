from fastapi import FastAPI
from pydantic import BaseModel
from rag import RAG

app = FastAPI()
rag = RAG()  # initialize retrieval engine


class Query(BaseModel):
    question: str


@app.post("/ask")
def ask_api(payload: Query):
    answer = rag.answer(payload.question)
    return {"answer": answer}

