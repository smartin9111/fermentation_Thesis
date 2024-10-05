from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FermentationViewSet, TemperatureMeasurementViewSet

router = DefaultRouter()
router.register(r'fermentations', FermentationViewSet)
router.register(r'temperature-measurements', TemperatureMeasurementViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
