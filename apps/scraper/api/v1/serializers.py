from rest_framework.serializers import (
    Serializer,
    URLField,
)


class ScraperSerializer(Serializer):
    url = URLField(required=True)
