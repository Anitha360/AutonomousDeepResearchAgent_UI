def generate_citations(urls):

    citations = []

    for i, url in enumerate(urls):

        citations.append(f"[{i+1}] {url}")

    return citations