from django.shortcuts import render
import requests
import  quranpy

from django.shortcuts import HttpResponse
# Create your views here.
from urllib.error import HTTPError
from django.http import Http404
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Reciter, QuranEdition, Language,UserPreference,Surah,Ayah,EnglishSurah,EnglishAyah
from django.contrib import messages
import quranpy
from django.shortcuts import render
from django.http import HttpResponse
import requests



QURAN_SEARCH_API_URL = "http://api.alquran.cloud/v1/search/Abraham/all/en -"
QURAN_API = 'https://api.quran.com/api/v4/chapters'
#THE ARABIC TEXT OF THE QURAN
QURAN_CLOUD_API = "http://api.alquran.cloud/v1/"
QURAN_CLOUD_AUDIO_API = 'https://cdn.islamic.network/quran/audio/'
AUDIO_BITRATE = 128

ORIGINAL_REVELATION_LANGUAGE = quranpy.Editions.arabic


# Define the base Quran.com API URLs
QURAN_API_CHAPTERS = "https://api.quran.com/api/v4/chapters"
QURAN_API_SEARCH = "https://api.quran.com/api/v4/search"

QURAN_CLOUD_API_URL = 'http://api.alquran.cloud/v1'
QURAN_API_VERSES = "https://api.quran.com/api/v4/"
QURAN_COM_API_URL = "https://api.quran.com/api/v4"

# views.py

DEFAUL_ARABIC_EDITION = 'ar.alafasy'
DEFAUL_ENGLISH_EDITION = 'en.yusufali'



def quran_settings(request):
    # Get all available reciters and languages
    reciters = Reciter.objects.all()
    languages = Language.objects.all()

    # Get the current user settings (e.g., favorite reciters, selected language, playback speed, notifications)
    user = request.user
    favorite_reciters = user.favorite_reciter # Assuming user has a many-to-many field for favorite reciters
    selected_language = user.selected_language  # Assuming user has a foreign key for selected language

    context = {
        'reciters': reciters,
        'languages': languages,
        'favorites': favorite_reciters,
        'selected_language': selected_language,
        'playback_speed': user.playback_speed,
        'repeat': user.repeat,
        'daily_verse': user.daily_verse,
        'prayer_times': user.prayer_times
    }

    return render(request, 'quranApp/settings.html', context)


# Update favorite reciter
@login_required
def update_favorite_reciter(request):
    if request.method == 'POST':
        reciter_id = request.POST.get('reciter_id')
        if reciter_id:
            user = request.user
            user.favorite_reciters.clear()  # Ensure only one favorite reciter
            user.favorite_reciters.add(reciter_id)
            messages.success(request, "Favorite reciter updated successfully!")
        else:
            messages.error(request, "Please select a valid reciter.")
        return redirect('quranApp:quran_settings')


# Update translation language
@login_required
def update_language_settings(request):
    if request.method == 'POST':
        language_id = request.POST.get('language_id')
        if language_id:
            user = request.user
            user.selected_language_id = language_id
            user.save()
            messages.success(request, "Language updated successfully!")
        else:
            messages.error(request, "Please select a valid language.")
        return redirect('quranApp:quran_settings')


# Update audio playback settings
@login_required
def update_audio_settings(request):
    if request.method == 'POST':
        user = request.user
        user.playback_speed



def clean_search():
    try:
        url = "http://api.alquran.cloud/v1/search"
        return url
    except HTTPError as e:
        return e


def home(request):
    # Fetch the Quran Surah details (chapters)

    surahs = Surah.objects.all()
    response = requests.get(QURAN_API_CHAPTERS)

    if response.status_code == 200:
        chapters = response.json().get('chapters', [])
    else:
        chapters = []

    # Initialize search_response to None in case there is no search query
    search_response = None
    query = request.GET.get('search')

    if query:
        # Perform search using the Quran.com API
        search_params = {
            'q': query,  # The search query parameter
            'size': 10   # Limit the number of results
        }
        response = requests.get(QURAN_API_SEARCH, params=search_params)

        if response.status_code == 200:
            # Extract search results from the 'data' key in the response
            search_response = response.json().get('data', {}).get('matches', [])

    # Pass both the chapters and search results to the template
    return render(request, 'quranApp/home.html', {
        'chapters': surahs,
        'search_response': search_response,
        'query': query
    })





