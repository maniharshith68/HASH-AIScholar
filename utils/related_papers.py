# Semantic vector search and generation.
# from sentence_transformers import SentenceTransformer
# from sklearn.metrics.pairwise import cosine_similarity
# from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# # Load embedding and generation models
# embedder = SentenceTransformer('all-mpnet-base-v2')
# tokenizer = AutoTokenizer.from_pretrained("t5-base")
# model = AutoModelForSeq2SeqLM.from_pretrained("t5-base")

# def suggest_related_papers_with_semantic_search(paper_text, corpus_texts, top_k=5):
#     # Encode input and corpus
#     query_vec = embedder.encode([paper_text])
#     corpus_vecs = embedder.encode(corpus_texts)

#     # Compute similarity scores
#     similarities = cosine_similarity(query_vec, corpus_vecs)[0]

#     # Find top K similar papers
#     top_indices = similarities.argsort()[-top_k:][::-1]
#     related_snippets = [corpus_texts[i] for i in top_indices]

#     # Aggregate related info for generator input
#     prompt = "Suggest related academic papers based on these abstracts:\n" + "\n".join(related_snippets)
#     inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=512)

#     # Generate suggestion output
#     outputs = model.generate(**inputs, max_length=150, num_beams=4)
#     suggestions = tokenizer.decode(outputs[0], skip_special_tokens=True)

#     return suggestions



# utils/related_papers.py
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def suggest_related_papers(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Suggest 5 related academic papers based on this:\n{text}"}],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()

