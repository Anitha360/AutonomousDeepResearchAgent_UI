from config.logger import get_logger

logger = get_logger("CitationManager")

def generate_citations(urls):
    logger.info("Citation generation started")

    citations = []

    for i, url in enumerate(urls):
        logger.info("Processing source %d: %s", i + 1, url)
        citations.append(f"[{i+1}] {url}")
        
    logger.info("Citation generation completed. Total citations: %d", len(citations))
    return citations