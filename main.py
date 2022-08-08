import pyttsx3 as p
import speech_recognition as sr
import webbrowser as web
import pyautogui as pt

def speak(text):
    a = p.init()
    a.say(text)
    a.runAndWait()

def Listen_user():
    b = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        # b.adjust_for_ambient_noise(source)
        audio = b.listen(source)

    try:
        print("recoginzing...")
        query = b.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print("Say that again...")
        return None

    return query

while True:

    speak("Hello  world!")
    command = Listen_user().lower()

    if 'open google' in command:
        web.open("https://www.google.co.in/")

    elif 'open youtube' in command:
        web.open("https://www.google.co.in/")

    elif 'open google' in command:
        web.open("https://www.google.co.in/")

    elif 'open google' in command:
        web.open("https://www.google.co.in/")

    elif 'open google' in command:
        web.open("https://www.google.co.in/")

    elif 'open google' in command:
        web.open("https://www.google.co.in/")

    elif 'increase' in command:
        pt.press("volumeup")

    elif 'decrease' in command:
        pt.press("volumedown")

    elif 'mute' in command:
        pt.press("volumemute")

    elif 'break' in command:
        speak("See u later sir")
        quit()

    