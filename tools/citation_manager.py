from config.logger import get_logger

logger = get_logger("Citations")
def generate_citations(urls):
    logger.info("Initilize Citations")

    citations = []

    for i, url in enumerate(urls):

        citations.append(f"[{i+1}] {url}")

    logger.info("Executed Ciation", citations)
    return citations