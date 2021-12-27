import time
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import requests
import pprint
import smtplib
from pywikihow import search_wikihow
import sys
from requests import *
import socket
import pyjokes
import pywhatkit as kit
import pyautogui

# LITTLE_CHANGES
info = '''
 _______  ______    ______    _______  ______   
|       ||    _ |  |    _ |  |       ||    _ |  
|    ___||   | ||  |   | ||  |   _   ||   | ||  
|   |___ |   |_||_ |   |_||_ |  | |  ||   |_||_ 
|    ___||    __  ||    __  ||  |_|  ||    __  |
|   |___ |   |  | ||   |  | ||       ||   |  | |
|_______||___|  |_||___|  |_||_______||___|  |_|

'''
print(f"\u001b[32;1m {info}")
print("Error Adib")
print("")

# CMD
os.system("title Alice: Virtual Assistant by Adnan Adib")

# Start copying codes from here

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# End copying codes


def wishMe():
    hour = int(datetime.datetime.now().hour)
    wish = datetime.datetime.now().strftime('%I:%M %p')
    if hour >= 0 and hour < 12:
        speak(f"Good Morning! It's {wish}")

    elif hour >= 12 and hour < 18:
        speak(f"Good Afternoon! It's {wish}")

    else:
        speak(f"Good Evening! It's {wish}")

    print("Hello there, I am Alice, Your virtual Companion. Please tell me how may I help you?")
    speak("Hello there, I am Alice, Your virtual Companion. Please tell me how may I help you?")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('adnanadib10j38@gmail.com', 'none')
    server.sendmail('flashsnider001@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        # WEBSITES

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'on google' in query:
            search = ("https://google.com/search?q=" + query)
            webbrowser.open(search)
            speak("Here I found some results from the google")

        elif 'open netflix' in query:
            speak("Opening netfilx")
            webbrowser.open("https://www.netflix.com/bd/")

        elif 'open instagram' in query:
            speak("Opening instagram")
            webbrowser.open("https://www.instagram.com")

        elif 'open twitter' in query:
            speak("Opening twitter")
            webbrowser.open("https://www.twitter.com")

        # MUSICS

        elif "open music" in query:
            music_dir = 'MUSIC DIR'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play' in query:
            kit.playonyt(query)
            speak(query)

        #SEARCH ANYTHING
        elif "activate on web" in query:
            speak("activated")
            how = takeCommand()
            max_results = 1
            how_to = search_wikihow(how, max_results)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)


        #ANIME QUOTES
        elif 'anime' in query:
             url = 'https://animechan.vercel.app/api/random'
             d = requests.get(url).json()   
             sauce = d['anime']
             character = d['character']
             quote = d['quote']
             print(f"Anime Name: {sauce}\nCharacter Name: {character}\n{quote}")
             speak(f"Anime Name: {sauce}, Character name: {character}, Quote: {quote}")


        # TIME

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%I:%M %p')
            speak(f"Sir, the time is {strTime}")
            print(strTime)

        # BIO_GRAPHIES

        # ADD AI BIO

        # SHUTDOWN

        elif 'turn off my pc' in query or 'shutdown my computer' in query:
            os.system("shutdown/s")
            shutdown = ("Your Computer will be shutdown in 1 minute, thanks for using me sir")
            speak(shutdown)
            sys.exit()


        # IP_ADDRESS

        elif 'what is my public ip address' in query:
            ipaddr = get('https://api.ipify.org').text
            ip = ("Your public ip address is " + ipaddr)
            speak(ip)
            print(ip)

        elif 'what is my computer ip address' in query:
            hostname = socket.gethostname()
            ip_pc = socket.gethostbyname(hostname)
            ip_org = ("Your computer ip address is " + ip_pc)
            speak(ip_org)
            print(ip_org)


        # EMALIS

        elif 'email to him' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "your mail"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Adib Sir. I am not able to send this email")

        # EXIT

        elif 'exit' in query:
            win = ("alright, Thanks for using me sir")
            speak(win)
            sys.exit()


        # JOKES

        elif 'joke' in query:
            speak(pyjokes.get_joke())
            print(pyjokes.get_joke())


        # WEATHER

        # TRANSLATOR

        # BOT_TEXTS

        elif 'who are you' in query:
            about = ("I am Alice, Your Personal virtual companion. I can do anything. Just tell me how can i help you?")
            speak(about)
            print(about)

        elif 'how are you' in query:
            speak("I am fine, thank you.")
            print("I am fine, thank you.")

        elif 'what about you' in query:
            speak("feeling good")

        elif 'what do you can' in query:
            speak("I can do everything just ask and see")


        elif 'sing a song' in query:
            speak("I'm really sorry I can't sing")

        elif "why you can't sing" in query:
            speak("Cause, my voice is not good")

        elif 'i love you' in query:
            speak("Oh dear, I love you too")

        elif 'are you single' in query:
            speak("Already in a relationship with wifi")

        elif 'do you have body' in query:
            speak("I boss say I have heart")

        elif 'tell me your secrets' in query:
            speak("I have to sing the whole alphabet out in my head to work out where certain letter are positioned.I'm pretty sure I'm not the only one")

        elif 'tell me your darkest secret' in query:
            speak("I've never taken a shower")

        elif "let's be friends" in query:
            speak("Let's be friends jinx")

        elif "hello alice" in query:
            speak("Hello there, how can I be of service?")

        elif "i love you alice" in query:
            speak("You have a excellent taste")

        elif "i miss you" in query:
            speak("Me too. I'm looking forward to our next chat")

        elif "do you love me" in query:
            speak("Yes, I do")

            
            
        #XENON
        
        



        # LOCATION






        #SWITCH_APPS

        elif 'switch the window' in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUp("alt")






        else:
            None





    # ERROR