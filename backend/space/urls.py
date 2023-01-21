from rest_framework.routers import DefaultRouter

from space.views import SpaceViewSet, SlotViewSet

router = DefaultRouter()
router.register("space", SpaceViewSet, basename="space")
router.register("slot", SlotViewSet, basename="slot")

urlpatterns = router.urls
