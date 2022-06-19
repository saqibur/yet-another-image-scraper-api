from dataclasses import field
import django_filters.rest_framework as filters

from apps.image.models import ScrapedImage


class ScrapedImageFilter(filters.FilterSet):
    url = filters.CharFilter(field_name="scraped_from", label="url")

    class Meta:
        model = ScrapedImage
        exclude = [
            "id",
            "image",
            "metadata",
        ]