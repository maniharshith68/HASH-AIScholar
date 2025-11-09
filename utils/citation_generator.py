# # utils/citation_generator.py

# import os
# import requests
# from openai import OpenAI
# from typing import Dict, Optional

# # Initialize OpenAI client
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# # ---------- Metadata Fetching Utilities ---------- #

# def fetch_metadata_from_crossref(query: str) -> Optional[Dict]:
#     """
#     Try to fetch paper metadata (title, authors, year, DOI, etc.) using CrossRef API.
#     The query can be a DOI, title, or part of an abstract.
#     """
#     base_url = "https://api.crossref.org/works"
#     params = {"query": query, "rows": 1}
#     try:
#         response = requests.get(base_url, params=params, timeout=10)
#         response.raise_for_status()
#         items = response.json().get("message", {}).get("items", [])
#         if not items:
#             return None
#         item = items[0]
#         authors = [
#             f"{a.get('given', '')} {a.get('family', '')}".strip()
#             for a in item.get("author", [])
#         ]
#         metadata = {
#             "title": item.get("title", [""])[0],
#             "authors": authors,
#             "year": item.get("issued", {}).get("date-parts", [[None]])[0][0],
#             "doi": item.get("DOI"),
#             "journal": item.get("container-title", [""])[0],
#             "publisher": item.get("publisher", ""),
#             "url": item.get("URL", ""),
#         }
#         return metadata
#     except Exception as e:
#         print(f"⚠️ Error fetching metadata from CrossRef: {e}")
#         return None


# def fetch_metadata_from_semantic_scholar(query: str) -> Optional[Dict]:
#     """
#     Fallback to Semantic Scholar API if CrossRef fails.
#     """
#     base_url = "https://api.semanticscholar.org/graph/v1/paper/search"
#     params = {"query": query, "limit": 1, "fields": "title,authors,year,doi,url,venue"}
#     try:
#         response = requests.get(base_url, params=params, timeout=10)
#         response.raise_for_status()
#         data = response.json()
#         if not data.get("data"):
#             return None
#         item = data["data"][0]
#         authors = [a["name"] for a in item.get("authors", [])]
#         metadata = {
#             "title": item.get("title"),
#             "authors": authors,
#             "year": item.get("year"),
#             "doi": item.get("doi"),
#             "journal": item.get("venue"),
#             "url": item.get("url"),
#         }
#         return metadata
#     except Exception as e:
#         print(f"⚠️ Error fetching metadata from Semantic Scholar: {e}")
#         return None


# # ---------- LLM Citation Generation ---------- #

# def format_citation_with_llm(metadata: Dict, style: str = "APA") -> str:
#     """
#     Use an LLM to format metadata into a citation in the requested style.
#     """
#     prompt = f"""
#     Generate a {style} citation for the following paper metadata.

#     Metadata:
#     Title: {metadata.get("title")}
#     Authors: {', '.join(metadata.get("authors", []))}
#     Year: {metadata.get("year")}
#     Journal: {metadata.get("journal")}
#     Publisher: {metadata.get("publisher")}
#     DOI: {metadata.get("doi")}
#     URL: {metadata.get("url")}

#     Output only the formatted citation.
#     """

#     response = client.chat.completions.create(
#         model="gpt-4-turbo",
#         messages=[{"role": "user", "content": prompt}],
#         temperature=0.3,
#     )

#     return response.choices[0].message.content.strip()


# # ---------- Main Function ---------- #

# def generate_citation(query: str, style: str = "APA") -> Dict:
#     """
#     1. Fetch metadata from CrossRef or Semantic Scholar
#     2. Generate formatted citation via LLM
#     3. Return structured output
#     """
#     metadata = fetch_metadata_from_crossref(query) or fetch_metadata_from_semantic_scholar(query)
#     if not metadata:
#         return {"error": "Metadata not found for query."}

#     citation_text = format_citation_with_llm(metadata, style)

#     return {
#         "style": style,
#         "metadata": metadata,
#         "citation": citation_text,
#     }




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
