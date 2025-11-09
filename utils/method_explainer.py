# utils/method_explainer.py
import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def explain_methods(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Explain the methodology used in this research paper:\n{text}"}],
        temperature=0.5
    )
    return response.choices[0].message.content.strip()




# from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration

# def explain_methods_with_rag(text):
#     # Initialize tokenizer, retriever, and RAG model
#     tokenizer = RagTokenizer.from_pretrained("facebook/rag-sequence-base")
#     retriever = RagRetriever.from_pretrained("facebook/rag-sequence-base", index_name="exact", use_dummy_dataset=True)
#     rag_model = RagSequenceForGeneration.from_pretrained("facebook/rag-sequence-base", retriever=retriever)

#     # Prepare input text
#     input_dict = tokenizer([text], return_tensors="pt", truncation=True, max_length=512)

#     # Generate explanation output with beam search
#     output_ids = rag_model.generate(**input_dict, num_beams=3, max_length=150)
#     explanation = tokenizer.batch_decode(output_ids, skip_special_tokens=True)[0]

#     return explanation

# # Example usage
# paper_text = "Paste your research paper text here."
# print(explain_methods_with_rag(paper_text))
