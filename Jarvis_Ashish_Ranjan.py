from typing import re

import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import speech_recognition as sr
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning")
    elif 12 <= hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Ashish Ranjan personal Assistant sir , Please tell me how may i help you ")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am Listening........")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing.......")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:

        print("Say that again please......")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('hostelenquiry@hmail.com', 'Monal@123')
    server.sendmail('hostelenquiry@gmail.com',to,content)
    server.close()


if __name__ == "__main__":

    WishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching on Wikipedia.....')
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(result)
            speak(result)


        elif 'youtube' in query:
            speak('Searching on YouTube..... ')
            webbrowser.open("https://www.youtube.com/results?search_query=" + query)


        elif 'google' in query:
            webbrowser.open("google.com")

        elif 'stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


        elif 'play music' in query:
            music_dir = 'E:\\hd video'
            songs = os.listdir(music_dir)
            a = random.choice(songs)
            os.startfile(os.path.join(music_dir, a))


        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")

        elif 'open code' in query:
            path1 = 'C:\\Program Files (x86)\\Dev-Cpp\\devcpp.exe'
            os.startfile(path1)

        elif 'open pycharm' in query:
            path2 = 'C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.1\\bin\\pycharm64.exe'
            os.startfile(path2)

        elif 'send email' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                to = "aviashishranjan@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry i am not able to send email right now")
