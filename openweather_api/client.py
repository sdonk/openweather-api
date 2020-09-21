import requests

from openweather_api.core import ClientCore


class APIClient(ClientCore):

    endpoints = {
        'current_weather_data': 'weather'
    }

    def get_current_weather_by_city_name(self, city: str) -> requests.Response:
        endpoint = self.endpoints['current_weather_data']
        params = {
            'q': city
        }
        return self.get(endpoint=endpoint, params=params)

    def get_current_weather_by_city_id(self, city_id: str) -> str:
        pass