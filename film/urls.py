from rest_framework.routers import DefaultRouter
from django.urls import path, include

from film.views import FilmViewSet

router = DefaultRouter()
router.register("films", FilmViewSet, basename="user"),

urlpatterns = [path("", include(router.urls))]

app_name = "films"
