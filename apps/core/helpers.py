from rest_framework.serializers import Serializer
from rest_framework.request import Request


def create_validated_instance(serializer: Serializer, request: Request):
    serializer = serializer(data=request.data, context={"request": request})
    serializer.is_valid(raise_exception=True)
    return serializer.save(), serializer.validated_data


def get_validated_data(
    serializer: Serializer,
    request: Request,
):
    serializer = serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    return serializer.validated_data
