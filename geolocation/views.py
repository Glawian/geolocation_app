from rest_framework import viewsets

from geolocation.serializers import GeolocationGetSerializer, GeolocationPostSerializer
from geolocation.models import Geolocation


class GeolocationViewSet(viewsets.ModelViewSet):
    def get_serializer_class(self):
        if self.action == 'create':
            return GeolocationPostSerializer
        return GeolocationGetSerializer
    queryset = Geolocation.objects.all()
