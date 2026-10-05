import os
from dotenv import load_dotenv
from mistralai.client import Mistral

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")

print("API key loaded:", api_key is not None)
print("API key length:", len(api_key) if api_key else 0)

client = Mistral(api_key=api_key)

response = client.chat.complete(
    model="mistral-medium-latest",
    messages=[
        {
            "role": "user",
            "content": "Say hello in one sentence."
        }
    ],
)

print(response.choices[0].message.content)