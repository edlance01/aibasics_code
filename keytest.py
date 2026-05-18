import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)  # Ensure .env variables override existing environment variables

# DEBUG: Print the first 4 characters of the key Python is actually using
current_key = os.environ.get("OPENAI_API_KEY", "")
if current_key:
    #print(f"DEBUG: Using key ending in: ...{current_key[4:]}")
    print(f"DEBUG: Using key starting with: {current_key[:4]}...")  # Show the first 4 characters for debugging
else:
    print("DEBUG: No API key found at all!")

client = OpenAI()
