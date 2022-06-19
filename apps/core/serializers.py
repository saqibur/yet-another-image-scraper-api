from rest_framework.serializers import Serializer

from apps.core.models import BaseModel


class BaseModelSerializer(Serializer):
    class Meta:
        models = BaseModel
        exclude = [
            "id",
        ]
