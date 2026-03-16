import os

from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings


DATA_PATH = "data/company_docs"


def ingest_docs():

    documents = []

    for file in os.listdir(DATA_PATH):
        if file.endswith(".txt"):
            loader = TextLoader(f"{DATA_PATH}/{file}")
            documents.extend(loader.load())

    print("Documents Loaded:", len(documents))

    # ✅ SMART CHUNKING
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = splitter.split_documents(documents)

    print("Chunks Created:", len(chunks))

    # ✅ LOCAL EMBEDDINGS (NO OPENAI)
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="vectordb"
    )

    vectordb.persist()

    print("✅ Vector DB Created Successfully")


if __name__ == "__main__":
    ingest_docs()