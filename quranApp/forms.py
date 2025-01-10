from django.db import models

class Language(models.Model):
    """Model representing a language."""
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)  # e.g., 'en', 'ar', etc.

    def __str__(self):
        return self.name

class Reciter(models.Model):
    """Model representing a Quran reciter."""
    name = models.CharField(max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    audio_url = models.URLField(max_length=200)  # URL for the reciter's audio

    def __str__(self):
        return self.name