quran=quranpy
#methods = [method for method in dir(quran) if not method.startswith('__')]
#print(methods)

from django.shortcuts import render
from django.http import HttpResponse
from .models import Surah, Ayah
import quranpy  # Assuming quranpy is the library you're using

# Constants for language editions
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Surah, Ayah, EnglishSurah, Language

# Assuming you store the default language in some constant variables:

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Surah, EnglishSurah, Ayah, EnglishAyah  # Ensure you have your models imported correctly
import quranpy


# DEFAUL_ARABIC_EDITION = Language.objects.get(name='arabic')
# DEFAUL_ENGLISH_EDITION = Language.objects.get(name='yusufali')
#
# DEFAUL_ARABIC_EDITION = Language.objects.get(name='arabic')
# DEFAUL_ENGLISH_EDITION = Language.objects.get(name='yusufali')

# def sura_detail_view(request, surah_id):
#     # Get the user's preferred language or fallback to English
#     api_url = f"https://api.quran.cloud/v1/surah/{surah_id}"
#     user_preferred_language = request.user.selected_language if request.user.is_authenticated else DEFAUL_ENGLISH_EDITION
#     languages = Language.objects.values_list('value', flat=True).first()
#
#     languages = languages
#     newdic=dict()
#
#
#
#
#     ayahs_in_preferred = quranpy.Surah(surah_id, edition=user_preferred_language)
#     print(f'This is user language: {user_preferred_language}')
#
#     try:
#         # Fetch the Surah object for both Arabic and English translations
#         arabic_surah = get_object_or_404(Surah, number=surah_id)
#         english_surah = get_object_or_404(EnglishSurah, number=surah_id)
#
#         # Fetch Ayahs for Arabic (always displayed) and English
#         defaul_arabic_ayahs = Ayah.objects.filter(surah=arabic_surah)  # Arabic ayahs, constant
#         defaul_english_ayahs = EnglishAyah.objects.filter(english_surah=english_surah)  # English translation
#
#         # Initialize variables
#         ayahs_in_preferred_language = None
#
#         # Determine which ayahs to display based on the user's preferred language
#         if user_preferred_language == DEFAUL_ARABIC_EDITION:
#             ayahs_in_preferred_language = defaul_arabic_ayahs  # If Arabic, display Arabic text only
#         elif user_preferred_language == DEFAUL_ENGLISH_EDITION:
#             ayahs_in_preferred_language = defaul_english_ayahs  # If English, display English translation
#         else:
#             # For any other language, use `quranpy` to fetch the preferred language ayahs
#             try:
#
#                ayahs_in_preferred_language = quranpy.Surah(surah_id, edition=user_preferred_language)
#             except Exception as e:
#                 print(f"Error fetching preferred language ayahs: {e}")
#                 # Fallback to the English translation if quranpy fetch fails
#                 ayahs_in_preferred_language = defaul_english_ayahs
#
#         return render(request, 'quranApp/sura_detail.html', {
#             'defaul_arabic_ayahs': defaul_arabic_ayahs,  # Always display Arabic ayahs
#             'ayahs_in_preferred_language': ayahs_in_preferred_language,  # Based on user preference (or fallback)
#             'user_preferred_language': user_preferred_language,  # Pass the user's preferred language for display
#             'ayahs_in_preferred':ayahs_in_preferred,
#
#
#             'codes':languages,
#         })

    # except Surah.DoesNotExist:
    #     return HttpResponse("Surah not found.", status=404)
    # except Exception as e:
    #     print(f"An error occurred: {e}")
    #     return HttpResponse(f"An error occurred: {e}", status=500)


import requests

DEFAUL_ARABIC_EDITION = 'en' #Language.objects.get(name='arabic')
DEFAUL_ENGLISH_EDITION = 'en' #Language.objects.get(name='yusufali')

