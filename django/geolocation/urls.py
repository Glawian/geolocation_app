from rest_framework import routers
from geolocation.views import GeolocationViewSet

router = routers.DefaultRouter()
router.register(r'geolocation', GeolocationViewSet, basename='geolocation')
urlpatterns = router.urls
