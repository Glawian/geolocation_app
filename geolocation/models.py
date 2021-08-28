from django.db import models

class Geolocation(models.Model):
    ip = models.CharField(max_length=15)
    continent_name = models.CharField(max_length=15)
    country_name = models.CharField(max_length=50)
    region_name = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=15)
    latitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
