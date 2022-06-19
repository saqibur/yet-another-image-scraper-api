from django.urls import (
    include,
    path,
)

from apps.core.constants import API_V1


app_name = "image"

urlpatterns = [
    path(
        f"{API_V1}/images/",
        include(("apps.image.api.v1.urls", API_V1), namespace=API_V1),
    ),
]
