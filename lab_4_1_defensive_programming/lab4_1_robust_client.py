import os
from dotenv import load_dotenv
import openai #importing the entire module to handle exceptions
from openai import OpenAI

load_dotenv(override=True)  # Ensure .env variables override existing environment variables
client = OpenAI()

def safe_api_call(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5,
            timeout=10.0,  # force a timeout if the network is hanging
        )
        return response.choices[0].message.content.strip()
    except openai.AuthenticationError:
        return "Error: Invalid API key. Please check your .env file."
    except openai.RateLimitError:
        return "Error: High traffic volume or hit monthly usage limits.  Retry later."
    except openai.APIConnectionError:
        return "Error: Network connection issue. Please check your internet and try again."
    except openai.OpenAIError as e:
        return f"An unexpected error occurred: {str(e)}"
    

#Test the wrapper
print(safe_api_call("Give me a one-word synonym for 'resilient'."))

          