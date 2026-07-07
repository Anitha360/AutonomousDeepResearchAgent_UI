# Architecture Diagram — Autonomous Deep Research AI Agent

```mermaid
---
title: System Architecture — Dual-Flow Research Agent
---
graph TB
    subgraph User_Interface["User Interface Layer"]
        CLI["CLI (main.py)"]
        UI["Streamlit Web App<br/>(ui/streamlit_app.py)"]
    end

    subgraph Orchestration["Orchestration Layer"]
        subgraph Flow1["Flow 1: AutoGen Multi-Agent Chat"]
            RGC["RoundRobinGroupChat<br/>max_turns=12"]
            PA["Planner Agent<br/>Breaks problem into tasks"]
            RA["Researcher Agent<br/>Has tool access"]
            AA["Analyst Agent<br/>Extracts patterns & insights"]
            CA["Critic Agent<br/>Validates reasoning & gaps"]
            WA["Writer Agent<br/>Produces final report"]
        end

        subgraph Flow2["Flow 2: Procedural Pipeline"]
            ARP["autonomous_research_pipeline.py"]
        end
    end

    subgraph Tools["Tool Layer"]
        WS["web_search.py<br/>DuckDuckGo API<br/>Top 5 results"]
        WSC["web_scraper.py<br/>requests + BeautifulSoup<br/>5000 char limit"]
        SR["source_ranker.py<br/>Sorts by text length<br/>Returns top 3"]
        CM["citation_manager.py<br/>[1], [2], [3] formatting"]
    end

    subgraph Memory["Memory & Knowledge Layer"]
        VS["vector_store.py<br/>ChromaDB (in-memory)<br/>+ SentenceTransformer<br/>all-MiniLM-L6-v2"]
        KG["knowledge_graph.py<br/>NetworkX graph<br/>(NOT YET INTEGRATED)"]
    end

    subgraph LLM["LLM Backend"]
        OLLAMA["Ollama (local)<br/>qwen2.5:7b<br/>http://localhost:11434/v1"]
    end

    subgraph Output["Output Layer"]
        PDF["pdf_generator.py<br/>ReportLab → research_report.pdf"]
        CONSOLE["Console stream"]
    end

    subgraph Config["Configuration"]
        LOG["logger.py<br/>Python logging"]
        MC["model_client.py<br/>OpenAIChatCompletionClient<br/>→ Ollama"]
    end

    %% Connections for Flow 1
    CLI --> RGC
    RGC --> PA --> RA --> AA --> CA --> WA
    RA --> WS
    RA --> WSC
    RGC --> CONSOLE
    OLLAMA --- MC
    MC --- RGC

    %% Connections for Flow 2
    UI --> ARP
    ARP --> WS
    ARP --> WSC
    WSC --> VS
    ARP --> SR
    ARP --> CM
    CM --> PDF
    SR --> PDF
    PDF --> UI

    %% Styling
    classDef flow1 fill:#e1f5fe,stroke:#0288d1,stroke-width:2px
    classDef flow2 fill:#fff3e0,stroke:#f57c00,stroke-width:2px
    classDef shared fill:#f3e5f5,stroke:#7b1fa2,stroke-width:2px
    classDef output fill:#e8f5e9,stroke:#388e3c,stroke-width:2px
    classDef infra fill:#fce4ec,stroke:#c62828,stroke-width:2px

    class PA,RA,AA,CA,WA,RGC flow1
    class ARP flow2
    class WS,WSC,SR,CM shared
    class VS,KG shared
    class PDF,CONSOLE output
    class OLLAMA,MC,LOG infra
    class CLI,UI infra
```

---

## Data Flow Diagrams

### Flow 1: Multi-Agent CLI (AutoGen)

