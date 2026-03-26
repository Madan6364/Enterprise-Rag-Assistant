from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Enterprise RAG Assistant")


# Request Schema
class Query(BaseModel):
    question: str


# API Endpoint
@app.post("/chat")
async def chat(query: Query):

    from langchain_community.vectorstores import Chroma
    from langchain_community.llms import Ollama
    from langchain.chains import RetrievalQA
    from langchain_community.embeddings import HuggingFaceEmbeddings

    # Load Embeddings
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Load Vector DB
    vectordb = Chroma(
        persist_directory="vectordb",
        embedding_function=embeddings
    )

    retriever = vectordb.as_retriever(search_kwargs={"k": 3})

    # Load LLM
    llm = Ollama(model="mistral")

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )

    result = qa.invoke({"query": query.question})

    clean_answer = result["result"].replace("\n", " ")

    return {
        "question": query.question,
        "answer": clean_answer
    }
