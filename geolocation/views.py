from rest_framework import response, viewsets
from rest_framework.permissions import IsAuthenticated

from geolocation.serializers import GeolocationGetSerializer, GeolocationPostSerializer
from geolocation.models import Geolocation


class GeolocationViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated, )
    def get_serializer_class(self):
        if self.action == 'create':
            return GeolocationPostSerializer
        return GeolocationGetSerializer
    queryset = Geolocation.objects.all()
