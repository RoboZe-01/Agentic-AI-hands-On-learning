import os
from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model = "mistral-small-latest",temperature=0.7)

response = model.invoke("Explain machine learning in 5 simple words.")

print(response.content)