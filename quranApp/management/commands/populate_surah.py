# management/commands/populate_quran.py
import requests
from django.core.management.base import BaseCommand
from quranApp.models import Surah, Ayah

class Command(BaseCommand):
    help = 'Populate Surah and Ayah models from external Quran APIs'

    def handle(self, *args, **kwargs):
        for i in range(1, 115):  # Change range if needed
            # Fetch Arabic data
            api_url_arabic = f"https://api.alquran.cloud/v1/surah/{i}/ar.alafasy"
            response_arabic = requests.get(api_url_arabic)
            if response_arabic.status_code == 200:
                quran_data_arabic = response_arabic.json()['data']
                self.populate_surah_ayah(quran_data_arabic, language='arabic')

            # Remove or comment out the English data fetching
            # # Fetch English data
            # api_url_english = f"https://api.alquran.cloud/v1/surah/{i}/en.yusufali"  # Example English API
            # response_english = requests.get(api_url_english)
            # if response_english.status_code == 200:
            #     quran_data_english = response_english.json()['data']
            #     self.populate_surah_ayah(quran_data_english, language='english')

    def populate_surah_ayah(self, data, language):
        # Populate Surah information
        surah, created = Surah.objects.get_or_create(
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

        # Populate Ayah information for Arabic
        for ayah_data in data['ayahs']:
            if language == 'arabic':
                ayah, created = Ayah.objects.get_or_create(
                    surah=surah,
                    number=ayah_data['numberInSurah'],
                    text_arabic=ayah_data['text'],
                    audio_url=ayah_data['audio'],
                    audio_secondary=ayah_data['audioSecondary']
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Created Ayah {ayah.number} of Surah {surah.english_name}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Ayah {ayah.number} of Surah {surah.english_name} already exists'))

# To run the command
# python manage.py populate_quran
