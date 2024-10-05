from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name

class Fruit(models.Model):
    FRUIT_CHOICES = [
        ('apple', 'Alma'),
        ('plum', 'Szilva'),
        ('apricot', 'Barack'),
        ('sour_cherry', 'Cigány meggy'),
        ('grape', 'Szőlő'),
    ]
    name = models.CharField(max_length=50, choices=FRUIT_CHOICES)
    harvest_date = models.DateField()
    weight_kg = models.FloatField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.harvest_date}"

class Fermentation(models.Model):
    fruit = models.ForeignKey(Fruit, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    final_yield_l = models.FloatField(null=True, blank=True)
    alcohol_percentage = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Fermentation of {self.fruit}"

class TemperatureMeasurement(models.Model):
    fermentation = models.ForeignKey(Fermentation, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    temperature_c = models.FloatField()

    def __str__(self):
        return f"Temperature: {self.temperature_c}°C at {self.timestamp}"

class SugarMeasurement(models.Model):
    fermentation = models.ForeignKey(Fermentation, on_delete=models.CASCADE)
    date = models.DateField()
    sugar_content_percent = models.FloatField()

    def __str__(self):
        return f"Sugar content: {self.sugar_content_percent}% on {self.date}"

class PHMeasurement(models.Model):
    fermentation = models.ForeignKey(Fermentation, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    ph_value = models.FloatField()

    def __str__(self):
        return f"PH: {self.ph_value} at {self.timestamp}"

class Evaluation(models.Model):
    fermentation = models.ForeignKey(Fermentation, on_delete=models.CASCADE)
    output_volume_l = models.FloatField(help_text="Final output volume in liters")
    taste_score = models.IntegerField(help_text="Taste evaluation on a scale of 1-10")
    smell_score = models.IntegerField(help_text="Smell evaluation on a scale of 1-10")
    color_score = models.IntegerField(help_text="Color evaluation on a scale of 1-10")
    notes = models.TextField(null=True, blank=True, help_text="Additional notes for the evaluation")

    def __str__(self):
        return f"Evaluation for {self.fermentation} - Output: {self.output_volume_l} L"
