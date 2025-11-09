# utils/citation_generator.py
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def generate_citation(text, style="APA"):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Generate a {style} citation for this paper:\n{text}"}],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()
