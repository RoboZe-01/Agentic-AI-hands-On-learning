
# import required dependencies
import os
from dotenv import load_dotenv

# Langchain
from langchain_mistralai import ChatMistralAI


# Load the .env 
load_dotenv()

# Load the LLM model 
model = ChatMistralAI(model="mistral-small-2603")
result = model.invoke("Hello")
print(result.content)