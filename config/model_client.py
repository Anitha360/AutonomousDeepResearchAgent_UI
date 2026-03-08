# from autogen_ext.models.openai import OpenAIChatCompletionClient
# from config.logger import get_logger

# logger = get_logger("ModelClient")


# def get_model_client():
#     logger.info("Initializing model client")
    
#     try:

#         model_name = "qwen2.5:7b"

#         logger.info("Loading model: %s", model_name)

#         client = OpenAIChatCompletionClient(
#             model=model_name,
#             base_url="http://localhost:11434/v1",
#             api_key="ollama",

#             model_info={
#                 "vision": False,
#                 "function_calling": True,
#                 "json_output": True,
#                 "structured_output": False,
#                 "family": "qwen",
#             },

#             temperature=0.7,
#         )

#         logger.info("Model client initialized successfully")

#         return client

#     except Exception as e:

#         logger.error("Failed to initialize model client: %s", str(e))

#         raise

from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.logger import get_logger
import time

logger = get_logger("ModelClient")


def get_model_client(retries: int = 5, backoff_factor: float = 0.5):
    """
    Initialize Ollama on-prem model client with retry logic.
    
    :param retries: Number of retries if initialization fails
    :param backoff_factor: Multiplier for exponential backoff
    :return: OpenAIChatCompletionClient instance
    """
    model_name = "qwen2.5:7b"
    logger.info("Initializing model client for model: %s", model_name)

    attempt = 0
    while attempt < retries:
        try:
            client = OpenAIChatCompletionClient(
                model=model_name,
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
                request_timeout=30  # optional: set timeout for local server
            )
            logger.info("Model client initialized successfully")
            return client

        except Exception as e:
            attempt += 1
            wait_time = backoff_factor * (2 ** (attempt - 1))
            logger.warning(
                "Failed to initialize model client (attempt %d/%d): %s. Retrying in %.1f seconds...",
                attempt, retries, str(e), wait_time
            )
            time.sleep(wait_time)

    # If all retries fail, raise error
    logger.error("Failed to initialize model client after %d attempts", retries)
    raise Exception(f"Cannot initialize Ollama client for {model_name}")