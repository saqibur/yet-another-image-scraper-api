import os

from django.conf import settings
from django.conf.urls.static import static
from django.urls import (
    include,
    path,
)
from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

app_label = "apps.core"


def swagger_api_urlpatterns():
    schema_view = get_schema_view(
        openapi.Info(
            title="Yet Another Image Scraper API",
            default_version="v1",
            description="A minimal API used for scraping images from URLs",
            license=openapi.License(name="MIT License"),
        ),
        public=True,
        permission_classes=[permissions.AllowAny],
    )
    swagger_url = []

    if settings.DEBUG == True:
        swagger_url += [
            path("docs/swagger/", schema_view.with_ui("swagger", cache_timeout=0)),
            path("docs/redoc/", schema_view.with_ui("redoc", cache_timeout=0)),
        ]
    return swagger_url


urlpatterns = [
    path("", include("apps.image.urls", "image")),
    path("", include("apps.scraper.urls", "scraper")),
] + (
    static(settings.MEDIA_URL, document_root=os.path.join(settings.BASE_DIR, "media"))
    + swagger_api_urlpatterns()
)
