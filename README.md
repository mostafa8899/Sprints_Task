# 🧠 NeoAI Insight Engine

A dynamic, multi-agent R&D simulation ecosystem designed for autonomous data collection, trend analysis, and the generation of research directions using powerful LLMs via Groq API. This project fulfills the full scope of the **Adaptive Research & Innovation Agent Ecosystem** challenge.

## 📌 Table of Contents

- [🔍 Project Overview](#-project-overview)
- [🧠 Agent Architecture](#-agent-architecture)
- [🌐 Integrations & Features](#-integrations--features)
- [📦 File Structure](#-file-structure)
- [🚀 How to Run](#-how-to-run)
- [🧪 Testing](#-testing)
- [📘 Design Highlights](#-design-highlights)
- [📸 Screenshots](#-screenshots)
- [📩 Submission Info](#-submission-info)

## 🔍 Project Overview

This project simulates a modern, adaptive R&D environment composed of multiple intelligent agents:

- **Research Agent**: pulls live AI-related data from a third-party API (GNews).
- **Insight Agent**: extracts key concepts and performs basic NLP.
- **Innovation Agent**: synthesizes a full research proposal using LLMs via the [Groq API](https://console.groq.com/).

All components work together in a modular, real-time system inspired by how research labs operate.

## 🧠 Agent Architecture

Each agent in the system serves a distinct role:

| Agent              | Role                                                                 |
|-------------------|----------------------------------------------------------------------|
| `DataCollectorAgent` | Pulls data from GNews API (filtered and capped)                    |
| `InsightAgent`     | Performs keyword extraction using `spaCy` NLP model                 |
| `IdeaGeneratorAgent` | Uses Groq-hosted LLMs to generate a structured Markdown report      |

Agents communicate sequentially (and could be extended to async or message-based models later).

## 🌐 Integrations & Features

- ✅ External API: [GNews API](https://gnews.io/)
- ✅ LLMs: [Groq Cloud](https://console.groq.com/) (LLaMA 3, Mixtral, etc.)
- ✅ Frameworks: FastAPI backend, Streamlit frontend
- ✅ Error handling, fallbacks, and timeout management included
- ✅ Clean modular Python structure

## 📦 File Structure

```
neoai_insight_engine/
│
├── agents/
│   ├── data_collector_agent.py     # Fetches news data from GNews API
│   ├── insight_agent.py            # Extracts keywords using spaCy
│   └── idea_generator_agent.py     # Generates proposals using Groq LLM
│
├── api/
│   └── api.py                      # FastAPI backend serving /generate endpoint
│
├── frontend/
│   └── app.py                      # Streamlit frontend
│
├── requirements.txt                # All dependencies
└── README.md                       # This file
```

## 🚀 How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

> Ensure Python 3.10+ is installed.

### 2. Set API Keys

Replace the placeholder Groq API key in `idea_generator_agent.py`:
```python
api_key = "your_groq_api_key"
```

Add your [GNews API key](https://gnews.io/) in `data_collector_agent.py`.

### 3. Run Backend (FastAPI)

```bash
cd api
uvicorn api:app --reload
```

> Should be available at: http://localhost:8000

### 4. Run Frontend (Streamlit)

```bash
cd frontend
streamlit run app.py
```

## 🧪 Testing

You can test the backend directly using `curl`:

```bash
curl -X POST http://localhost:8000/generate/   -H "Content-Type: application/json"   -d '{"query": "AI in medicine", "model": "llama3-8b-8192"}'
```

Or from the UI: type a topic and press "🚀 Generate Report"

## 📘 Design Highlights

- 🔄 Agents are fully decoupled — interchangeable and testable
- 🧠 NLP powered by `spaCy` and LLMs via Groq Cloud
- 🛡️ Handles API errors gracefully
- 🖼️ Styled with custom Streamlit UI components
- 🧱 Built to be extended: can add chat, new agents, or real-time PubSub

## 📸 Screenshots

> _Add screenshots of the frontend, keyword list, and markdown report._

## 📩 Submission Info

**Subject**:  
`R&D Project Submission – [Your Name] – Adaptive Research & Innovation Agent Ecosystem`

**Email**:  
yehia.mohamed@sprints.ai  
CC: mohamed.farouk@sprints.ai, osama.hussien@sprints.ai  

**Include**:
- GitHub repo link
- Add all 3 reviewers as GitHub collaborators
- A 200–300 word email body summarizing the project

## ⚠️ Evaluation Notes

This project showcases:

- Modular system design
- Autonomous agent workflows
- Clear UI/UX
- Adaptability to real-world data
- LLM integration via modern APIs

## 🏁 Final Submission Deadline

**📅 August 6, 2025 – 12:00 PM (Africa/Cairo)**

---

Made with 💙 for innovation.
