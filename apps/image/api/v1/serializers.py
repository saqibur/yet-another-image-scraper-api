from rest_framework.serializers import ModelSerializer

from apps.image.models import (
    ImageVariant,
    ScrapedImage,
)


class ImageVariantModelSerializer(ModelSerializer):
    class Meta:
        model = ImageVariant
        exclude = [
            "id",
            "scraped_image",
        ]


class ScrapedImageModelSerializer(ModelSerializer):
    image_variants = ImageVariantModelSerializer(
        source="image_variant", many=True, read_only=True, required=False
    )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.image != "":
            representation["name"] = instance.image.name
            representation["width"] = instance.image.width
            representation["height"] = instance.image.height
        return representation

    class Meta:
        model = ScrapedImage
        exclude = [
            "id",
        ]
