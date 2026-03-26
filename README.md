### Enterprise RAG Assistant

An end-to-end Retrieval-Augmented Generation (RAG) application built using FastAPI, LangChain, ChromaDB, and HuggingFace models.
This project allows users to ask questions and receive intelligent answers generated using a local knowledge base.

#### Project Overview

This project demonstrates how modern AI systems combine vector databases + large language models to build intelligent assistants.

Instead of giving generic answers, the assistant:

Searches relevant documents from a vector database (ChromaDB)
Retrieves the most relevant context
Sends the context to a language model (FLAN-T5)
Generates a meaningful answer based on the retrieved knowledge

#### Tech Stack
Python
FastAPI
LangChain
ChromaDB (Vector Database)
HuggingFace Transformers
Sentence-Transformers (Embeddings)
Uvicorn

#### Project Structure
enterprise-rag-assistant/
│
├── app/
│   ├── main.py
│   ├── rag_pipeline.py
│   ├── api.py
│   └── config.py
│
├── insert_docs.py
├── requirements.txt
└── README.md

#### How It Works

Step 1: User sends a question using the /ask API
Step 2: The question is converted into embeddings
Step 3: ChromaDB retrieves the most relevant documents
Step 4: The retrieved context is passed to the LLM
Step 5: The system generates an AI-powered answer

#### How to Run the Project
1. Clone the repository
git clone https://github.com/Madan6364/enterprise-rag-assistant.git
cd enterprise-rag-assistant
2. Install dependencies
pip install -r requirements.txt
3. Insert sample documents
python insert_docs.py
4. Run the API
python -m uvicorn app.main:app --reload
5. Open Swagger UI
http://127.0.0.1:8000/docs

Now you can test the /ask endpoint.

Example Query
{
  "query": "What is the role of AI in the IT industry?"
}

#### Key Features
1. End-to-end RAG pipeline
2. Local vector database using ChromaDB
3. Local language model using HuggingFace
4. FastAPI backend with Swagger UI
5. Clean and modular project structure
6. Ready for real-world knowledge-based applications

python app/ingest.py

Start API:

python -m uvicorn app.api:app --reload
