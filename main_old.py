import asyncio

from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console

from agents.planner_agent import create_planner
from agents.researcher_agent import create_researcher
from agents.analyst_agent import create_analyst
from agents.critic_agent import create_critic
from agents.defender_agent import create_defender
from agents.writer_agent import create_writer

from pipeline.autonomous_research_pipeline import run_autonomous_research
from tools.citation_manager import generate_citations
from report.pdf_generator import generate_pdf


async def main():

    planner = create_planner()
    researcher = create_researcher()
    analyst = create_analyst()
    critic = create_critic()
    defender = create_defender()
    writer = create_writer()

    team = RoundRobinGroupChat(
        [
            planner,
            researcher,
            analyst,
            critic,
            defender,
            writer,
        ],
        max_turns=12,
    )

    topic = input("Enter research topic: ")

    # Run agent discussion
    await Console(
        team.run_stream(
            task=f"Conduct deep research on the topic: {topic}"
        )
    )

    # Run the autonomous research pipeline
    documents, urls = run_autonomous_research(topic)

    # Generate citations
    citations = generate_citations(urls)

    # Combine documents into a report
    research_content = "\n\n".join(documents)

    # Generate PDF
    generate_pdf(
        title=topic,
        content=research_content,
        citations=citations,
        filename="report/research_report.pdf",
    )


if __name__ == "__main__":
    asyncio.run(main())