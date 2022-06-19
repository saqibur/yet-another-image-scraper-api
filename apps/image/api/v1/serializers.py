from rest_framework.serializers import ModelSerializer

from apps.image.models import ScrapedImage

class ScrapedImageModelSerializer(ModelSerializer):
    class Meta:
        model = ScrapedImage
        exclude = [
            "id",
        ]
