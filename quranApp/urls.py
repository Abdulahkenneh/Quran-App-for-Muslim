from django.urls import path
from .views import home,update_audio_settings,update_language_settings,play_audio_verse,settings,quran_settings,update_notifications_settings,update_favorite_reciter,sura_page_detail_view,sura_detail_view,profile_view,prayer_times_view,tafseer_view,memorization_view,daily_ayah_view

app_name = 'quranApp'
urlpatterns = [
    path('',home,name='home'),
    # Qur'an Surah Detail page (default to Surah 1 if not specified)
    path('quran/<int:surah_id>/', sura_detail_view, name='sura-detail'),  # Matches just surah_id
    path('quran/<int:surah_id>/<int:ayah_id>/', sura_detail_view, name='sura-detail-with-ayah'),

    path('quran-page/<int:surah_id>/',sura_page_detail_view, name='sura_page_detail'),
    path('tafseer/',tafseer_view,name='tafseer'),
    path('prayer-time/',prayer_times_view,name='prayer_times'),
    path('profile/',profile_view,name='profile'),
    path('memorization/',memorization_view,name='memorization'),
    path('daily-ayah/',daily_ayah_view,name='daily_ayah'),


    #settings urls
# Route for rendering the settings page
    path('settings/', quran_settings, name='quran_settings'),

    # Route for updating the favorite reciter
    path('settings/favorite_reciter/', update_favorite_reciter, name='favorite_reciters'),

    # Route for updating the translation language
    path('settings/language/', update_language_settings, name='update_language_settings'),

    # Route for updating the audio playback settings
    path('settings/audio/', update_audio_settings, name='update_audio_settings'),

    # Route for updating notification settings
    path('settings/notifications/', update_notifications_settings, name='update_notifications_settings'),



]