def get_surah_ayahs(surah_id, edition):
    """Fetches the Ayahs from the Quran Cloud API based on the surah_id and language edition."""
    quran_com_url= f"https://api.quran.com/api/v4/quran/verses/by_chapter/{surah_id}?language=en&edition={edition}"

    api_url = f"https://api.quran.cloud/v1/surah/{surah_id}/editions/{edition}"

    try:
        # Send a GET request to fetch the Surah ayahs in the preferred language
        response = requests.get(api_url)
        response.raise_for_status()  # Raise exception for HTTP errors

        data = response.json()

        # Ensure the response status is OK and contains ayahs
        if data['status'] == 'OK':
            ayahs = data['data'][0]['ayahs']  # Accessing the Ayahs list
            return ayahs
        else:
            print(f"Failed to fetch ayahs for Surah {surah_id} in edition {edition}: {data['message']}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching preferred language ayahs from Quran API: {e}")
        return None


def sura_detail_view(request, surah_id):
    # Get the user's preferred language or fallback to English
    user_preferred_language = request.user.selected_language if request.user.is_authenticated else DEFAUL_ENGLISH_EDITION
    print(f'This is user language: {user_preferred_language}')

    defaultedition = QuranEdition.objects.filter(name='ara-quransimple', language='Arabic').values_list('name',
                                                                                                 flat=True).first()
    edition = QuranEdition.objects.filter(language='Arabic').values_list('name', flat=True).first()
    #user_preferred_language_with_code = Language.objects.filter(name=user_preferred_language).values_list('value', flat=True).first()

    default_language = True
    default_language = True
    response_obj = None
    try:
        # Fetch the Surah object
        arabic_surah = get_object_or_404(Surah, number=surah_id)
        english_surah = get_object_or_404(EnglishSurah, number=surah_id)

        # Fetch Ayahs for Arabic and English
        defaul_arabic_ayahs = Ayah.objects.filter(surah=arabic_surah)
        defaul_english_ayahs = EnglishAyah.objects.filter(english_surah=english_surah)

        # Initialize variables
        ayahs_in_preferred_language = None
        default_language = defaul_arabic_ayahs  # Default to Arabic if anything fails

        default_edition_url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{defaultedition}/{surah_id}.json"
        response = requests.get(default_edition_url)
        if response.status_code == 200:
            default_language = response.json().get('verses',[])
            if not default_language:
                # Fallback to English if the preferred language fetching fails
                default_language = defaul_english_ayahs



        #This is the api that is getting tranlation of the quran
        quran_url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/{edition}/{surah_id}.json"

        response = requests.get(quran_url)
        if response.status_code == 200:
            ayahs_in_preferred_language = response.json().get('verses', [])
            if not ayahs_in_preferred_language:
                # Fallback to English if the preferred language fetching fails
                ayahs_in_preferred_language = defaul_english_ayahs




#       This is the api that is get the genuine numbers of the quran
        url_from_quranCom = f"https://api.quran.com/api/v4/verses/by_chapter/{surah_id}"
        quran_com_url_response = requests.get(url_from_quranCom)
        if quran_com_url_response.status_code ==200:
            verse_from_quran_com_url_response_obj =quran_com_url_response.json().get('verses', [])

        # Handle preferred language Ayahs dynamically
        if user_preferred_language == DEFAUL_ARABIC_EDITION:
            ayahs_in_preferred_language = defaul_arabic_ayahs
        elif user_preferred_language == DEFAUL_ENGLISH_EDITION:
            ayahs_in_preferred_language = defaul_english_ayahs
        else:
            # For any other language, use the Quran Cloud API to fetch the preferred language ayahs
            try:

                quran_url = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/al-Madina/{surah_id}.json"
                response = requests.get(quran_url)
                if response.status_code == 200:
                    ayahs_in_preferred_language = response.json().get('chapter')
                    if not ayahs_in_preferred_language:
                        # Fallback to English if the preferred language fetching fails
                        ayahs_in_preferred_language = defaul_english_ayahs
            except Exception as e:
                print(f"Error fetching preferred language ayahs: {e}")
                ayahs_in_premferred_language = defaul_english_ayahs  # Fallback to English
        zip_lists = zip(default_language, ayahs_in_preferred_language, verse_from_quran_com_url_response_obj)

        return render(request, 'quranApp/sura_detail.html', {

            'DEFAUL_ENGLISH_EDITION': user_preferred_language,
            'defaul_english_ayahs': defaul_english_ayahs,  # English Ayahs
            'user_preferred_language': user_preferred_language,
            'zip_lists':zip_lists,
            'default_language': default_language,
            'verse_from_quran_com_url_response_obj':verse_from_quran_com_url_response_obj,
            'ayahs_in_preferred_language':ayahs_in_preferred_language


             # Ayahs in user's preferred language
        })
    except Surah.DoesNotExist:
        return HttpResponse("Surah not found.", status=404)
    except Exception as e:
        print(f"An error occurred: {e}")
        return HttpResponse(f"An error occurred: {e}", status=500)

