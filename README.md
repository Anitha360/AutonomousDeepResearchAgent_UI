<<<<<<< HEAD
# Deep Research Agent (AutoGen + Ollama)

An **Agentic AI research system** built using Microsoft's AutoGen framework and local LLMs via Ollama.
The system coordinates multiple AI agents to **plan, research, analyze, critique, and generate structured research reports automatically.**

This project demonstrates **modern multi-agent AI architecture** similar to advanced research assistants.

---

## Project Overview

The Deep Research Agent takes a research question and executes a full research workflow:

1. **Planner Agent** – breaks the research query into tasks
2. **Research Agent** – searches the web and gathers sources
3. **Analyst Agent** – extracts key insights from sources
4. **Critic Agent** – validates reasoning and identifies weaknesses
5. **Writer Agent** – produces the final structured research report

The system uses **tools, memory, and multi-agent collaboration** to simulate a real research process.

---

## Architecture

User Query
↓
Planner Agent
↓
Research Agent (Web Search + Scraper)
↓
Analyst Agent
↓
Critic Agent
↓
Writer Agent
↓
Final Research Report

---

## Project Structure

```
deep-research-agent-autogen
│
├── agents
│   ├── planner_agent.py        # Breaks query into research plan
│   ├── research_agent.py       # Uses tools to collect information
│   ├── analyst_agent.py        # Extracts insights
│   ├── critic_agent.py         # Validates analysis
│   └── writer_agent.py         # Generates final report
│
├── config
│   └── model_client.py         # LLM configuration (Ollama / OpenAI API)
│
├── memory
│   └── vector_memory.py        # Vector storage using ChromaDB
│
├── tools
│   ├── search_tool.py          # Web search using DuckDuckGo
│   └── web_scraper.py          # Scrapes article content
│
├── workspace                  # Stores generated reports
│
├── main.py                     # Entry point for research workflow
├── requirements.txt            # Project dependencies
=======
# Autonomous Deep Research AI Agent

An **Agentic AI system** that autonomously performs deep research on a given topic, evaluates information sources, debates conclusions internally, and generates a structured research paper with citations.

The system demonstrates a **multi-agent architecture** where specialized AI agents collaborate to plan research, gather data, analyze findings, validate claims, and produce a final report.

---

# System Overview

The system follows an **agent-orchestrated research pipeline**.

User enters a research topic → the system plans research → gathers web data → stores knowledge → analyzes findings → performs internal debate → generates a structured research paper → exports a PDF.

The project demonstrates the core concepts of **Agentic AI systems** including:

* Autonomous planning
* Iterative research loops
* Memory via vector databases
* Knowledge graph construction
* Multi-agent debate and reasoning
* Automated research report generation

---

# Final System Architecture

```
User (Streamlit UI)
        │
        ▼
Autonomous Research Controller
        │
        ▼
Planner Agent
        │
        ▼
Research Loop (Autonomous)
 ├── Web Search
 ├── Web Scraper
 ├── Vector Memory (ChromaDB)
 └── Knowledge Graph Builder
        │
        ▼
Analyst Agent
        │
        ▼
Debate System
 ├── Critic Agent
 └── Defender Agent
        │
        ▼
Writer Agent
        │
        ▼
Citation Manager
        │
        ▼
PDF Research Paper Generator
```

---

# Project Structure

```
                ┌──────────────┐
                │  Streamlit UI │
                └──────┬───────┘
                       │
                       ▼
                Research Orchestrator
                       │
                       ▼
                  Planner Agent
                       │
                       ▼
         Autonomous Research Pipeline
                       │
        ┌──────────────┼──────────────┐
        ▼                              ▼
   Web Search                      Web Scraper
        │                              │
        └──────────────┬───────────────┘
                       ▼
                   Vector Memory
                       │
                       ▼
                Knowledge Graph
                       │
                       ▼
                  Analyst Agent
                       │
                       ▼
                   Critic Agent
                       ▲
                       │
                  Defender Agent
                       │
                       ▼
                   Writer Agent
                       │
                       ▼
                 Citation Manager
                       │
                       ▼
                   PDF Generator

