# Quran Explorer App 🌙📖

A feature-rich, interactive application for exploring the Holy Quran. This application enables users to access Quranic chapters, verses, translations, audio recitations, prayer times, and more, all with a user-friendly interface.

## Features

### Core Functionalities
- **Surah and Ayah Details**: Browse chapters and verses of the Quran with Arabic text and translations in multiple languages.
- **Audio Playback**: Play audio recitations of verses with adjustable playback speed.
- **Search Functionality**: Search the Quran by keyword or phrase.
- **Daily Ayah**: Receive a daily verse for inspiration and reflection.
- **Prayer Times**: View Islamic prayer times based on your location.

### User Personalization
- **Favorite Reciters**: Select and manage your favorite Quran reciters.
- **Language Selection**: Choose your preferred language for translations.
- **Audio Playback Settings**: Adjust playback speed and enable repeat options.
- **Notifications**: Enable or disable notifications for daily verses and prayer times.

### Quran Data Sources
- **API Integration**: Fetch Quranic data and translations from reliable sources such as:
  - [Quran.com API](https://api.quran.com)
  - [AlQuran Cloud API](http://api.alquran.cloud)
  - [QuranPy Library](https://pypi.org/project/quranpy/)
  
## Tech Stack

- **Backend**: Django, Python
- **Frontend**: HTML, CSS, JavaScript
- **APIs**: Quran.com API, AlQuran Cloud API
- **Database**: SQLite/PostgreSQL (configurable)
- **Libraries**:
  - [QuranPy](https://pypi.org/project/quranpy/) for Quranic data handling
  - Requests for API communication

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/quran-explorer.git
   cd quran-explorer






Create a virtual environment and activate it:


python3 -m venv env
source env/bin/activate
Install the dependencies:


pip install -r requirements.txt
Apply migrations and start the server:


python manage.py migrate
python manage.py runserver
Open your browser and navigate to http://127.0.0.1:8000.

Usage
Home Page: Browse Quranic chapters and perform searches.
Settings: Customize language preferences, favorite reciters, and notification settings.
Audio Playback: Listen to recitations directly within the app.
API Endpoints
Quran Chapters: /api/v4/chapters
Search Verses: /api/v4/search
Audio: /quran/audio/128/<edition>/<verse_number>.mp3
Contribution
This project is still open for improvement, and we welcome every collaborator! Whether you have ideas for new features, bug fixes, or enhancements, your contributions are highly appreciated.

To contribute:

Fork the repository.
Create a new branch (feature/your-feature).
Commit your changes and push to the branch.
Open a pull request.
Together, we can build a better application for everyone in the global Muslim community.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Quran.com for Quranic data and API support.
AlQuran Cloud for Quranic text and audio APIs.
The global Muslim community for their support and feedback.
Made with 💖 and 🌙 by <h2>Abdulah Mamadee Kenneh</h2>


Let me know if you need further tweaks!



   
