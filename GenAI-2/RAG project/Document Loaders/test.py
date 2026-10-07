from langchain_community.document_loaders import TextLoader


data = TextLoader(r'D:\Robotics\Agentic AI hands On learning\GenAI-2\RAG project\data\notes.txt')
docs = data.load()
print(docs[0].page_content)