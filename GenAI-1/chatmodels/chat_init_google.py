from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import init_chat_model


init_chat_model(google_genai:model="gemini-2.5-flash-lite")