def rank_sources(documents):

    ranked = sorted(
        documents,
        key=lambda x: len(x),
        reverse=True
    )

    return ranked[:3]