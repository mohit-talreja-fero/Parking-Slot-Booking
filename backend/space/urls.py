from rest_framework.routers import DefaultRouter
from django.urls import path, include
from space.views import SpaceViewSet, SlotViewSet

router = DefaultRouter()
router.register("space", SpaceViewSet, basename="space")
router.register("slot", SlotViewSet, basename="slot")

urlpatterns = [
    # path(r'^tellme/', include("tellme.urls")),
]


urlpatterns += router.urls