def sura_page_detail_view(request, surah_id):
    # Fetch Arabic text and optionally a translation (e.g., en.asad for English translation)
    arabic_response = requests.get(f'{QURAN_CLOUD_API_URL}/{surah_id}/ar.alafasy')
    translation_response = requests.get(f'{QURAN_CLOUD_API_URL}/{surah_id}/en.asad')

    if arabic_response.status_code == 200 and translation_response.status_code == 200:
        arabic_data = arabic_response.json()
        translation_data = translation_response.json()

        # Combine Arabic and translation in a structured format
        sura_data = {
            'name': arabic_data['data']['name'],
            'number': arabic_data['data']['number'],
            'verses': [
                {
                    'number': verse['number'],
                    'arabic': verse['text'],
                    'translation': translation_data['data']['ayahs'][index]['text']
                }
                for index, verse in enumerate(arabic_data['data']['ayahs'])
            ]
        }
        return render(request, 'quranApp/sura_detail.html', {'sura': sura_data})
    else:
        return HttpResponse("Sura not found.", status=404)
def tafseer_view(request):
    return render(request, 'quranApp/tafseer.html', context={})

def prayer_times_view(request):
    return render(request, 'quranApp/prayer_times.html', context={})

def profile_view(request):
    return render(request, 'quranApp/profile.html', context={})


def memorization_view(request):
    return render(request, 'quranApp/memorization.html', context={})

def daily_ayah_view(request):
    return render(request, 'quranApp/daily_ayah.html', context={})


def play_audio_verse(request,verse_number):
    edition ='ar.alafasy'
    url = f"https://cdn.islamic.network/quran/audio/128/{edition}/{verse_number}.mp3"

    response = requests.get(url)

    if response.status_code != 200:  # Render error page if the status code is not 200
        return render(request, 'quranApp/errorpage.html')
    else:
        quran_json_obj = response.json()# Parse the JSON response

        quranDictionary = dict()
        for suraNumber , sura in enumerate(quran_json_obj):
            quranDictionary[sura]=suraNumber
        return render(request, 'quranApp/home.html', context={'suras': quran_json_obj,'quranDictionary':quranDictionary})



def settings(request):
    return render(request,'quranApp/settings.html')

@login_required
def update_notifications_settings(request):
    if request.method == 'POST':
        user = request.user
        user.daily_verse = 'daily_verse' in request.POST
        user.prayer_times = 'prayer_times' in request.POST
        user.save()
        return redirect('quranApp:quran_settings')


@login_required
def update_audio_settings(request):
    if request.method == 'POST':
        user = request.user
        user.playback_speed = request.POST.get('playback_speed', 1.0)
        user.repeat = 'repeat' in request.POST
        user.save()
        return redirect('quranApp:quran_settings')


@login_required
def update_language_settings(request):
    if request.method == 'POST':
        language_id = request.POST.get('language_id')
        if language_id:
            user = request.user
            user.selected_language_id = language_id
            user.save()
        return redirect('quranApp:quran_settings')


def update_favorite_reciter(request):
    if request.method == 'POST':
        reciter_id = request.POST.get('reciter_id')
        if reciter_id:
            user = request.user
            try:
                selected_reciter = Reciter.objects.get(id=reciter_id)
                user.favorite_reciter = selected_reciter  # Assign favorite reciter
                user.save()
            except Reciter.DoesNotExist:
                pass
        return redirect('quranApp:quran_settings')