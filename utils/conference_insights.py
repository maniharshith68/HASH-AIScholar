# # utils/conference_insights.py

# import os
# import json
# import requests
# from openai import OpenAI
# from bertopic import BERTopic
# from sentence_transformers import SentenceTransformer

# # Initialize OpenAI client
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# # ---------- If present, External Context: Conference Metadata ---------- #

# def fetch_conference_metadata(paper_title: str):
#     """
#     Fetch metadata (venue, year, connected papers) from Semantic Scholar.
#     """
#     url = "https://api.semanticscholar.org/graph/v1/paper/search"
#     params = {
#         "query": paper_title,
#         "limit": 1,
#         "fields": "title,venue,year,authors,citationCount,influentialCitationCount,url"
#     }
#     try:
#         response = requests.get(url, params=params, timeout=10)
#         response.raise_for_status()
#         data = response.json().get("data", [])
#         if not data:
#             return None
#         paper = data[0]
#         return {
#             "title": paper.get("title"),
#             "conference": paper.get("venue"),
#             "year": paper.get("year"),
#             "citation_count": paper.get("citationCount"),
#             "influential_citations": paper.get("influentialCitationCount"),
#             "authors": [a.get("name") for a in paper.get("authors", [])],
#             "url": paper.get("url"),
#         }
#     except Exception as e:
#         print(f"⚠️ Error fetching conference metadata: {e}")
#         return None


# # ---------- NLP Preprocessing & Topic Modeling ---------- #

# def extract_topics_from_transcript(transcript: str, top_n: int = 5):
#     """
#     Use BERTopic to identify major themes in the conference transcript.
#     """
#     model = SentenceTransformer("all-MiniLM-L6-v2")
#     topic_model = BERTopic(verbose=False)
#     sentences = [s for s in transcript.split(".") if len(s.split()) > 5]
#     if not sentences:
#         return []
#     topics, _ = topic_model.fit_transform(sentences)
#     topic_info = topic_model.get_topic_info()
#     return topic_info.head(top_n).to_dict("records")


# # ---------- LLM Analysis ---------- #

# def analyze_conference_with_llm(transcript: str, metadata: dict = None):
#     """
#     Use an LLM to synthesize:
#     - Human insights
#     - Network context
#     - Trend understanding
#     - Relevance to research paper
#     """
#     context_block = ""
#     if metadata:
#         context_block = f"""
#         Conference Metadata:
#         - Conference: {metadata.get("conference")}
#         - Year: {metadata.get("year")}
#         - Authors: {', '.join(metadata.get('authors', []))}
#         - Citation Count: {metadata.get('citation_count')}
#         - Influential Citations: {metadata.get('influential_citations')}
#         """

#     prompt = f"""
#     You are an academic summarization assistant.
#     Analyze this conference transcript and extract:

#     1. **Key Human Insights:** opinions, intuitions, or qualitative judgments expressed by speakers.
#     2. **Network Context:** mention of collaborators, institutions, or influential research networks.
#     3. **Trend Understanding:** emerging research directions, technologies, or patterns discussed.
#     4. **Relevance:** how this conference content connects to the research paper topic.

#     {context_block}

#     Transcript:
#     {transcript}

#     Provide a structured JSON output with fields:
#     "human_insights", "network_context", "trend_analysis", "relevance_summary".
#     """

#     response = client.chat.completions.create(
#         model="gpt-4-turbo",
#         messages=[{"role": "user", "content": prompt}],
#         temperature=0.6,
#     )

#     content = response.choices[0].message.content.strip()

#     # Try block to parse JSON
#     try:
#         parsed = json.loads(content)
#     except Exception:
#         parsed = {"raw_response": content}

#     return parsed


# # ---------- Main Pipeline ---------- #

# def summarize_conference(transcript: str, paper_title: str = None):
#     """
#     Full pipeline:
#     1. fetch conference metadata (Semantic Scholar)
#     2. Extract topics using BERTopic
#     3. Generate structured insights via LLM
#     """
#     metadata = fetch_conference_metadata(paper_title) if paper_title else None
#     topics = extract_topics_from_transcript(transcript)
#     llm_output = analyze_conference_with_llm(transcript, metadata)

#     return {
#         "metadata": metadata,
#         "key_topics": topics,
#         "insights": llm_output,
#     }



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