project/
│
├── main.py                      # CLI entry point
│
├── config/
│   ├── logger.py                # logging configuration
│   └── settings.py              # global config (API keys, model names)
│
├── agents/
│   ├── planner_agent.py
│   ├── analyst_agent.py
│   ├── critic_agent.py
│   ├── defender_agent.py
│   ├── writer_agent.py
│   └── agent_registry.py        # (NEW) register all agents
│
├── pipeline/
│   ├── research_orchestrator.py
│   └── autonomous_research_pipeline.py
│
├── tools/
│   ├── web_search.py
│   ├── web_scraper.py
│   ├── source_ranker.py
│   └── citation_manager.py
│
├── memory/
│   └── vector_store.py
│
├── knowledge/
│   └── knowledge_graph.py
│
├── report/
│   └── pdf_generator.py
│
├── ui/
│   └── app.py                   # Streamlit interface
│
├── report/
│   └── research_report.pdf
│
└── requirements.txt

```

---

<<<<<<< HEAD
## Technologies Used

* Python 3.10+
* AutoGen (Agent framework)
* Ollama (Local LLM runtime)
* DuckDuckGo Search
* BeautifulSoup Web Scraper
* ChromaDB Vector Memory
* Async Python

---

## Installation

### 1. Clone the Repository

```
git clone https://github.com/yourusername/deep-research-agent-autogen.git
cd deep-research-agent-autogen
```

### 2. Create Virtual Environment
=======
# Core Components

## Agents

### Planner Agent

Breaks down the research topic into smaller research questions and determines what information needs to be collected.

### Researcher Agent

Executes the research process using web search and scraping tools.

### Analyst Agent

Analyzes gathered documents and extracts key insights.

### Critic Agent

Challenges the conclusions generated by the analyst and identifies weaknesses or biases.

### Defender Agent

Defends valid conclusions and refines arguments against the critic.

### Writer Agent

Synthesizes all findings into a structured research report.

---

# Memory System

The project includes two memory layers.

## Vector Memory (ChromaDB)

Used for:

* semantic document storage
* similarity search
* retrieval-augmented reasoning

Embeddings are generated using a transformer model from the **sentence-transformers** library.

## Knowledge Graph

Stores relationships between entities discovered during research.

Example:

```
AI Agents → used in → Autonomous Systems
Autonomous Systems → applied in → Robotics
```

This helps the system reason about relationships between concepts.

---

# Research Tools

### Web Search

Finds relevant research sources for the query.

### Web Scraper

Extracts content from webpages.

### Source Ranker

Evaluates sources based on relevance and quality.

### Citation Manager

Generates formatted references for the research report.

---

# Pipeline Workflow

The **Autonomous Research Pipeline** orchestrates the entire process:

1. User enters a research topic
2. Planner Agent generates research plan
3. Researcher Agent gathers sources
4. Documents are stored in vector memory
5. Knowledge graph is built
6. Analyst Agent extracts insights
7. Critic and Defender agents debate findings
8. Writer Agent generates final report
9. Citation Manager compiles references
10. PDF generator produces research paper

---

# Streamlit User Interface

The system includes a simple web interface built with **Streamlit**.

Features:

* enter research topic
* run autonomous research
* view summarized findings
* download generated research paper

Run the UI:

```
streamlit run ui/streamlit_app.py
```

---

# Installation

Clone the repository

```
git clone <repo-url>
cd autonomous-research-agent
```

Create virtual environment
>>>>>>> c5b555e (autonomous AI agent with streamlit)

```
python -m venv venv
```

Activate environment

Windows

```
venv\Scripts\activate
```

<<<<<<< HEAD
Mac/Linux

```
source venv/bin/activate
```

### 3. Install Dependencies
=======
Install dependencies
>>>>>>> c5b555e (autonomous AI agent with streamlit)

```
pip install -r requirements.txt
```

---

<<<<<<< HEAD
## Install Ollama

Download and install Ollama from:

https://ollama.com

Then pull a model:

```
ollama pull qwen2.5:7b
```

Start the Ollama server:

```
ollama serve
```

Ollama runs at:

```
http://localhost:11434
```

---

## Run the Project

Start the research system:

```
python main.py
```

Example query:

```
Enter your research topic:
Future of Agentic AI systems
```

The agents will collaboratively generate a **structured research report**.

---

## Example Output

The system produces reports like:

```
Research Topic: Future of Agentic AI

