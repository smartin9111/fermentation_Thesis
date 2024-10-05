from rest_framework import serializers
from api.models import Fermentation, TemperatureMeasurement

class FermentationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fermentation
        fields = '__all__'

class TemperatureMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureMeasurement
        fields = '__all__'
