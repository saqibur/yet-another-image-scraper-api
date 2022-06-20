from enum import Enum

API_V1 = "v1"

LOCAL_SERVER = "LOCAL"
DEVELOPMENT_SERVER = "DEVELOPMENT"

SCRAPED_IMAGE_LOCATION = "scraped_images"


class ImageFormat(Enum):
    JPEG = "jpeg"
    JPG = "jpg"
    PNG = "png"
    TIFF = "tiff"
    GIF = "gif"
    WEBP = "webp"
    MBP = "bmp"
    ICO = "ico"

    @classmethod
    def values(cls):
        return [member.value for _image_format, member in cls.__members__.items()]


class ImageSize(Enum):
    SMALL = 256
    MEDIUM = 1024
    LARGE = 2048

    @classmethod
    def values(cls):
        return [member.value for _image_size, member in cls.__members__.items()]


class StringifiedImageSize(Enum):
    SMALL = "small"
    MEDIUM = "medium"
    LARGE = "large"

    @classmethod
    def values(cls):
        return [member.value for _stringified_image_size, member in cls.__members__.items()]
