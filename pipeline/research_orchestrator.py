# pipeline/research_orchestrator.py
import asyncio
import os

from config.logger import get_logger
from agents.agent_registry import get_agents

from pipeline.autonomous_research_pipeline import run_autonomous_research
from tools.citation_manager import generate_citations
from report.pdf_generator import generate_pdf

logger = get_logger("ResearchOrchestrator")


async def run_research(topic: str):
    logger.info("Starting research orchestration for topic: %s", topic)

    # -----------------------------
    # Initialize agents from registry
    # -----------------------------
    agents = get_agents()
    planner = agents["planner"]
    analyst = agents["analyst"]
    critic = agents["critic"]
    defender = agents["defender"]
    writer = agents["writer"]

    # -----------------------------
    # 1. PLANNER AGENT
    # -----------------------------
    logger.info("Running planner agent")
    plan = await planner.run(
        task=f"Break this research topic into key research questions: {topic}"
    )
    research_plan = plan.messages[-1].content

    # -----------------------------
    # 2. AUTONOMOUS RESEARCH PIPELINE
    # -----------------------------
    logger.info("Running autonomous research pipeline")
    documents, urls = await run_autonomous_research(topic)
    combined_docs = "\n\n".join(documents)

    # -----------------------------
    # 3. ANALYST AGENT
    # -----------------------------
    logger.info("Running analyst agent")
    analysis = await analyst.run(
        task=f"""
Analyze the following research documents.

Research Plan:
{research_plan}

Documents:
{combined_docs}
"""
    )
    analysis_text = analysis.messages[-1].content

    # -----------------------------
    # 4. CRITIC AGENT
    # -----------------------------
    logger.info("Running critic agent")
    critique = await critic.run(
        task=f"""
Critically evaluate the following research analysis.

Analysis:
{analysis_text}
"""
    )
    critique_text = critique.messages[-1].content

    # -----------------------------
    # 5. DEFENDER AGENT
    # -----------------------------
    logger.info("Running defender agent")
    defense = await defender.run(
        task=f"""
Respond to the critic and defend the conclusions.

Critique:
{critique_text}

Analysis:
{analysis_text}
"""
    )
    defense_text = defense.messages[-1].content

    # -----------------------------
    # 6. WRITER AGENT
    # -----------------------------
    logger.info("Running writer agent")
    report = await writer.run(
        task=f"""
Write a structured research paper about: {topic}

Research Plan:
{research_plan}

Insights:
{analysis_text}

Criticism:
{critique_text}

Defense:
{defense_text}
"""
    )
    final_report = report.messages[-1].content

    # -----------------------------
    # 7. CITATIONS
    # -----------------------------
    citations = generate_citations(urls)

    # -----------------------------
    # 8. PDF GENERATION
    # -----------------------------
    os.makedirs("report", exist_ok=True)
    pdf_path = "report/research_report.pdf"
    generate_pdf(
        title=topic,
        content=final_report,
        citations=citations,
        filename=pdf_path,
    )

    logger.info("Research pipeline completed")
    return {
        "plan": research_plan,
        "analysis": analysis_text,
        "critique": critique_text,
        "defense": defense_text,
        "report": final_report,
        "citations": citations,
        "pdf_path": pdf_path,
    }