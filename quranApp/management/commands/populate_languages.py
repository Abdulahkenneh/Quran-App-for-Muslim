from django.core.management.base import BaseCommand
from quranApp.models import Language
from quranpy import Editions  # Ensure this is the correct import

class Command(BaseCommand):
    help = 'Populate languages from Quran editions'

    def handle(self, *args, **kwargs):
        for edition in Editions:
            print(dir(edition))
            # Extract language name and code based on your Editions structure
            lang_name = edition.name  # or however the name is structured
            lang_code = edition.value  # assuming this gives you the code

            # Create or get the language
            Language.objects.get_or_create(name=lang_name, value=lang_code)

        self.stdout.write(self.style.SUCCESS('Successfully populated languages'))
