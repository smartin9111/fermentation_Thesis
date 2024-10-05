from django.core.management.base import BaseCommand
from datetime import timedelta, datetime, time
from django.utils.timezone import is_naive, make_aware, get_current_timezone
from api.models import Fermentation, TemperatureMeasurement
import random


class Command(BaseCommand):
    help = 'Generates temperature measurements for a specific fermentation using its start and end dates'

    def add_arguments(self, parser):
        parser.add_argument('fermentation_id', type=int, help='Fermentation ID for which to generate data')

    def handle(self, *args, **kwargs):
        fermentation_id = kwargs['fermentation_id']

        # Fermentáció ID alapján
        try:
            fermentation = Fermentation.objects.get(id=fermentation_id)
        except Fermentation.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Fermentation with ID {fermentation_id} does not exist.'))
            return

        # Ellenőrzi, hogy van-e start_date és end_date
        if not fermentation.start_date or not fermentation.end_date:
            self.stdout.write(self.style.ERROR('Fermentation must have both start_date and end_date.'))
            return

        # Naive vagy időzónával rendelkező datetime generálása a rendszer beállítása szerint
        start_time = datetime.combine(fermentation.start_date, time(0, 0))
        end_time = datetime.combine(fermentation.end_date, time(23, 59))

        # Ha az időzóna támogatása aktív (USE_TZ = True), az időpontokat aware típusúra alakítjuk
        if is_naive(start_time):
            start_time = make_aware(start_time, get_current_timezone())
        if is_naive(end_time):
            end_time = make_aware(end_time, get_current_timezone())

        # Ellenőrizzük, hogy a dátumok valóban a megadottak-e
        self.stdout.write(self.style.SUCCESS(f'Start time: {start_time}, End time: {end_time}'))

        # Minden napra generáljunk adatokat, percrenként növelve az időt
        current_time = start_time
        while current_time <= end_time:
            temperature_c = random.randint(12, 25)

            # Hőmérséklet adat mentése az adatbázisba
            TemperatureMeasurement.objects.create(
                fermentation=fermentation,
                timestamp=current_time,
                temperature_c=temperature_c
            )

            # Ellenőrizzük, hogy a timestamp valóban a megadott időn belül mozog
            self.stdout.write(f'Generated: {temperature_c}°C at {current_time}')

            # Növeljük az időt egy perccel
            current_time += timedelta(minutes=1)

        self.stdout.write(
            self.style.SUCCESS(f'Successfully generated temperature data for fermentation ID {fermentation_id}'))
