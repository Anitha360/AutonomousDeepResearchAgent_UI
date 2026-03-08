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
└── README.md
```

---

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

```
python -m venv venv
```

Activate environment

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

---

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
