from config.logger import get_logger

logger = get_logger("SourceRanker")

def rank_sources(documents):
    logger.info("Source ranking started")

    logger.info("Total documents received for ranking: %d", len(documents))
    if not documents:
        logger.warning("No documents received for ranking")
        return []

    ranked = sorted(
        documents,
        key=lambda x: len(x),
        reverse=True
    )
    
    
    logger.info("Documents ranked based on content length")

    top_sources = ranked[:3]

    logger.info("Top %d sources selected for further analysis", len(top_sources))

    return top_sources