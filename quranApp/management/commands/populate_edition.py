from quranApp.models import QuranEdition
from django.core.management.base import BaseCommand
import requests
class Command(BaseCommand):
    def handle(self,*args, **kwargs):
        url = "https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions.min.json"
        response = requests.get(url)
        if response.status_code ==200:
            json_object = response.json()

            for edition_key, values in json_object.items():
                name = values.get('name')
                author = values.get("author")
                language = values.get("language")
                url = values.get("link")

                edition, created = QuranEdition.objects.update_or_create(
                    name=name,
                    defaults={
                        "author": author,
                        "language": language,
                        "url": url
                    }
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f'SUCCESS CREATED: {name}'))

                else:
                    self.stdout.write(self.style.SUCCESS(f'UPDATED EDITION: {name}'))

        else:
            self.stdout.write(self.style.ERROR(f"Error fetching editions: {response.status_code}"))