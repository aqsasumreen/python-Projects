import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pyautogui
import openai
openai.api_key = "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"

# What is the meaning of SAPI 5?
# windows me jo in bulit voices hti hain unko use kr skty hain.
# Microsoft Speech API (SAPI5) is the technology for voice recognition
# and synthesis provided by Microsoft. Starting with Windows XP, it ships as part of the Windows OS.
# speaker =win32com.client.Dispatch("SAPI.SpVoice")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
# System me  aik female voice hti hy aik male ,,
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good AfterNoon!")
    else:
        speak("Good Evening!")
    speak("Im Jarvis AI Mam. Please tell me How may I help You!")


def takecommand():
    # it takes microphone input from user and returns str output..
    # AGR BOLNY K DRMIYAN aik sec ka gap ho tou wo phrase ko complete na kr de.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said ", query)
    except Exception as e:
        print(e)
        print("say that again please..")
        return "None"
    return query


if __name__ == '__main__':
    wishMe()
    while True:
        query = takecommand().lower()
        if 'wikipedia' in query:
            speak("Searching for Wikipedia...")
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music ' in query:
            music_dir = 'E:\\BTS'
            songs = os.listdir(music_dir)
            print(songs)
            var = random.randint(1, 10)
            os.startfile(os.path.join(music_dir, songs[var]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
            speak(f"Mam , the time is{strTime}")
        elif 'open code' in query:
            code1 = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(code1)
        elif 'open pyCharm' in query:
            code2 = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.3.2\\bin\\pycharm64.exe"
            os.startfile(code2)
        elif 'screenshot' in query:
            img = pyautogui.screenshot()
            img.save("SS1.png")
            speak("screenshot taken")



# The pause_threshold value is the number of seconds the system will take
# to recognize the voice after the user has completed their sentence.
