import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(override=True)  # Ensure .env variables override existing environment variables
client = OpenAI()

# Read the input log file
try:
    with open("log.txt", "r") as file:
        raw_logs = file.read()
except FileNotFoundError:
    print("Error: log.txt file not found. Please ensure the file exists in the current directory.")
    exit(1)

system_prompt = (
    "You are a backend parser.   Convert raw longs into a valid JSON array of objects.  Each object must have: 'time', 'level' (INFO/WARN/CRITICAL), and 'msg'."
    "Ouput ONLY raw valid JSON text.  Do not include markdown code block formatting(like ```json)."
) 

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": raw_logs}
    ],
    temperature=0.0,
    timeout=10.0
)

raw_json_output = response.choices[0].message.content.strip()

# Validate and pretty-print the JSON output
try:
    json_data = json.loads(raw_json_output)
    pretty_json = json.dumps(json_data, indent=4)
    print(pretty_json)
except json.JSONDecodeError:
    print("Error: The output from the model is not valid JSON. Please check the raw output:")
    print(raw_json_output)
