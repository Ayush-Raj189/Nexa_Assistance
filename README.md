# 🤖 Nexa Assistant

**Nexa Assistant** is a smart, voice-controlled Python assistant that lets you automate everyday tasks with natural speech. Whether it's checking the weather, reading the news, messaging on WhatsApp, playing music, or even telling a joke — Nexa does it all with your voice.

---

## 📌 Features

| Category           | Description                                                                 |
|--------------------|-----------------------------------------------------------------------------|
| 🎙️ Voice Input      | Listens to your voice using `speech_recognition`                            |
| 🗣️ Voice Output     | Replies using `pyttsx3` text-to-speech engine                               |
| 🔎 Web Browsing     | Opens Google, YouTube, LinkedIn, and more                                  |
| 🧠 Wiki Answers     | Fetches summaries from Wikipedia                                             |
| 📱 WhatsApp Control | Sends messages via `pywhatkit`                                              |
| 🌦️ Weather Reports  | Real-time weather updates via OpenWeatherMap API                            |
| 📰 News Headlines    | Speaks top headlines using News API                                         |
| 📍 Location Info    | Detects and speaks your current location using IP-based lookup              |
| 😂 Jokes & Games    | Tells random jokes and plays a number guessing game                         |
| 📸 Screenshot Tool  | Takes and saves a screenshot automatically                                  |
| 🔇 Volume Control   | Mute/unmute system volume with voice                                        |
| 🎵 Music Player     | Plays predefined songs from `musicLibrary.py`                               |
| 🛠️ App Launcher     | Opens system apps like Notepad, Calculator, Settings, Camera, etc.         |

---

## 💬 Sample Commands

> Just speak any of the following:
- "Open Google"
- "What's the weather in Mumbai?"
- "Send message to Riya"
- "Tell me a joke"
- "Search for AI tools"
- "Play a game"
- "Take a screenshot"
- "Mute the volume"
- "Play Believer"

## 🗂️ Folder Structure
Nexa_Assistant/
├── main.py # Core logic of voice assistant
├── musicLibrary.py # Dictionary of song names and YouTube links
├── requirements.txt # List of all dependencies
├── .env # API keys (not included in repo)
└── README.md # Project documentation

## 🔐 .env Configuration

Create a `.env` file and insert your keys like so:

```env
OPENAI_API_KEY=your_api_key_here
WEATHER_API_KEY=your_api_key_here
NEWS_API_KEY=your_api_key_here

🛠️ Setup Instructions
Follow these steps to get Nexa running:
# Clone the repository
git clone https://github.com/Ayush-Raj189/Nexa_Assistance.git
cd Nexa_Assistant

# Create a virtual environment
python -m venv venv

# Activate the environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Add your API keys to .env

# Run the assistant
python main.py


👨‍💻 Developer
Ayush Raj
GitHub: Ayush-Raj189

🌟 Show Your Support
If you like this project, don’t forget to ⭐ the repo. Contributions, ideas, and feedback are welcome!


