def sura_detail_view(request, surah_id):
    user_prefered_language = request.user.selected_language
    arabic_verses_form_quranpy = quranpy.Surah(surah_id, edition=ORIGINAL_REVELATION_LANGUAGE)
    quran = quranpy.Surah(surah_id, edition=user_prefered_language)

    edition = 'ar'

    QURAN_COM_API_URL = "https://api.quran.com/api/v4"
    arabic_verses_from_cloud = f"{QURAN_CLOUD_API}/surah/{surah_id}/{edition}"
    verses_url = f'{QURAN_COM_API_URL}/verses/by_chapter/{surah_id}'
    arabic_url = f'{QURAN_COM_API_URL}/verses/by_chapter/{surah_id}?language=ar&words=true'
    english_url = f'{QURAN_COM_API_URL}/chapters/{surah_id}?language=en'  # Surah details in English

    # Fetching verses and surah details
    try:
        
        verses_response = requests.get(verses_url)
        arabic_response = requests.get(arabic_url)
        english_response = requests.get(english_url)
        arabic_verses_from_cloud = requests.get(arabic_verses_from_cloud)


        # Check if all responses are successful
        if (
            verses_response.status_code == 200 and
            arabic_response.status_code == 200 and
            english_response.status_code == 200 and
            arabic_verses_from_cloud.status_code ==200
        ):
            # Parse the JSON responses
            verses_data = verses_response.json().get('verses', [])
            arabic_sura_data = arabic_response.json().get('verses', [])
            english_sura_data = english_response.json().get('data', {})
            arabic_verses = arabic_verses_from_cloud.json()
            arabic_verses =arabic_verses['data']

            # Print debug information
          

            # Render the data in the template
            return render(request, 'quranApp/sura_detail.html', {
              #  'arabic_sura': arabic_sura_data,
              #  'english_sura': english_sura_data,
                'surah_number': surah_id,
              #  'verses': verses_data,
                'arabic_verses':arabic_verses_form_quranpy,
                'quran_verses_in_user_prefered_languages':quran,


        
            })

        else:
            return HttpResponse("Error fetching surah data from API", status=404)

    except Exception as e:
        return HttpResponse(f"An error occurred: {e}", status=500)
