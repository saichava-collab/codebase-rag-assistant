import streamlit as st
from helper import ask_backend

st.set_page_config(page_title="Codebase Q&A Assistant", layout="wide")

st.title("🧠 Codebase Q&A Assistant (RAG)")

query = st.text_input("Ask a question about your codebase:")

if st.button("Submit"):
    if query.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Searching..."):
            answer = ask_backend(query)
        st.text_area("Answer:", value=answer, height=400)

