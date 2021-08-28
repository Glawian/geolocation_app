from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from geolocation.serializers import GeolocationSerializer
from geolocation.models import Geolocation


class GeolocationViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Geolocation.objects.all()
    serializer_class = GeolocationSerializer
