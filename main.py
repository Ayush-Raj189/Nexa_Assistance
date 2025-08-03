import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
import datetime
import os
import re
import random
import pyautogui
import wikipedia
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import pyjokes
import pywhatkit
from dotenv import load_dotenv
load_dotenv()

contacts = {
    "ayush": "+919835237626",  # Replace with actual number
    "Ansh": "+919079231064",
    "Rahul":"+917410993211",
    "Priyansh":"+919571025342",
}
def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)
    
# Listen function
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Recognizing...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        print("Command:", command)
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand.")
        return ""
    except sr.RequestError:
        speak("Sorry, I'm having trouble reaching the recognition service.")
        return ""
    
    
def set_volume_mute(mute=True):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMute(mute, None)
    
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = os.getenv("NEWS_API_KEY")
# newsapi = "df7add71f6fd4d2a9e9cabe39c689c99"

def get_location():
    try:
        ip = requests.get("https://api64.ipify.org?format=json").json()["ip"]
        loc = requests.get(f"https://ipapi.co/{ip}/json/").json()
        city = loc.get("city", "unknown")
        region = loc.get("region", "unknown")
        country = loc.get("country_name", "unknown")
        speak(f"You're in {city}, {region}, {country}.")
    except:
        speak("Couldn't fetch your location.")

def play_guess_game():
    number = random.randint(1, 20)
    speak("🎲 Let's play a game! I'm thinking of a number between 1 and 20.")
    speak("Try to guess it. Say or type your number!")

    attempts = 0  

    while True:
        try:
            guess = int(input("🔢 Your guess: "))
            attempts += 1

            if guess == number:
                speak(f"🎉 Congratulations! You guessed it in {attempts} attempt(s)!")
                print(f"✅ Correct! The number was {number}.")
                break
            elif guess < number:
                speak("📉 Too low! Try a higher number.")
                print("Hint: Try a higher number.")
            else:
                speak("📈 Too high! Try a lower number.")
                print("Hint: Try a lower number.")

        except ValueError:
            speak("⚠️ Please enter a valid number between 1 and 20.")
            print("Invalid input. Please enter an integer.")

def speak(text):
    try:
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)
        engine.setProperty('rate', 180)
        print("Speaking:", text)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
    except Exception as e:
        print("Speak Error:", e)

def aiProcess(command):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Nexa skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content

def processCommand(c):
    if any(phrase in c.lower() for phrase in ["hello", "hi", "hey", "hey nexa","greet me"]):
        hour = datetime.datetime.now().hour
        greeting = "Good morning" if 5 <= hour < 12 else "Good afternoon" if 12 <= hour < 18 else "Good evening"
        speak(f"{greeting}! I'm Nexa. How can I help?")
        return 
      
    if "open google" in c.lower():
        webbrowser.open("https://google.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")

    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
        
    elif "who is" in c.lower() or "what is" in c.lower():
     try:
        topic = c.lower().replace("who is", "").replace("what is", "").strip()
        summary = wikipedia.summary(topic, sentences=2)
        speak(summary)
     except Exception as e:
        speak("Sorry, I couldn't find anything on that.")    
        
    elif "open notepad" in c.lower():
     os.system("notepad")
    elif "open calculator" in c.lower():
     os.system("calc")   
    elif "open camera" in c.lower():
     os.system("start microsoft.windows.camera:") 
    elif "open settings" in c.lower():
     os.system("start ms-settings:")
  
    
    elif "send message to" in c:
        for name in contacts:
            if name in c:
                phone_number = contacts[name]
                speak(f"What message should I send to {name}?")
                message = listen()

                now = datetime.datetime.now()
                hour = now.hour
                minute = now.minute + 2
                if minute >= 60:
                    minute -= 60
                    hour = (hour + 1) % 24

                try:
                    speak(f"Sending message to {name} in 2 minutes.")
                    pywhatkit.sendwhatmsg(phone_number, message, hour, minute)
                    speak("Message scheduled. Please keep your browser open and don't move your mouse.")
                except Exception as e:
                    print("WhatsApp Error:", e)
                    speak("Failed to send the WhatsApp message.")
                return

    elif "joke" in c or "tell me a joke" in c:
        joke = pyjokes.get_joke()
        speak(joke)
  
     
    elif "where am i" in c.lower() or "location" in c.lower():
     get_location() 
     
    elif "mute" in c.lower():
     set_volume_mute(True)
     speak("Muted the volume")

    elif "unmute" in c.lower():
     set_volume_mute(False)
     speak("Unmuted the volume")   
     
    elif "screenshot" in c.lower():
     pyautogui.screenshot("nexa_screenshot.png")
     speak("Screenshot taken and saved.")  

    elif "play a game" in c.lower() or "guess the number" in c.lower():
     play_guess_game()

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, I couldn't find that song.")

    elif "news" in c.lower():
        print("News command recognized.")
        try:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
            print(f"Request status: {r.status_code}")
            if r.status_code == 200:
                data = r.json()
                articles = data.get('articles', [])
                print(f"Found {len(articles)} articles.")
                speak("Here are the top headlines.")
                for article in articles[:5]:
                    print("Speaking:", article['title'])
                    speak(article['title'])
            else:
                speak("Sorry, I couldn't fetch the news right now.")
                print("Failed to fetch news, status code:", r.status_code)
        except Exception as e:
            speak("Error while fetching news.")
            print("News Error:", e)

    elif any(phrase in c.lower() for phrase in ["time", "current time", "what time", "what's the time"]):
        now = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")

    elif any(phrase in c.lower() for phrase in ["date", "today", "what's the date", "current date"]):
        today = datetime.datetime.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")
    
    elif "search for" in c.lower():
        query = c.lower().replace("search for", "").strip()
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        speak(f"Here are the results for {query}")

    elif "weather" in c.lower():
        match = re.search(r"weather\s+(in|of|at)?\s*(.+)", c.lower())
        if not match:
            speak("Please tell me which city's weather you want.")
            return
        city = match.group(2).strip().title()
        api_key = os.getenv("WEATHER_API_KEY")
        # api_key = "ddf8839a809be4d0444b4a84ea1423e3"
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        try:
            res = requests.get(url)
            weather = res.json()
            if weather.get("main"):
                temp = weather["main"]["temp"]
                desc = weather["weather"][0]["description"]
                response = f"The temperature in {city} is {temp} degrees Celsius with {desc}."
                print(response)
                speak(response)
            else:
                speak(f"Sorry, I couldn't get the weather for {city}.")
        except Exception as e:
            speak("Error getting weather.")
            print("Weather API Error:", e)

    else:
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Nexa.....")
    while True:
        r = sr.Recognizer()
        print("recognizing......")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)

            if word.lower() == "hello":
                speak("Ya Please Tell me What To do")
                with sr.Microphone() as source:
                    print("Nexa Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print("Command:", command)
                    processCommand(command)
        except Exception as e:
            print("Error:", e)
