from config.logger import get_logger

logger = get_logger("Rank Sources")
def rank_sources(documents):
    logger.info("Ranked Source initialised")
    ranked = sorted(
        documents,
        key=lambda x: len(x),
        reverse=True
    )

    logger.info("Rank source executed:", ranked[3])
    return ranked[:3]