1. Introduction
2. Key Technologies
3. Current Industry Applications
4. Challenges and Limitations
5. Future Outlook
6. References
```

Reports are saved inside the **workspace folder**.

---

## Features

* Multi-Agent AI architecture
* Tool-enabled research agents
* Automated web search
* Web content scraping
* Vector memory storage
* Modular and extensible design
* Works with local LLMs using Ollama

---

## Future Improvements

Possible enhancements:

* Streamlit UI for interactive research
* Multi-source ranking and scoring
* Self-reflection agent loop
* Automatic PDF report generation
* Knowledge graph integration
* Multi-model routing

---

## Use Cases

This project can be used for:

* Automated research assistants
* AI knowledge gathering systems
* Competitive intelligence tools
* Academic literature analysis
* Agentic AI experimentation

---

## Author

Built as part of an **Agentic AI engineering portfolio project**.

---

## License

MIT License
=======
# Running the System

Start the Streamlit interface

```
streamlit run ui/streamlit_app.py
```

Enter a research topic and the system will automatically perform research and generate a downloadable report.

---

# Example Query

```
Agentic AI systems in enterprise automation
```

The system will:

* gather research sources
* analyze information
* perform internal reasoning
* generate a research paper with citations

---

# Future Improvements

Possible enhancements include:

* multi-step reasoning with advanced LLMs
* academic source prioritization
* real-time agent reasoning visualization
* improved knowledge graph visualization
* deeper autonomous research loops

---

# Technologies Used

* Python
* Streamlit
* ChromaDB
* Sentence Transformers
* ReportLab
* Web Scraping
* Multi-Agent AI Architecture

---

# Learning Goals

This project demonstrates how to build **Agentic AI systems capable of autonomous reasoning and research**.

It is designed as a practical example of:

* AI agents
* retrieval-augmented systems
* research automation pipelines
* multi-agent reasoning frameworks
>>>>>>> c5b555e (autonomous AI agent with streamlit)


Opencode Gemini
This project implements an Autonomous Deep Research AI Agent with two primary flows: a Multi-Agent Collaborative Chat Flow (via CLI) and a Procedural Web Scraper & Report Pipeline (via Streamlit UI).
1. Multi-Agent Collaborative Chat Flow (main.py)
This flow uses the Microsoft AutoGen framework to orchestrate 5 specialized LLM agents in a cooperative sequence:
[User Input: Topic]
       │
       ▼
 ┌───────────┐
 │  Planner  │ ──► Structured research plan & key questions
 └─────┬─────┘
       ▼
 ┌───────────┐
 │Researcher │ ──► Executes tools: search_web() & scrape_page()
 └─────┬─────┘
       ▼
 ┌───────────┐
 │  Analyst  │ ──► Identifies patterns, trends, and key insights
 └─────┬─────┘
       ▼
 ┌───────────┐
 │  Critic   │ ──► Evaluates research quality, gaps, & weak arguments
 └─────┬─────┘
       ▼
 ┌───────────┐
 │  Writer   │ ──► Synthesizes findings into a final structured report
 └───────────┘
- Execution Engine: RoundRobinGroupChat sequentially rotates through these agents for up to 12 turns.
- LLM Client: Agents use OpenAIChatCompletionClient pointing to a local Ollama instance (qwen2.5:7b on port 11434).
2. Procedural Research & Report Pipeline Flow (ui/streamlit_app.py)
This flow provides an interactive web UI that bypasses the multi-agent chat and runs a programmatic research, ingestion, and publishing pipeline:
[Streamlit UI Input] ──► run_autonomous_research(query)
                                │
                                ▼
                        ┌──────────────┐
                        │ search_web() │ ──► DuckDuckGo search returns top 5 URLs
                        └──────┬───────┘
                               ▼
                        ┌──────────────┐
                        │ scrape_page()│ ──► Requests pages & parses paragraphs (<5000 chars)
                        └──────┬───────┘
                               ▼
                        ┌──────────────┐
                        │ Vector Store │ ──► Embeds and indexes text using `SentenceTransformer`
                        └──────┬───────┘     and local `ChromaDB`
                               ▼
                        ┌──────────────┐
                        │ rank_sources │ ──► Filters and ranks the top 3 longest sources
                        └──────┬───────┘
                               ▼
                        ┌──────────────┐
                        │ generate_pdf │ ──► Combines top sources + citations and compiles
                        └──────────────┘     a PDF using `ReportLab`
3. Core Components Summary
- tools/: 
- web_search.py: Integrates ddgs (DuckDuckGo Search) to query and retrieve URLs.
- web_scraper.py: Fetches pages via requests and parses content using BeautifulSoup.
- source_ranker.py: Ranks collected text based on length/completeness.
- citation_manager.py: Formats referenced URLs into numeric citations.
- memory/:
- vector_store.py: Local vector storage utilizing chromadb and all-MiniLM-L6-v2 embeddings.
- knowledge_graph.py: Builds node-edge relationships using networkx for structured semantic querying.
- report/pdf_generator.py: Compiles the title, content, and bibliography into a formatted PDF using ReportLab's flowable story structure.