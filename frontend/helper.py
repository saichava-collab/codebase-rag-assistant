import requests

API_URL = "http://localhost:8000/ask"

def ask_backend(question: str) -> str:
    response = requests.post(API_URL, json={"question": question})
    response.raise_for_status()
    return response.json()["answer"]

