from autogen_agentchat.agents import AssistantAgent
from config.model_client import get_model_client
from config.logger import get_logger

logger = get_logger("critic")

def create_critic():
    logger.info("Initialize Critic")
    critic = AssistantAgent(
        name="critic",
        model_client=get_model_client(),
        system_message="""
You review the research.

Check:
- missing information
- weak arguments
- research quality
"""
    )
    logger.info("Completed Critic")
    return critic