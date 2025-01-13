from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import WeatherSerializer

# Create your views here.
class WeatherAPIView(generics.GenericAPIView):
    serializer_class = WeatherSerializer
    
    def get(self, request):
        serializer = WeatherSerializer(data=request.query_params)
        if not serializer.is_valid():
            return Response({'error': serializer.error_messages}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message':'Your API work correctly'}, status=status.HTTP_200_OK)
    

weather_api_view = WeatherAPIView.as_view()