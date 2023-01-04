from rest_framework.routers import DefaultRouter

from space.views import SpaceViewSet

router = DefaultRouter()
router.register("space", SpaceViewSet, basename="space")

urlpatterns = router.urls
