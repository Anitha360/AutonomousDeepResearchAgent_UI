import requests
from bs4 import BeautifulSoup
from config.logger import get_logger

logger = get_logger("Scraper Page")

def scrape_page(url: str) -> str:

    try:
        logger.info("Initialise web scraper")
        response = requests.get(url, timeout=10)

        soup = BeautifulSoup(response.text, "html.parser")

        paragraphs = soup.find_all("p")

        text = " ".join([p.get_text() for p in paragraphs])
        logger.info("Executed web scraper:" , text[:5000])
        return text[:5000]

    except:
        return ""