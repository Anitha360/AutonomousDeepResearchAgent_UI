from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.logger import get_logger

logger = get_logger("ModelClient")

def get_model_client():
    logger.info("Initialize ModelClient")
    return OpenAIChatCompletionClient(
        model="qwen2.5:7b",
        base_url="http://localhost:11434/v1",
        api_key="ollama",

        model_info={
            "vision": False,
            "function_calling": True,
            "json_output": True,
            "structured_output": False,
            "family": "qwen",
        },

        temperature=0.7,
    )