from typing import List
import inject

from app.exceptions import DataFetchError
from app.interfaces.dtos.amazon_product_snapshot import AmazonProductSnapshot
from integrations.amazon_search.formatters import format_search
from integrations.constants import HttpMethodEnum
from integrations.retriable_http_client import RetriableHttpClient


class AmazonSearchClient:
    """
    A client for interacting with the Amazon search page.
    """

    @inject.autoparams()
    def __init__(self, http_client: RetriableHttpClient):
        self.http_client = http_client
        self.base_uri = "https://www.amazon.com"

    def search(self, keyword: str) -> str:
        """
        Searches Amazon for a keyword.

        Args:
            keyword (str): The keyword to search for.

        Returns:
            str: The HTML of the search results page.
        """
        uri = f"{self.base_uri}/s?k={keyword}"

        headers = {
            "authority": "www.amazon.com",
            "pragma": "no-cache",
            "cache-control": "no-cache",
            "dnt": "1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
        }

        response = self.http_client.request(HttpMethodEnum.GET, uri, headers=headers)

        if response.status_code != 200:
            raise DataFetchError(
                f"Failed request to '{uri}': {response.text} - {response.status_code}"
            )

        return response.text

    def get_products_for_keyword(self, keyword: str) -> List[AmazonProductSnapshot]:
        """
        Searches Amazon for a keyword and returns a list of products.

        Args:
            keyword (str): The keyword to search for.

        Returns:
            list: A list of products.
        """
        html = self.search(keyword)
        return format_search(html)
