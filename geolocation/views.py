from rest_framework import viewsets

from geolocation.serializers import GeolocationSerializer
from geolocation.models import Geolocation


class GeolocationViewSet(viewsets.ModelViewSet):
    queryset = Geolocation.objects.all()
    serializer_class = GeolocationSerializer