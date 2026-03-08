from autogen_agentchat.agents import AssistantAgent
from config.model_client import get_model_client
from config.logger import get_logger

logger = get_logger("PlannerAgent")

def create_planner():
    
    logger.info("Initializing Planner Agent")

    planner = AssistantAgent(
        name="planner",
        model_client=get_model_client(),
        system_message="""
You are a research planner.

Break the research problem into structured tasks.
Create a research plan and key questions.
"""
    )
    logger.info("Planner Agent successfully created")
    return planner