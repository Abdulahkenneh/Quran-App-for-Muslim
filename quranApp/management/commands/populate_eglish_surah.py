# management/commands/populate_quran.py
import requests
from django.core.management.base import BaseCommand
from quranApp.models import Surah, EnglishAyah,EnglishSurah  # Ensure you import the correct models

class Command(BaseCommand):
    help = 'Populate Surah and Ayah models from external Quran APIs'

    def handle(self, *args, **kwargs):
        for i in range(1, 115):  # Change range if needed
            # Fetch English data
            api_url_english = f"https://api.alquran.cloud/v1/surah/{i}/en.yusufali"  # Example English API
            response_english = requests.get(api_url_english)
            if response_english.status_code == 200:
                quran_data_english = response_english.json()['data']
                self.populate_surah_ayah(quran_data_english)

    def populate_surah_ayah(self, data):
        # Populate Surah information
        surah, created = EnglishSurah.objects.get_or_create(
            number=data['number'],
            name=data['name'],
            english_name=data['englishName'],
            english_name_translation=data['englishNameTranslation'],
            revelation_place=data['revelationType'],
            total_ayahs=data['numberOfAyahs'],
            slug=data['name'],
        )

        if created:
            self.stdout.write(self.style.SUCCESS(f'Created Surah: {surah.english_name}'))
        else:
            self.stdout.write(self.style.WARNING(f'Surah {surah.english_name} already exists'))

        # Populate Ayah information for English
        for ayah_data in data['ayahs']:
            ayah, created = EnglishAyah.objects.get_or_create(
                english_surah=surah,
                number=ayah_data['numberInSurah'],
                text_english=ayah_data['text'],
                # If you want to include audio URL or other fields, add them here
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created Ayah {ayah.number} of Surah {surah.english_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Ayah {ayah.number} of Surah {surah.english_name} already exists'))

# To run the command
# python manage.py populate_quran
