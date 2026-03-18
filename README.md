### Enterprise RAG Assistant

Enterprise Retrieval Augmented Generation (RAG) Assistant that answers
questions from company documents using LLMs.

#### Tech Stack

- FastAPI
- Streamlit
- LangChain
- Ollama
- Docker
- ChromaDB

#### Architecture

User → Streamlit UI → FastAPI API → LangChain → Vector DB → LLM → Response

#### Features

- Document based question answering
- Local LLM using Ollama
- Vector search with embeddings
- API based architecture
- Docker support

#### Run Locally

git clone https://github.com/Madan6364/enterprise-rag-assistant.git

cd enterprise-rag-assistant

pip install -r requirements.txt

uvicorn app.main:app --reload

streamlit run frontend/app.py

#### Example Question

What is the leave policy?

#### Output

Employees get:
- 12 Casual Leaves
- 10 Sick Leaves
- 15 Paid Vacation Leaves

Run ingestion:

python app/ingest.py

Start API:

python -m uvicorn app.api:app --reload
