from rest_framework import serializers

from geolocation.models import Geolocation
from geolocation.geolocation_api import GeolocationApi

class GeolocationGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geolocation
        fields = '__all__'

class GeolocationPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geolocation
        fields = ['ip']
    
    def create(self, validated_data):
        api = GeolocationApi()
        model_data = api.get_model_data(validated_data.get('customer'))
        return Geolocation.objects.create(**model_data)
        