import hashlib
from datetime import date

import requests
from django.core.cache import cache


class WeatherAPIClient:
    BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"

    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(
        self, location: str, start_date=None, end_date=None, unit_group="metric"
    ):
        cache_key = self.generate_cache_key(location, start_date, end_date, unit_group)
        cached_data = cache.get(cache_key)

        if cached_data:
            return cached_data

        date_range = start_date or date.today()
        if end_date:
            date_range = f"{start_date}/{end_date}"

        url = f"{self.BASE_URL}/{location}/{date_range}/"

        params = {
            "key": self.api_key,
            "unitGroup": unit_group,
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            cache.set(cache_key, data, timeout=3600)
            return data
        except requests.exceptions.RequestException:
            raise Exception(f"Failed to fetch weather data for {location}.")

    def generate_cache_key(self, location, start_date, end_date, unit_group):
        raw_key = f"{location}:{start_date}:{end_date}:{unit_group}"

        return hashlib.md5(raw_key.encode()).digest()
