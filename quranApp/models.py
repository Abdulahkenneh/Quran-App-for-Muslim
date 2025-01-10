from django.db import models
from django.conf import settings
from django.utils.text import slugify  # Import slugify for generating slugs


class Language(models.Model):
    """Model to store languages."""
    name = models.CharField(max_length=100, unique=True)
    value = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


from django.db import models

class QuranEdition(models.Model):
    name = models.CharField(max_length=100, unique=True,blank=True)
    author = models.CharField(max_length=255,default=True)
    language = models.CharField(max_length=100,blank=True)
    url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.language})"


class Reciter(models.Model):
    """Model representing a Quran reciter."""
    name = models.CharField(max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    audio_url = models.URLField(max_length=200)

    def __str__(self):
        return self.name


class Surah(models.Model):
    """Model to store Quran Surahs."""
    number = models.PositiveIntegerField(unique=True)      # Surah number (1-114)
    name = models.CharField(max_length=100)                # Name of the Surah
    english_name = models.CharField(max_length=100)
    english_name_translation = models.CharField(max_length=255)  # Add this line
    total_ayahs = models.PositiveIntegerField()             # Total number of Ayahs (verses) in the Surah
    revelation_place = models.CharField(max_length=50)     # Place of revelation (Mecca or Medina)
    audio_url = models.URLField(max_length=200, blank=True, null=True)  # URL for audio recitation of the Surah
    slug = models.SlugField(unique=False, blank=True)        # Slug field

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  # Create slug from Surah name
        super().save(*args, **kwargs)


class EnglishSurah(models.Model):
    """Model to store Quran Surahs."""
    number = models.PositiveIntegerField(unique=True)      # Surah number (1-114)
    name = models.CharField(max_length=100)                # Name of the Surah
    english_name = models.CharField(max_length=100)
    english_name_translation = models.CharField(max_length=255)  # Add this line
    total_ayahs = models.PositiveIntegerField()             # Total number of Ayahs (verses) in the Surah
    revelation_place = models.CharField(max_length=50)     # Place of revelation (Mecca or Medina)
    audio_url = models.URLField(max_length=200, blank=True, null=True)  # URL for audio recitation of the Surah
    slug = models.SlugField(unique=False, blank=True)        # Slug field

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  # Create slug from Surah name
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'

class Ayah(models.Model):
    """Model to store Quran Ayahs."""
    surah = models.ForeignKey(Surah, on_delete=models.CASCADE)  # Foreign key to Surah
    number = models.PositiveIntegerField()  # Ayah number in the Surah
    text = models.TextField()  # Text of the Ayah
    text_arabic = models.TextField()
    text_english = models.TextField(blank=True, null=True)  # English translation of the Ayah
    translations = models.TextField(blank=True, null=True)  # Translation of the Ayah (optional)
    audio_url = models.URLField(max_length=200)  # Main audio URL for the Ayah
    audio_secondary = models.JSONField(blank=True, null=True)  # Secondary audio URLs (store as JSON)

    def __str__(self):
        return f'Ayah {self.number} of {self.surah.name}'


class EnglishAyah(models.Model):
    """Model to store Quran Ayahs."""
    english_surah = models.ForeignKey(EnglishSurah, on_delete=models.CASCADE,null=True,blank=True)  # Foreign key to EnglishSurah
    number = models.PositiveIntegerField()  # Ayah number in the Surah
    text = models.TextField()  # Text of the Ayah
    text_arabic = models.TextField()
    text_english = models.TextField(blank=True, null=True)  # English translation of the Ayah
    translations = models.TextField(blank=True, null=True)  # Translation of the Ayah (optional)
    audio_url = models.URLField(max_length=200)  # Main audio URL for the Ayah
    audio_secondary = models.JSONField(blank=True, null=True)  # Secondary audio URLs (store as JSON)


    def __str__(self):
        return f'Ayah {self.number} of {self.english_surah.name}'
class Bookmark(models.Model):
    """Model to store bookmarks for Ayahs."""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ayah = models.ForeignKey(Ayah, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Bookmark for {self.ayah} by {self.user.username}"


class Recitation(models.Model):
    """Model to link Reciters with specific Ayahs or Surahs."""
    reciter = models.ForeignKey(Reciter, on_delete=models.CASCADE)
    surah = models.ForeignKey(Surah, on_delete=models.CASCADE, null=True, blank=True)
    ayah = models.ForeignKey(Ayah, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.ayah:
            return f"{self.reciter.name} reciting {self.ayah}"
        elif self.surah:
            return f"{self.reciter.name} reciting {self.surah}"
        return f"{self.reciter.name} - No specific recitation"


class UserPreference(models.Model):
    """Model to store user preferences for the Quran app."""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    preferred_reciter = models.ForeignKey(Reciter, on_delete=models.SET_NULL, null=True, blank=True)
    preferred_language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Preferences"


class Translation(models.Model):
    """Model to store translations of Ayahs in different languages."""
    ayah = models.ForeignKey(Ayah, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    translation_text = models.TextField()

    def __str__(self):
        return f"{self.language.name} translation of {self.ayah}"


class DailyAyah(models.Model):
    """Model to store a daily Ayah for the users."""
    ayah = models.ForeignKey(Ayah, on_delete=models.CASCADE)
    date = models.DateField(unique=True)

    def __str__(self):
        return f"Daily Ayah for {self.date}: {self.ayah}"
