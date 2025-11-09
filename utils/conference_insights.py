# utils/conference_insights.py
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def summarize_conference(transcript):
    prompt = (
        "Analyze this conference transcript and extract:\n"
        "- Key human insights\n"
        "- Network context\n"
        "- Trend understanding\n"
        "- Relevance to the research paper\n\n"
        f"{transcript}"
    )
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.6
    )
    return response.choices[0].message.content.strip()
