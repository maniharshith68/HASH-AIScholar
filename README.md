# 🧠 Hash#AI Scholar: Your GenAI-Powered Research Companion

AI Scholar is a generative AI-powered tool designed to revolutionize how researchers, students, and professionals interact with academic papers and conference presentations. It doesn't just summarize — it understands, contextualizes, and narrates the research journey. And even more, it add the human touch, by providing insights from the conferences where this paper was presented/mentioned/taked about. It enriches the value that an AI Scholar assistant can add to a student's attempt at understanding a research paper.

---

## 🚀 Features

- 📄 **Summarize Research Papers**  
  Generate concise, human-readable summaries of academic PDFs.

- 🧮 **Extract Key Equations**  
  Automatically detect and display mathematical expressions and formal definitions.

- 🧪 **Explain Methods**  
  Translate complex methodologies into plain language explanations.

- 🔍 **Suggest Related Papers**  
  Discover similar or foundational works using semantic search and LLMs.

- 📝 **Generate Citations**  
  Output formatted citations in APA, MLA, or BibTeX styles — with download support.

- 🎤 **Summarize Conference Presentations**  
  Analyze transcripts to extract human insights, network context, and trend understanding.

- 🔊 **AI Voice Narration**  
  Listen to narrated summaries and insights using ElevenLabs voice synthesis.

---

## 🧰 Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python, OpenAI GPT-4  
- **Voice:** ElevenLabs API  
- **PDF Parsing:** PyMuPDF  
- **Citation Formatting:** LLM + Custom Templates  
- **Deployment:** Streamlit Cloud / Render / Local

---

## To Run this project:
1. Install everything mentioned in requirements.txt
2. Add your OpenAI and Elevenlabs API key in config.py.
3. In terminal, run command: "streamlit run main.py"
   For the purpose of testing, we have used a 1 page PDF about LLMs and a transcript of a 1 min video about LLMs.

You can find the sample files we used, and the screenshots of the content generated in dir 'usage-example'

---

## 📦 Installation
Make sure that after the repo is cloned, add your relevant API keys in config.py in your local repo.

```bash
git clone https://github.com/yourusername/Hash-AIScholar.git
cd Hash-AIScholar
pip install -r requirements.txt
streamlit run main.py

