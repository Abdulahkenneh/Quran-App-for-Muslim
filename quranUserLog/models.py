

from django.contrib.auth.models import AbstractUser
from django.db import models
from quranApp.models import Reciter,Language

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    favorite_reciter = models.ForeignKey(Reciter, on_delete=models.SET_NULL, null=True, blank=True)
    selected_language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True)  # Add this field
    playback_speed = models.FloatField(default=1.0)
    repeat = models.BooleanField(default=False)
    daily_verse = models.BooleanField(default=False)
    prayer_times = models.BooleanField(default=False)

    def __str__(self):
        return self.username


