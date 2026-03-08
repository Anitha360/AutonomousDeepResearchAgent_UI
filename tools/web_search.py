from ddgs import DDGS
from typing import List
from config.logger import get_logger

logger = get_logger("WebSearch")


def search_web(query: str) -> List[str]:

    logger.info("Starting web search for query: %s", query)

    urls = []

    try:

        with DDGS() as ddgs:

            logger.info("Sending search request to DuckDuckGo")

            for r in ddgs.text(query, max_results=5):

                url = r.get("href")

                if url:

                    logger.info("Search result found: %s", url)

                    urls.append(url)

        logger.info("Web search completed. Total URLs collected: %d", len(urls))

    except Exception as e:

        logger.error(
            "Web search failed for query: %s | Error: %s",
            query,
            str(e)
        )

    return urls