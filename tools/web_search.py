from ddgs import DDGS
from typing import List
from config.logger import get_logger

logger = get_logger("Web Search")

def search_web(query: str) -> List[str]:
    logger.info("Initialize Web search")
    urls = []

    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=5):
            urls.append(r["href"])
            
    logger.info("Executed web search", urls)
    return urls