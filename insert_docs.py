
from app.rag_pipeline import init_db

db = init_db()

docs = [
    """Artificial Intelligence is transforming the IT sector in many ways. 
    It helps automate repetitive tasks such as testing, data entry, and customer support. 
    Because of this, developers can focus more on innovation and problem solving.""",

    """AI also helps professionals gain knowledge faster. 
    Tools like AI assistants, code generators, and smart search systems help developers learn new technologies quickly 
    and improve productivity in the workplace.""",

    """The biggest benefit of AI in the IT industry is increased efficiency. 
    Companies use AI for software development, data analysis, cybersecurity, and automation. 
    This creates new job opportunities such as AI engineers, data scientists, and machine learning specialists.""",

    """AI will not completely replace software engineers. 
    Instead, it will help them work faster by generating code, debugging programs, and improving software quality."""
]

db.add_texts(docs)

print("Better documents inserted successfully!")
print("Documents inserted successfully!")