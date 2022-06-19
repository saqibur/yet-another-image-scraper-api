from PIL import Image

from django.core.management.base import BaseCommand
from apps.core.decorators import restrict_command_to_development_environment
from apps.core.constants import ImageSize

from random import randint, choice
from faker import Faker
from io import BytesIO
from django.core.files.images import ImageFile


from apps.image.models import ScrapedImage


class Command(BaseCommand):
    help = "Generates initial data for the application for demo-ing"

    def add_arguments(self, parser):
        parser.add_argument("count", type=int)

    @restrict_command_to_development_environment
    def handle(self, *args, **kwargs):
        count = kwargs["count"]

        fake = Faker()
        sizes = ImageSize.values()
        scraped_images = []

        for _ in range(count):
            fake_file_path = fake.file_path(depth=randint(0, 5), category="image")
            fake_domain = fake.domain_name(randint(1, 3))

            extension = fake_file_path.split(".")[-1]
            extension = "JPEG" if extension.lower() == "jpg" else extension.upper()

            filename = fake_file_path.split("/")[-1]

            fake_image = fake.image(
                size=(choice(sizes), choice(sizes)),
                image_format=extension,
            )

            scraped_images.append(
                ScrapedImage(
                    image=ImageFile(BytesIO(fake_image), name=filename),
                    scraped_from=f"https://{fake_domain}{'/'.join(fake_file_path.split('/')[:-1])}",
                )
            )

        ScrapedImage.objects.bulk_create(scraped_images)

        self.stdout.write(self.style.SUCCESS(f"Completed seeding script for scraped images."))
