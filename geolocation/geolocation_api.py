import os
import requests
from typing import Dict

class GeolocationApi(object):
    def __init__(self):
        self.base_url = 'http://api.ipstack.com/'
        self.token = os.environ['API_TOKEN']
    
    def get_model_data(self, ip: str) -> Dict:
        geolocation_data = self._get_geolocation_data(ip)
        return {
            'ip': ip,
            'continent_name': geolocation_data['continent_name'],
            'country_name': geolocation_data['country_name'],
            'region_name': geolocation_data['region_name'],
            'city': geolocation_data['city'],
            'zip_code': geolocation_data['zip_code'],
            'latitude': geolocation_data['latitude'],
            'longitude': geolocation_data['longitude'],
        }

    def _get_geolocation_data(self, ip: str) -> Dict:

        params = {'access_key': self.token, 'fields': 'main'}
        url = self.base_url + ip

        return requests.get(url, params).json()
