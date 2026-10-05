
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

print("API key loaded:", api_key is not None)
print("Prefix:", api_key[:3] if api_key else None)
print("Length:", len(api_key) if api_key else 0)

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=api_key
)

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = llm.invoke(user_input)

    print("AI:", response.content)
