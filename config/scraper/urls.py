from django.urls import path
from .views import run_scraper

urlpatterns = [
    path("", run_scraper),
]