from langchain_community.vectorstores import Chroma
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain_community.embeddings import HuggingFaceEmbeddings


def chat():

    print("✅ Starting Enterprise RAG Assistant...")

    # Embeddings
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
    llm = Ollama(model="llama3")

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever
    )

    print("\n🔥 RAG Chat Ready")
    print("Type 'exit' to quit\n")

    while True:
        query = input("Ask Question: ")

        if query.lower() == "exit":
            break

        response = qa.invoke({"query": query})

        print("\nAI Answer:\n", response["result"])
        print("-" * 50)


if __name__ == "__main__":
    chat()