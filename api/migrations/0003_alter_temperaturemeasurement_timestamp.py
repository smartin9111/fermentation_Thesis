# Generated by Django 4.2.16 on 2024-10-01 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_evaluation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperaturemeasurement',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
