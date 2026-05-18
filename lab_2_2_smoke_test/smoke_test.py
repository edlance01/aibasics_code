import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI()

try:
    response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Say hello world in three different languages."}
    ]
)

    # Task 1: Print the generated text response
    print("--- AI Response ---")
    print(response.choices[0].message.content)
    print("-------------------")
    
    # Task 2: Extract and print token usage details
    print(f"Prompt Tokens: {response.usage.prompt_tokens}")
    print(f"Completion Tokens: {response.usage.completion_tokens}")
    print(f"Total Tokens Used: {response.usage.total_tokens}")

except Exception as e:
    print(f"An error occurred: {e}")
