from django.contrib import admin
from .models import Fruit, Fermentation, Location, TemperatureMeasurement, SugarMeasurement, PHMeasurement, Evaluation

admin.site.register(Fruit)
admin.site.register(Fermentation)
admin.site.register(Location)
admin.site.register(TemperatureMeasurement)
admin.site.register(SugarMeasurement)
admin.site.register(PHMeasurement)
admin.site.register(Evaluation)


