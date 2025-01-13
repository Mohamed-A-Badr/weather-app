from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import WeatherSerializer
from .services.weather_api import WeatherAPIClient


# Create your views here.
class WeatherAPIView(generics.GenericAPIView):
    serializer_class = WeatherSerializer

    def get(self, request):
        serializer = WeatherSerializer(data=request.query_params)
        if not serializer.is_valid():
            return Response(
                {"error": serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST
            )
        client = WeatherAPIClient(settings.WEATHER_API_KEY)
        data = serializer.validated_data
        try:
            weather_date = client.get_weather(
                location=data["location"],
                start_date=data["start_date"],
                end_date=data["end_date"],
            )
            return Response(weather_date, status=status.HTTP_200_OK)
        except KeyError as err:
            return Response(
                {"error": f"Missing required field: {err}"}, status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


weather_api_view = WeatherAPIView.as_view()
