from autogen_agentchat.agents import AssistantAgent
from config.model_client import get_model_client
from config.logger import get_logger

logger = get_logger("Analyst")

def create_analyst():
    logger.info("Initialise Analyst")
    analyst = AssistantAgent(
        name="analyst",
        model_client=get_model_client(),
        system_message="""
You analyze research information.

Identify patterns, trends, and key insights.
"""
    )
    logger.info("Completed Analyst")
    return analyst