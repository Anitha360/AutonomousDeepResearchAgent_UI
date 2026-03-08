from autogen_agentchat.agents import AssistantAgent
from config.model_client import get_model_client
from config.logger import get_logger

logger = get_logger("Critic")

def create_critic():
    logger.info("Critic agent initialised")

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
    logger.info("Critic agent successfully completed")
    return critic