from autogen_agentchat.agents import AssistantAgent
from config.model_client import get_model_client
from config.logger import get_logger

logger = get_logger("defender")

def create_defender():
    logger.info("Defender Initiated")
    defender = AssistantAgent(
        name="defender",
        model_client=get_model_client(),
        system_message="""
You defend the research paper against criticism.

Respond to critic arguments and strengthen the research reasoning.
Provide evidence and justification.
"""
    )
    logger.info("Defender successfully completed")
    return defender