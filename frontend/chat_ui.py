import streamlit as st
import requests

st.title("Enterprise RAG Assistant")

question = st.text_input("Ask a question about the document:")

if st.button("Ask"):
    if question:
        response = requests.post(
            "http://localhost:8000/chat",
            json={"question": question}
        )

        if response.status_code == 200:
            data = response.json()
            st.write("Answer:", data["answer"])
        else:
            st.write("Error from API")