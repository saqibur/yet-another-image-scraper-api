from io import BytesIO
import time
import traceback

from django.conf import settings
from django.core.files.images import ImageFile

from PIL import Image
import requests

from apps.core.constants import (
    ImageSize,
    StringifiedImageSize,
)
from apps.image.models import (
    ImageVariant,
    ScrapedImage,
)


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

                image = ImageFile(
                    BytesIO(response.content),
                    scraped_image.metadata["origin"].split("/")[-1],
                )

                ImageVariantService.create_image_variants_for_image(
                    scraped_image,
                    image,
                )

                scraped_image.image = image
                scraped_image.metadata.update(headers)
                scraped_image.save()
                time.sleep(settings.WAIT_PERIOD_BETWEEN_IMAGE_DOWNLOADS)
            except Exception as exn:
                traceback.print_exc()
                print(exn)


class ImageVariantService:
    @staticmethod
    def create_image_variants_for_image(scraped_image, image):
        def _save_image_variation(image_size, stringified_image_size):
            output_size = (image_size.value, image.height)
            image_variant = Image.open(image.file)
            image_variant.thumbnail(output_size)

            in_memory_thumbnail = BytesIO()
            image_variant.save(in_memory_thumbnail, image.name.split(".")[-1])
            in_memory_thumbnail.seek(0)

            ImageVariant.objects.create(
                scraped_image=scraped_image,
                image=ImageFile(
                    in_memory_thumbnail,
                    f"{stringified_image_size.value}/{image.name}",
                ),
                size=stringified_image_size.value,
            )

        if image.width > ImageSize.SMALL.value:
            _save_image_variation(ImageSize.SMALL, StringifiedImageSize.SMALL)
        if image.width > ImageSize.MEDIUM.value:
            _save_image_variation(ImageSize.MEDIUM, StringifiedImageSize.MEDIUM)
        if image.width > ImageSize.LARGE.value:
            _save_image_variation(ImageSize.LARGE, StringifiedImageSize.LARGE)
