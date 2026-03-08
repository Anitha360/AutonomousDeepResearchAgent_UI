# import requests
# from bs4 import BeautifulSoup
# from config.logger import get_logger

# logger = get_logger("WebScraper")

# def scrape_page(url: str) -> str:
#     logger.info("Starting scrape for URL: %s", url)

#     try:
#         logger.info("Sending HTTP request")
#         response = requests.get(url, timeout=10)
        
#         logger.info("Received response with status code: %s", response.status_code)

#         soup = BeautifulSoup(response.text, "html.parser")

#         paragraphs = soup.find_all("p")
#         if not paragraphs:
#             logger.warning("No paragraph content found on page: %s", url)

#         text = " ".join([p.get_text() for p in paragraphs])
        
#         logger.info("Extracted %d paragraphs from page", len(paragraphs))
#         cleaned_text = text[:5000]

#         logger.info("Returning scraped content (truncated to 5000 characters)")

#         return cleaned_text

#     except Exception as e:

#         logger.error("Error scraping URL: %s | Error: %s", url, str(e))

#         return ""

import requests
from bs4 import BeautifulSoup
from config.logger import get_logger
import time

logger = get_logger("WebScraper")


def scrape_page(url: str, retries: int = 3, backoff_factor: float = 0.5) -> str:
    """
    Scrape text content from a webpage, with retries and logging.
    
    :param url: URL to scrape
    :param retries: Number of retry attempts for network failures
    :param backoff_factor: Exponential backoff factor for retries
    :return: Extracted text (truncated to 5000 chars)
    """
    headers = {"User-Agent": "Mozilla/5.0 (compatible; WebScraper/1.0)"}

    attempt = 0
    while attempt < retries:
        try:
            logger.info("Scraping URL: %s (attempt %d)", url, attempt + 1)
            response = requests.get(url, headers=headers, timeout=10)
            
            if not response.ok:
                raise Exception(f"Bad response: {response.status_code}")

            soup = BeautifulSoup(response.text, "html.parser")
            paragraphs = soup.find_all("p")

            if not paragraphs:
                logger.warning("No paragraph content found on page: %s", url)

            text = " ".join([p.get_text() for p in paragraphs])
            cleaned_text = text[:5000]  # truncate to 5000 chars
            logger.info("Successfully extracted %d paragraphs", len(paragraphs))

            return cleaned_text

        except Exception as e:
            attempt += 1
            wait_time = backoff_factor * (2 ** (attempt - 1))
            logger.warning(
                "Error scraping URL (attempt %d/%d): %s. Retrying in %.1f seconds...",
                attempt, retries, str(e), wait_time
            )
            time.sleep(wait_time)

    logger.error("Failed to scrape URL after %d attempts: %s", retries, url)
    return ""