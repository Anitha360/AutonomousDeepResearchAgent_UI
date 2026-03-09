from tools.web_search import search_web
from tools.web_scraper import scrape_page
from tools.source_ranker import rank_sources
from memory.vector_store import VectorStore
from config.logger import get_logger

logger = get_logger("Autonomous Research Pipeline")

vector_store = VectorStore()

def run_autonomous_research(query: str):
    logger.info("run_autonomous_research")
    
    urls = search_web(query)

    documents = []

    for url in urls:

        text = scrape_page(url)

        if text:

            vector_store.add_document(text, url)

            documents.append(text)

    ranked_docs = rank_sources(documents)
    
    logger.info("run_autonomous_research: Ranked docs, urls:", ranked_docs, urls)
    return ranked_docs, urls