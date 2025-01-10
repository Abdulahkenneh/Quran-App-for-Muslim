from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import EnglishSurah, QuranEdition,EnglishAyah, Reciter, Language, Surah, Ayah, Bookmark, Recitation, UserPreference, DailyAyah

# Custom User Admin

# Reciter Admin
class ReciterAdmin(admin.ModelAdmin):
    """Admin interface for Reciter model."""
    list_display = ('name', 'language')  # Removed 'audio_url'
    list_filter = ('language',)
    search_fields = ('name',)
    ordering = ('name',)

class QuranEditionAdmin(admin.ModelAdmin):
    """Admin interface for Reciter model."""
    list_display = ('language',)  # Removed 'audio_url'
    list_filter = ('language',)
    search_fields = ('edition_name',)
   
    
# Language Admin
class LanguageAdmin(admin.ModelAdmin):
    """Admin interface for Language model."""
    list_display = ('name', 'value')  # Assuming you have 'name' and 'code' fields
    search_fields = ('name', 'value')
    ordering = ('name',)

# Surah Admin
class SurahAdmin(admin.ModelAdmin):
    """Admin interface for Surah model."""
    list_display = ('number', 'name', 'english_name', 'total_ayahs', 'revelation_place')
    list_filter = ('revelation_place',)
    search_fields = ('name', 'english_name')
    ordering = ('number',)

class EnglishSurahAdmin(admin.ModelAdmin):
    list_display = ('number', 'name', 'english_name', 'total_ayahs', 'revelation_place')
    list_filter = ('revelation_place',)
    search_fields = ('name', 'english_name')
    ordering = ('number',)

# Ayah Admin
class AyahAdmin(admin.ModelAdmin):
    """Admin interface for Ayah model."""
    list_display = ('number', 'surah', 'text_english',)  # Adjusted to show relevant fields
    list_filter = ('surah',)
    search_fields = ('text_english',)  # Assuming 'text_english' is the correct field name
    ordering = ('surah', 'number')
class EnglishAyahAdmin(admin.ModelAdmin):
    """Admin interface for Ayah model."""
    list_display = ('number', 'english_surah', 'text_english',)  # Adjusted to show relevant fields
    list_filter = ('english_surah',)
    search_fields = ('text_english',)  # Assuming 'text_english' is the correct field name
    ordering = ('english_surah', 'number')

# Bookmark Admin
class BookmarkAdmin(admin.ModelAdmin):
    """Admin interface for Bookmark model."""
    list_display = ('user', 'ayah', 'created_at')
    list_filter = ('user',)
    search_fields = ('user__username', 'ayah__text')
    ordering = ('created_at',)

# Recitation Admin
class RecitationAdmin(admin.ModelAdmin):
    """Admin interface for Recitation model."""
    list_display = ('reciter', 'surah', 'ayah')
    list_filter = ('reciter', 'surah', 'ayah')
    search_fields = ('reciter__name', 'surah__name', 'ayah__text')
    ordering = ('reciter',)

# User Preference Admin
class UserPreferenceAdmin(admin.ModelAdmin):
    """Admin interface for User Preference model."""
    list_display = ('user', 'preferred_reciter', 'preferred_language')
    list_filter = ('preferred_reciter', 'preferred_language')
    search_fields = ('user__username',)
    ordering = ('user',)

# Daily Ayah Admin
class DailyAyahAdmin(admin.ModelAdmin):
    """Admin interface for Daily Ayah model."""
    list_display = ('ayah', 'date')
    list_filter = ('date',)
    search_fields = ('ayah__text',)
    ordering = ('date',)

# Register the models with the admin site
admin.site.register(Reciter, ReciterAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Surah, SurahAdmin)
admin.site.register(EnglishSurah, EnglishSurahAdmin)
admin.site.register(Ayah, AyahAdmin)
admin.site.register(EnglishAyah, EnglishAyahAdmin)
admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Recitation, RecitationAdmin)
admin.site.register(UserPreference, UserPreferenceAdmin)
admin.site.register(DailyAyah, DailyAyahAdmin)
admin.site.register(QuranEdition,QuranEditionAdmin)
