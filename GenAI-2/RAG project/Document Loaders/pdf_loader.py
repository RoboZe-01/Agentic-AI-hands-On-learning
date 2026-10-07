from langchain_community.document_loaders import PyPDFLoader

data = PyPDFLoader(r"D:\Robotics\Agentic AI hands On learning\GenAI-2\RAG project\data\GRU.pdf")
docs= data.load()
print(docs)