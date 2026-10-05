import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

print("API key loaded:", api_key is not None)
print("Prefix:", api_key[:3] if api_key else None)
print("Length:", len(api_key) if api_key else 0)

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say hello in one sentence."
)

print(response.text)