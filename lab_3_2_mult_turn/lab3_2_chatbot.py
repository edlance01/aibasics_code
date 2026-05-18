import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

# Initialize history with a system role defining behavior
chat_history = [
    {
        "role": "system",
        "content": "You are a witty, concise Python mentor. Keep answers under 3 sentences.",
    }
]

print("Mentor AI active.  Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("Mentor AI signing off. Goodbye!")
        break

    # Append user message to history
    chat_history.append({"role": "user", "content": user_input})

    # Get AI response
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=chat_history,
        temperature=0.5,
    )

    ai_response = response.choices[0].message.content.strip()
    print(f"Mentor AI: {ai_response}\n")

    # Append AI response to history
    chat_history.append({"role": "assistant", "content": ai_response})
    