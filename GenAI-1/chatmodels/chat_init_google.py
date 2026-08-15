# Importing env variables like api keys

from dotenv import load_dotenv

load_dotenv()

# Using llm using init_chat_model
from langchain.chat_models import init_chat_model

# Initializing the model
model = init_chat_model("google_genai:gemini-2.5-flash-lite")
response = model.invoke("Give 3 random words")

# Printing the response content
print(response.content)