```mermaid
sequenceDiagram
    actor User
    participant CLI as main.py
    participant RGC as RoundRobinGroupChat
    participant PA as Planner Agent
    participant RA as Researcher Agent
    participant AA as Analyst Agent
    participant CA as Critic Agent
    participant WA as Writer Agent
    participant Tools as search_web + scrape_page
    participant LLM as Ollama (qwen2.5:7b)

    User->>CLI: Enter research topic
    CLI->>RGC: Start conversation (max 12 turns)
    
    loop Round-robin
        RGC->>PA: Next turn
        PA->>LLM: Generate research plan
        LLM-->>PA: Structured tasks
        PA-->>RGC: Plan output

        RGC->>RA: Next turn
        RA->>LLM: Request research actions
        LLM-->>RA: Decide to search
        RA->>Tools: search_web(query)
        Tools-->>RA: URLs
        RA->>Tools: scrape_page(url)
        Tools-->>RA: Text content
        RA-->>RGC: Research summary

        RGC->>AA: Next turn
        AA->>LLM: Analyze findings
        LLM-->>AA: Patterns & insights
        AA-->>RGC: Analysis output

        RGC->>CA: Next turn
        CA->>LLM: Critique research
        LLM-->>CA: Gaps & weaknesses
        CA-->>RGC: Critique output

        RGC->>WA: Next turn
        WA->>LLM: Write report section
        LLM-->>WA: Structured text
        WA-->>RGC: Report output
    end

    RGC-->>CLI: Full conversation history
    CLI-->>User: Console output (streamed live)
```

### Flow 2: Web UI Pipeline (Streamlit)

```mermaid
sequenceDiagram
    actor User
    participant UI as Streamlit App
    participant Pipe as research_pipeline.py
    participant WS as web_search.py
    participant WSC as web_scraper.py
    participant VS as vector_store.py
    participant SR as source_ranker.py
    participant CM as citation_manager.py
    participant PDF as pdf_generator.py

    User->>UI: Enter research query
    UI->>Pipe: run_autonomous_research(query)
    
    Pipe->>WS: search_web(query)
    WS-->>Pipe: [url1, url2, ..., url5]
    
    loop For each URL
        Pipe->>WSC: scrape_page(url)
        WSC-->>Pipe: page_text (5000 chars)
        Pipe->>VS: add_document(text, url)
        VS-->>Pipe: stored (in-memory)
    end

    Pipe->>SR: rank_sources(documents)
    SR-->>Pipe: top_3_docs (sorted by length)

    Pipe-->>UI: (ranked_docs, urls)

    UI->>CM: generate_citations(urls)
    CM-->>UI: ["[1] url1", "[2] url2", ...]

    UI->>PDF: generate_pdf(title, content, citations)
    PDF-->>UI: research_report.pdf

    UI-->>User: ✅ Success message + preview + download button
```

---

## Component Responsibility Matrix

| Component | Technology | Responsibility | Used In |
|---|---|---|---|
| **Planner Agent** | AutoGen + Ollama | Decompose research question into structured subtasks | Flow 1 |
| **Researcher Agent** | AutoGen + Ollama + Tools | Execute web searches and scrape content | Flow 1 |
| **Analyst Agent** | AutoGen + Ollama | Identify patterns, trends, key insights | Flow 1 |
| **Critic Agent** | AutoGen + Ollama | Validate reasoning, flag missing info | Flow 1 |
| **Writer Agent** | AutoGen + Ollama | Synthesize findings into structured report | Flow 1 |
| **Research Pipeline** | Python procedural | Deterministic search→scrape→rank→PDF | Flow 2 |
| **Web Search** | DuckDuckGo (ddgs) | Retrieve top 5 URLs for query | Both |
| **Web Scraper** | requests + BeautifulSoup | Extract text from HTML pages | Both |
| **Source Ranker** | Python (sort by len) | Rank documents, return top 3 | Flow 2 |
| **Vector Store** | ChromaDB + SentenceTransformer | Embed & store documents (in-memory) | Flow 2 |
| **PDF Generator** | ReportLab | Generate downloadable PDF report | Flow 2 |
| **Knowledge Graph** | NetworkX | Construct entity-relation graph (planned) | — |

---

## Key Architectural Decisions

| Decision | Rationale | Trade-off |
|---|---|---|
| **Two independent flows** (AutoGen + pipeline) | Separates LLM-dependent research from deterministic data gathering | Code duplication; maintenance burden |
| **Local-only stack** (Ollama, DuckDuckGo, ChromaDB) | Zero API costs, fully offline capable | Limited to smaller models; search coverage narrower than Bing/Google |
| **In-memory vector store** | Simplicity for demo/portfolio | Data lost on restart; not production-ready |
| **Single-agent tool access** (Researcher only) | Enforces separation of concerns per AutoGen best practices | Other agents cannot verify facts directly |
| **No LLM in Flow 2** | Faster execution; no Ollama dependency for PDF generation | Report is raw scraped text, not a synthesized analysis |

---

## Scaling / Production Roadmap

