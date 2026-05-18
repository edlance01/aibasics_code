import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

def analyze_review(review_text):
    system_instruction = (
        "You are an AI data analyst.  For any text provided, output exactly in this format:\n"
        "SENTIMENT: [Positive/Negative/Neutral]\n"
        "CATEGORY: [Tech Support/Billing/Shipping/Product Quality]"
        "SUMMARY: [One sentence summarizing the issue]"
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": review_text}
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content.strip()

# Test customer review
sample_review = (
    "I ordered the wireless headphones last Tuesday. They arrived two days late, and when "
    "I opened the box, the left earbud wouldn't charge at all. I tried calling customer service "
    "but was kept on hold for 40 minutes before hanging up. Extremely disappointed."
)

analysis = analyze_review(sample_review);
print(analysis)
