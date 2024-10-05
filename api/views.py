from rest_framework import viewsets
from api.models import Fermentation, TemperatureMeasurement
from .serializers import FermentationSerializer, TemperatureMeasurementSerializer

class FermentationViewSet(viewsets.ModelViewSet):
    queryset = Fermentation.objects.all()
    serializer_class = FermentationSerializer

class TemperatureMeasurementViewSet(viewsets.ModelViewSet):
    queryset = TemperatureMeasurement.objects.all()
    serializer_class = TemperatureMeasurementSerializer
