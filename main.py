# import asyncio

# from agents.planner_agent import create_planner
# from agents.analyst_agent import create_analyst
# from agents.critic_agent import create_critic
# from agents.defender_agent import create_defender
# from agents.writer_agent import create_writer

# from pipeline.autonomous_research_pipeline import run_autonomous_research
# from tools.citation_manager import generate_citations
# from report.pdf_generator import generate_pdf

# from config.logger import get_logger


# logger = get_logger("ResearchOrchestrator")


# async def main():

#     logger.info("Starting autonomous research orchestration")

#     topic = input("Enter research topic: ")
#     logger.info("User entered research topic: %s", topic)

#     # Create agents
#     logger.info("Initializing agents")

#     planner = create_planner()
#     analyst = create_analyst()
#     critic = create_critic()
#     defender = create_defender()
#     writer = create_writer()

#     logger.info("Agents initialized successfully")

#     # STEP 1: Planner
#     logger.info("Running Planner Agent")

#     plan = await planner.run(
#         task=f"Break this research topic into key research questions: {topic}"
#     )

#     research_plan = plan.messages[-1].content

#     logger.info("Planner agent completed research planning")

#     print("\nResearch Plan:\n", research_plan)

#     # STEP 2: Run autonomous research
#     logger.info("Starting autonomous research pipeline")

#     documents, urls = run_autonomous_research(topic)

#     logger.info("Research pipeline returned %d documents", len(documents))

#     combined_docs = "\n\n".join(documents)

#     # STEP 3: Analyst
#     logger.info("Running Analyst Agent")

#     analysis = await analyst.run(
#         task=f"""
# Analyze the following research documents and extract key insights.

# Documents:
# {combined_docs}
# """
#     )

#     analysis_text = analysis.messages[-1].content

#     logger.info("Analyst agent completed analysis")

#     # STEP 4: Critic
#     logger.info("Running Critic Agent")

#     critique = await critic.run(
#         task=f"""
# Critically evaluate this research analysis.

# Analysis:
# {analysis_text}
# """
#     )

#     critique_text = critique.messages[-1].content

#     logger.info("Critic agent completed critique")

#     # STEP 5: Defender
#     logger.info("Running Defender Agent")

#     defense = await defender.run(
#         task=f"""
# Respond to the critic and defend the research conclusions.

# Critique:
# {critique_text}

# Analysis:
# {analysis_text}
# """
#     )

#     defense_text = defense.messages[-1].content

#     logger.info("Defender agent completed defense")

#     # STEP 6: Writer
#     logger.info("Running Writer Agent")

#     report = await writer.run(
#         task=f"""
# Write a structured research paper about: {topic}

# Research Insights:
# {analysis_text}

# Criticism:
# {critique_text}

# Defense:
# {defense_text}
# """
#     )

#     final_report = report.messages[-1].content

#     logger.info("Writer agent generated final research report")

#     # STEP 7: Citations
#     logger.info("Generating citations")

#     citations = generate_citations(urls)

#     logger.info("Generated %d citations", len(citations))

#     # STEP 8: PDF
#     logger.info("Generating PDF report")

#     generate_pdf(
#         title=topic,
#         content=final_report,
#         citations=citations,
#         filename="report/research_report.pdf",
#     )

#     logger.info("PDF report generated successfully")

#     print("\nResearch paper generated successfully.")


# if __name__ == "__main__":
#     asyncio.run(main())


# main.py
import asyncio
from config.logger import get_logger
from pipeline.research_orchestrator import run_research

logger = get_logger("CLI_Main")

async def main():
    topic = input("Enter research topic: ").strip()
    if not topic:
        print("Topic cannot be empty!")
        return

    logger.info(f"CLI user started research for topic: {topic}")
    result = await run_research(topic)

    print("\n--- Research Plan ---\n")
    print(result["plan"])

    print("\n--- Analysis ---\n")
    print(result["analysis"])

    print("\n--- Critique ---\n")
    print(result["critique"])

    print("\n--- Defense ---\n")
    print(result["defense"])

    print("\n--- Final Report ---\n")
    print(result["report"])

    print("\n--- Citations ---\n")
    for c in result["citations"]:
        print(c)

    print(f"\nPDF report saved at: {result['pdf_path']}")
    logger.info(f"CLI research completed for topic: {topic}")

if __name__ == "__main__":
    asyncio.run(main())