import requests
from bs4 import BeautifulSoup
from apps.core.constants import ImageFormat


class SingleSiteImageScraperService:
    """
    A simple scraper that finds all image tags in a given URL and extracts
    all images.
    """

    HTML_PARSER = "html.parser"
    IMAGE_TAG = "img"

    def __init__(self, site_url):
        self.site_url = site_url if site_url.endswith("/") else site_url + "/"

        soup = BeautifulSoup(requests.get(site_url).text, SingleSiteImageScraperService.HTML_PARSER)
        image_tags = soup.find_all(SingleSiteImageScraperService.IMAGE_TAG)

        self.image_urls = self._normalize_urls([tag["src"] for tag in image_tags])

    def _normalize_urls(self, image_urls):
        normalized_urls = []

        for image_url in image_urls:
            if image_url.endswith(tuple(ImageFormat.values())):
                if not image_url.startswith(("http", "https")):
                    image_url = f"{self.site_url}{image_url}"

                normalized_urls.append(image_url)

        return normalized_urls
