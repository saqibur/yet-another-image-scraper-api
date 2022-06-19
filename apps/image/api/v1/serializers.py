from rest_framework.serializers import (
    CharField,
    IntegerField,
    ModelSerializer,
)

from apps.image.models import ScrapedImage


class ScrapedImageModelSerializer(ModelSerializer):
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.image != "":
            representation['name'] = instance.image.name
            representation['width'] = instance.image.width
            representation['height'] = instance.image.height
        return representation

    class Meta:
        model = ScrapedImage
        exclude = [
            "id",
        ]
