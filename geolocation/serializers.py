from rest_framework import serializers
from geolocation.models import Geolocation

class GeolocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geolocation
        fields = ['id', 'ip', 'continent_name', 'country_name', 'region_name', 'city', 'zip_code', 'latitude', 'longitude']
