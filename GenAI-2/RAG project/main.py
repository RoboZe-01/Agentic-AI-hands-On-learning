
# import required dependencies
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader

# Langchain
from langchain_mistralai import ChatMistralAI    # Mistral model as LLM
from langchain_groq import ChatGroq              # Groq model as LLM
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate # Prompt template
from langchain_text_splitters import RecursiveCharacterTextSplitter


# Load the .env 
load_dotenv()

# Load the LLM model 
# model = ChatMistralAI(model="mistral-small-latest")
# model = ChatGoogleGenerativeAI(model = "gemini-3.5-flash-lite")
model = ChatGroq(model="openai/gpt-oss-20b")


# ---- Text data loading ----
data = TextLoader(r"D:\Robotics\Agentic AI hands On learning\GenAI-2\RAG project\data\notes.txt")
docs = data.load()


# ----- Chuncking ----- 

splitter = RecursiveCharacterTextSplitter(           # Initializing the splitter function 
    chunk_size = 1000 ,
    chunk_overlap = 200,
)

# Using splitter function to split/chunk the data 

chunks = splitter.split_documents(docs) 
# ----- Chat Template creations ----- 

template = ChatPromptTemplate.from_messages(
    [
        ("system","you are a AI tha summarizes text data"),
        ("human","{data}")

    ]
)

prompt = template.format_messages(data=docs[0].page_content)



# ---- LLM colling
result = model.invoke(prompt)
print(result.content)