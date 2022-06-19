from django.urls import path
from rest_framework.routers import SimpleRouter

from apps.image.api.v1.views import ScrapedImageModelViewSet

router = SimpleRouter()
router.register("", ScrapedImageModelViewSet)

urlpatterns = [] + router.urls
