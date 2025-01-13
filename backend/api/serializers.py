from datetime import date
from rest_framework import serializers


class WeatherSerializer(serializers.Serializer):
    location = serializers.CharField(required=True, max_length=100)
    start_date = serializers.DateField(required=False, default=None)
    end_date = serializers.DateField(required=False, default=None)

    def raise_validation_error(self, message: str):
        raise serializers.ValidationError(message)

    def validate(self, attrs):
        if not attrs["location"]:
            self.raise_validation_error("Location field is required.")
        if attrs["start_date"] and attrs["start_date"] < date.today():
            self.raise_validation_error("Start Date should not be in the past.")
        if (
            attrs["end_date"]
            and attrs["start_date"]
            and (
                attrs["end_date"] < date.today()
                or attrs["end_date"] < attrs["start_date"]
            )
        ):
            self.raise_validation_error("End Date should not be in the past.")
        return super().validate(attrs)
