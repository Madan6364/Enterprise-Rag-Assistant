# Enterprise RAG Assistant

Enterprise-grade Retrieval Augmented Generation system built using:

- FastAPI
- LangChain
- ChromaDB
- Ollama (Llama3)
- Local Vector Database

## Features
- Document Question Answering
- Enterprise Knowledge Search
- Local LLM Inference
- REST API
- Swagger UI

## Run Project

Install dependencies:

pip install -r requirements.txt

Run ingestion:

python app/ingest.py

Start API:

python -m uvicorn app.api:app --reload