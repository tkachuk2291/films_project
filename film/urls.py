from rest_framework.routers import DefaultRouter
from django.urls import path, include

router = DefaultRouter()
router.register("films", UserWineViewSet, basename="user"),

urlpatterns = [path("", include(router.urls))]

app_name = "films"
