from django.urls import (
    include,
    path,
)

from apps.core.constants import API_V1


app_name = "scraper"

urlpatterns = [
    path(
        f"{API_V1}/scrapers/",
        include(("apps.scraper.api.v1.urls", API_V1), namespace=API_V1),
    ),
]
