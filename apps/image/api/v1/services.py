import requests
import time

from django.conf import settings
from apps.image.models import ScrapedImage
from django.core.files.images import ImageFile
from io import BytesIO


class ScrapedImageService:
    @staticmethod
    def fetch_images_for_saved_urls():
        scraped_images = ScrapedImage.objects.filter(
            image="",
        )

        for scraped_image in scraped_images:
            try:
                response = requests.get(scraped_image.metadata["origin"])
                headers = response.headers

                scraped_image.image = ImageFile(
                    BytesIO(response.content),
                    scraped_image.metadata["origin"].split("/")[-1],
                )

                scraped_image.metadata.update(headers)
                scraped_image.save()
                time.sleep(settings.WAIT_PERIOD_BETWEEN_IMAGE_DOWNLOADS)
            except Exception as exn:
                print(exn)
