# utils/summarizer.py
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def summarize_text(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Summarize this research paper:\n{text}"}],
        temperature=0.5
    )
    return response.choices[0].message.content.strip()


# from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration

# def summarize_with_rag(text):
#     # Initialize models and tokenizer
#     tokenizer = RagTokenizer.from_pretrained("facebook/rag-sequence-base")
#     retriever = RagRetriever.from_pretrained("facebook/rag-sequence-base", index_name="exact", use_dummy_dataset=True)
#     rag_model = RagSequenceForGeneration.from_pretrained("facebook/rag-sequence-base", retriever=retriever)

#     # Encode input
#     inputs = tokenizer([text], return_tensors="pt", truncation=True, max_length=512)

#     # Generate summary
#     summary_ids = rag_model.generate(**inputs, num_beams=3, max_length=100)
#     summary = tokenizer.batch_decode(summary_ids, skip_special_tokens=True)[0]

#     return summary

# # Usage
# paper = "Paste your research paper text here."
# print(summarize_with_rag(paper))
