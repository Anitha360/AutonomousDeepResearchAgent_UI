from tools.web_search import search_web
from tools.web_scraper import scrape_page
from tools.source_ranker import rank_sources
from memory.vector_store import VectorStore
from config.logger import get_logger

logger = get_logger("ResearchPipeline")

vector_store = VectorStore()


def run_autonomous_research(query: str):

    logger.info("Starting autonomous research for query: %s", query)

    logger.info("Searching the web for relevant sources")

    urls = search_web(query)

    logger.info("Total URLs found: %d", len(urls))

    documents = []

    for url in urls:

        logger.info("Scraping content from URL: %s", url)

        text = scrape_page(url)

        if text:

            logger.info(
                "Content successfully scraped. Length: %d characters",
                len(text)
            )

            logger.info("Storing document in vector memory")

            vector_store.add_document(text, url)

            documents.append(text)

        else:

            logger.warning(
                "Failed to extract content from URL: %s",
                url
            )

    logger.info("Total documents collected: %d", len(documents))

    logger.info("Ranking sources based on relevance")

    ranked_docs = rank_sources(documents)

    logger.info("Top ranked documents selected: %d", len(ranked_docs))

    logger.info("Autonomous research pipeline completed")

    return ranked_docs, urls