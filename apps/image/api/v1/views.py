from rest_framework.viewsets import ModelViewSet

from apps.image.api.v1.serializers import ScrapedImageModelSerializer
from apps.image.filters import ScrapedImageFilter


class ScrapedImageModelViewSet(ModelViewSet):
    serializer_class = ScrapedImageModelSerializer
    queryset = serializer_class.Meta.model.objects.all()
    filterset_class = ScrapedImageFilter
    lookup_field = "uuid"
    http_method_names = [
        "options",
        "head",
        "get",
    ]
