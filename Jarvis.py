import speech_recognition as sr
import webbrowser
import pyttsx3
import requests

# Initialize the recognizer and the TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# API key for the news service
news_api = "72b16bdff07642a2b0bc434a44cf0920"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    try:
        c = c.lower()
        if "open google" in c:
            webbrowser.open("https://google.com")
        elif "open facebook" in c:
            webbrowser.open("https://facebook.com")
        elif "open linkedin" in c:
            webbrowser.open("https://linkedin.com")
        elif "open youtube" in c:
            webbrowser.open("https://youtube.com")
        elif "news" in c:
            r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news_api}")
            if r.status_code == 200:
                data = r.json()
                articles = data.get("articles", [])
                if articles:
                    for article in articles[:5]:  # Read only the first 5 articles
                        title = article.get('title', 'No Title')
                        print(title)
                        speak(title)
                else:
                    speak("I couldn't find any news articles.")
            else:
                speak(f"Failed to retrieve news, status code {r.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")
        speak(f"An error occurred: {e}")

if __name__ == "__main__":
    speak("Initializing Jarvic...")
    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                print("Listening for activation word...")
                audio = recognizer.listen(source, timeout=4, phrase_time_limit=2)
                word = recognizer.recognize_google(audio)
                print(f"Heard word: {word}")

                if word.lower() == "jarvis":
                    speak("Yes?")
                    print("Jarvis Active....")
                    audio = recognizer.listen(source, timeout=4, phrase_time_limit=2)
                    command = recognizer.recognize_google(audio)
                    print(f"Heard command: {command}")
                    processCommand(command)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
