from django.core.management.base import BaseCommand
from myapp.models import Zupanija
import json
import os

class Command(BaseCommand):
    help = 'Napuni zupanije iz JSON datoteke'

    def handle(self, *args, **kwargs):
        
        script_dir = os.path.dirname(os.path.abspath(__file__))
        json_datoteka = os.path.join(script_dir, 'lokacije.json')

        with open(json_datoteka, 'r', encoding='utf-8') as file:
            data = json.load(file)

        for entry in data:
            # Remove the "Županija" suffix from the name and create Zupanija instance
            zupanija_name = entry['zupanija'].replace(' Županija', '')
            zupanija, created = Zupanija.objects.get_or_create(naziv=zupanija_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Kreirana zupanija: {zupanija}'))

        self.stdout.write(self.style.SUCCESS('Izvršeno punjenje'))
