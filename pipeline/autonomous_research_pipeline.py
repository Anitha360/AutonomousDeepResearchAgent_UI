from tools.web_search import search_web
from tools.web_scraper import scrape_page
from tools.source_ranker import rank_sources
from memory.vector_store import VectorStore

vector_store = VectorStore()

def run_autonomous_research(query: str):

    urls = search_web(query)

    documents = []

    for url in urls:

        text = scrape_page(url)

        if text:

            vector_store.add_document(text, url)

            documents.append(text)

    ranked_docs = rank_sources(documents)

    return ranked_docs, urls