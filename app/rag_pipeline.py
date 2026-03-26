from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline


# Create embedding model
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)


# Create text generation pipeline
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-small",
    max_length=256
)


# Convert to LangChain LLM
llm = HuggingFacePipeline(pipeline=generator)


# Initialize ChromaDB
def init_db():
    db = Chroma(
        persist_directory="chroma_db",
        embedding_function=embedding
    )
    return db


# Simple RAG pipeline
def simple_rag(db, query: str):
    try:
        # Search documents
        docs = db.similarity_search(query, k=5)

        # If nothing found
        if not docs:
            return "No relevant documents found in the database."

        # Combine context
        context = " ".join([doc.page_content for doc in docs])

        # Prompt
        prompt = f"""
You are an AI assistant.

Use the context below to answer the question clearly in 3–5 lines.
Do not copy the same sentence from the context.
Explain in simple words.

Context:
{context}

Question:
{query}

Answer:
"""

        # Generate answer
        result = llm.invoke(prompt)

        return result

    except Exception as e:
        return f"Error inside RAG: {str(e)}"