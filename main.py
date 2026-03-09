import asyncio

from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.ui import Console

from agents.planner_agent import create_planner
from agents.researcher_agent import create_researcher
from agents.analyst_agent import create_analyst
from agents.critic_agent import create_critic
from agents.writer_agent import create_writer


async def main():

    planner = create_planner()
    researcher = create_researcher()
    analyst = create_analyst()
    critic = create_critic()
    writer = create_writer()

    team = RoundRobinGroupChat(
        [
            planner,
            researcher,
            analyst,
            critic,
            writer,
        ],
        max_turns=12,
    )

    topic = input("Enter research topic: ")

    await Console(
        team.run_stream(
            task=f"Conduct deep research on the topic: {topic}"
        )
    )


if __name__ == "__main__":

    asyncio.run(main())