from django.urls import path

from apps.scraper.api.v1.views import ScraperAPIView


app_name = "scraper"

urlpatterns = [
    path("scrape-url/", ScraperAPIView.as_view()),
]
