from django.db.models import (
    CharField,
    ForeignKey,
    ImageField,
    JSONField,
    TextChoices,
    URLField,
    CASCADE,
)

from apps.core.constants import (
    StringifiedImageSize,
    SCRAPED_IMAGE_LOCATION,
)
from apps.core.models import BaseModel


class ImageSize(TextChoices):
    SMALL = StringifiedImageSize.SMALL.value
    MEDIUM = StringifiedImageSize.MEDIUM.value
    LARGE = StringifiedImageSize.LARGE.value


class ScrapedImage(BaseModel):
    scraped_from = URLField(
        verbose_name="URL scraped from",
        db_column="scraped_from",
    )

    metadata = JSONField(
        verbose_name="Image metadata",
        db_column="metadata",
        blank=True,
        null=True,
    )

    image = ImageField(
        verbose_name="Image",
        db_column="image",
        upload_to=f"{SCRAPED_IMAGE_LOCATION}/",
    )

    @property
    def is_scraped(self):
        return True if self.image else False

    @property
    def scraped_at(self):
        return self.modified_at

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Scraped image"
        verbose_name_plural = "Scraped images"
        db_table = "scraped_image"


class ImageVariant(BaseModel):
    scraped_image = ForeignKey(
        to="image.ScrapedImage",
        verbose_name="Scraped image",
        db_column="scraped_image",
        related_name="image_variant",
        on_delete=CASCADE,
    )

    size = CharField(
        max_length=10,
        verbose_name="Image size",
        db_column="size",
        choices=ImageSize.choices,
    )

    image = ImageField(
        verbose_name="Image",
        db_column="image",
        upload_to=f"{SCRAPED_IMAGE_LOCATION}/",
    )
