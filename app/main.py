from fastapi import FastAPI
from pydantic import BaseModel
from app.rag_pipeline import init_db, simple_rag

app = FastAPI()

# Initialize DB once when server starts
db = init_db()


# Request schema
class QueryRequest(BaseModel):
    query: str


# Test route
@app.get("/")
def home():
    return {"message": "RAG API is running!"}


# Ask AI route
@app.post("/ask")
def ask_ai(request: QueryRequest):
    answer = simple_rag(db, request.query)
    return {"answer": answer}