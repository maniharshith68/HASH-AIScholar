# main.py
import streamlit as st
from utils.pdf_parser import extract_text_from_pdf
from utils.transcript_parser import extract_text_from_transcript
from utils.summarizer import summarize_text
from utils.equation_extractor import extract_equations
from utils.method_explainer import explain_methods
from utils.related_papers import suggest_related_papers
from utils.citation_generator import generate_citation
from utils.conference_insights import summarize_conference
import tempfile

from utils.voice_narrator import narrate_text
import streamlit.components.v1 as components
import base64


st.set_page_config(page_title="HASH# AI Scholar", layout="wide")
st.title("📚 HASH# AI Scholar: Your Research Companion")

st.sidebar.header("Upload Files")
pdf_file = st.sidebar.file_uploader("Upload Research Paper (PDF)", type=["pdf"])
transcript_file = st.sidebar.file_uploader("Upload Conference Transcript (TXT)", type=["txt"])

if pdf_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(pdf_file.read())
        paper_text = extract_text_from_pdf(tmp.name)

    st.header("1. 📄 Paper Summary")
    # st.write(summarize_text(paper_text))
    summary = summarize_text(paper_text)
    st.write(summary)

    if st.button("🔊 Narrate Summary"):
        audio_path = narrate_text(summary)
        with open(audio_path, "rb") as audio_file:
            audio_bytes = audio_file.read()
            b64 = base64.b64encode(audio_bytes).decode()
            audio_html = f"""
            <audio autoplay controls>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
            components.html(audio_html, height=80)

    # Add download button
    st.download_button(
    label="📥 Download Summary",
    data=summary,
    file_name="summary.txt",
    mime="text/plain")


    st.header("2. 🧮 Key Equations")
    equations = extract_equations(paper_text)
    if equations:
        for eq in equations:
            st.code(eq)
    else:
        st.info("No equations found.")

    st.header("3. 🧪 Method Explanation")
    st.write(explain_methods(paper_text))

    st.header("4. 🔍 Suggested Related Papers")
    st.markdown(suggest_related_papers(paper_text))

    st.header("5. 📝 Citation")
    st.code(generate_citation(paper_text))

if transcript_file:
    transcript_text = transcript_file.read().decode("utf-8")
    st.header("6. 🎤 Conference Summary & Human Insights")
    st.write(summarize_conference(transcript_text))
