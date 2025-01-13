import requests
from datetime import date


class WeatherAPIClient:
    BASE_URL = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"

    def __init__(self, api_key):
        self.api_key = api_key

    def get_weather(
        self, location: str, start_date=None, end_date=None, unit_group="metric"
    ):
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
            return response.json()
        except requests.exceptions.RequestException:
            raise Exception(f"Failed to fetch weather data for {location}.")
