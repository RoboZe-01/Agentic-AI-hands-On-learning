from dotenv import load_dotenv

load_dotenv()
from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model = "mistral-medium-latest",temperature=0.9)

input = "what is full form of ML ?"
response = model.invoke(input)
print(response.content)