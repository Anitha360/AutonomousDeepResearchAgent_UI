from ddgs import DDGS
from typing import List

def search_web(query: str) -> List[str]:

    urls = []

    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=5):
            urls.append(r["href"])

    return urls