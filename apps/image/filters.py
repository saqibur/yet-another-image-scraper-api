import django_filters.rest_framework as filters

from apps.image.models import ScrapedImage


class ScrapedImageFilter(filters.FilterSet):
    url = filters.CharFilter(
        field_name="scraped_from",
        lookup_expr="icontains",
        label="url",
    )
    size = filters.CharFilter(field_name="image_variant__size")

    class Meta:
        model = ScrapedImage
        exclude = [
            "id",
            "image",
            "metadata",
        ]