```mermaid
graph LR
    subgraph Current["Current State"]
        C1["Local Ollama<br/>qwen2.5:7b"]
        C2["ChromaDB in-memory"]
        C3["DuckDuckGo search"]
        C4["Single-user CLI + Streamlit"]
    end

    subgraph Near_Term["Near-Term Improvements"]
        N1["Replace Ollama → OpenAI / Anthropic API"]
        N2["Persistent ChromaDB / Pinecone"]
        N3["Add Google Custom Search / Bing API"]
        N4["Async pipeline + caching"]
    end

    subgraph Future["Production Architecture"]
        F1["FastAPI backend + React/Svelte frontend"]
        F2["PostgreSQL + pgvector"]
        F3["Task queue (Celery + Redis)"]
        F4["Auth, rate-limiting, monitoring"]
        F5["Multi-session state management"]
    end

    C1 --> N1
    C2 --> N2
    C3 --> N3
    C4 --> N4
    N1 --> F1
    N2 --> F2
    N3 --> F3
    N4 --> F4
    F1 --> F5
```

---

## How to Explain This in a Tech Interview

### 30-Second Elevator Pitch

> *"This is an autonomous deep research system built with Python. It has two architectural modes: a **multi-agent chat** using Microsoft AutoGen where five AI agents collaborate in a round-robin conversation to research a topic, and a **procedural pipeline** served through a Streamlit UI that searches the web, scrapes content into a vector database, ranks sources, and generates a PDF report. The entire stack runs locally using Ollama for LLM inference and DuckDuckGo for search — no API keys needed."*

### 2-Minute Deep Dive

> *"The architecture is split into two independent flows sharing a common tool layer. The **first flow** is a research-grade multi-agent system: five AutoGen agents (Planner, Researcher, Analyst, Critic, Writer) take turns in a RoundRobinGroupChat. Only the Researcher has tool access — it calls `web_search` and `scrape_page` — while the others provide pure LLM reasoning. All agents use the same local Ollama model via an OpenAI-compatible client.*
>
> *"The **second flow** is a deterministic pipeline for the Streamlit UI. When a user submits a query, it searches DuckDuckGo, scrapes each result with BeautifulSoup, embeds and stores the content in an in-memory ChromaDB vector store, ranks the sources by length, and generates a PDF with ReportLab. This flow does not use LLMs — it is purely data gathering and formatting — which makes it fast and reliable but lacks the analytical depth of the agentic flow.*
>
> *"The **tool layer** is shared between both flows and includes web search, scraping, ranking, and citation formatting. The **memory layer** has a ChromaDB vector store and a built but not yet integrated NetworkX knowledge graph. The **config layer** handles logging and LLM client configuration. This modular separation means either flow can be extended independently.*
>
> *"The biggest architectural decision was keeping the two flows separate rather than integrating them. This was intentional — it lets the demo highlight both the AutoGen multi-agent paradigm and a simpler procedural approach, making it more educational as a portfolio project. In production, I would merge them: use the agentic flow for topic understanding and the pipeline for fast data retrieval, with a shared persistent vector store and async task queue."*

### Potential Interview Questions & Answers

| Question | Answer |
|---|---|
| **Why two flows instead of one?** | The project serves dual purposes: the AutoGen flow showcases multi-agent orchestration, while the Streamlit flow provides a fast, interactive demo. In production, I'd refactor both to share a unified orchestration layer. |
| **Why only the Researcher agent has tools?** | This follows the AutoGen principle of separation of concerns — agents specialize in reasoning or action, not both. It also prevents the Critic or Writer from making uncontrolled external calls. |
| **Why DuckDuckGo instead of Google/Bing?** | Zero API cost and no API key requirement. For a portfolio project with local-only requirements, it was the pragmatic choice. There's a clear upgrade path to Google Custom Search or Bing API. |
| **Why is the vector store in-memory?** | Simplicity for demo purposes. The `vector_store.py` module has a clean interface, so swapping to persistent ChromaDB or Pinecone is a single-line change. |
| **No tests — why?** | This is an early-stage demo project. I'd add pytest tests for the pipeline functions, tool modules, and PDF generation before production deployment. |
| **How would you handle errors from web scraping?** | Currently errors are swallowed with a bare `except`. I'd add retry logic with exponential backoff, request timeouts, user-agent rotation, and structured error propagation up the call stack. |
