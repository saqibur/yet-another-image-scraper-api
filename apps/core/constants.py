from enum import Enum

API_V1 ="v1"

LOCAL_SERVER = "LOCAL"
DEVELOPMENT_SERVER = "DEVELOPMENT"


class ImageSize(Enum):
    SMALL = 256
    MEDIUM = 1024
    LARGE = 2048

    @classmethod
    def values(cls):
        return [member.value for _image_size, member in cls.__members__.items()]
