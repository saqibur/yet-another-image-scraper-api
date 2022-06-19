from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView

from apps.core.helpers import get_validated_data
from apps.image.models import ScrapedImage
from apps.scraper.api.v1.serializers import ScraperSerializer
from apps.scraper.api.v1.services import SingleSiteImageScraperService


class ScraperAPIView(APIView):
    serializer_class = ScraperSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        url_to_scrape = get_validated_data(self.serializer_class, request)["url"]

        scraper = SingleSiteImageScraperService(url_to_scrape)

        scrapped_images = [
            ScrapedImage(scraped_from=url_to_scrape, metadata={"origin": url})
            for url in scraper.image_urls
        ]

        # NOTE: We're ignoring duplicates in case we've already fetched an image;
        #       Therefore, we'll only be scraping new links that pop up.
        ScrapedImage.objects.bulk_create(scrapped_images, ignore_conflicts=True)

        return Response(
            f"Please come back later for your scraped images. URL: {url_to_scrape}",
            status=HTTP_200_OK,
        )
