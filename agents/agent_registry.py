from agents.planner_agent import create_planner
from agents.analyst_agent import create_analyst
from agents.critic_agent import create_critic
from agents.defender_agent import create_defender
from agents.writer_agent import create_writer
from config.logger import get_logger

logger = get_logger("Agent Registry")


def get_agents():
    logger.info("Agent Registry initialised")

    return {
        "planner": create_planner(),
        "analyst": create_analyst(),
        "critic": create_critic(),
        "defender": create_defender(),
        "writer": create_writer()
    }