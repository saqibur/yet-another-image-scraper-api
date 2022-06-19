from django.db.models import ImageField, URLField, JSONField

from apps.core.models import BaseModel


class ScrapedImage(BaseModel):
    SCRAPED_IMAGE_LOCATION = "scraped_images"

    image = ImageField(
        verbose_name="Image",
        db_column="image",
        upload_to=f"{SCRAPED_IMAGE_LOCATION}/",
    )

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
