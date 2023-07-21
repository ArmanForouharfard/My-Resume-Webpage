import pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import random
import subprocess
from playsound import playsound
import smtplib

# the main codes starts from here
print("Initializing Jarvis")

MASTER = "Arman"

# the Ai's voice engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
# 0 is for Male voice engine and 1 is for Female engine

# Speck function will pronouce the string which is passed to it
def speak(text):   
    engine.say(text)
    engine.runAndWait()
     
# This function will wish you as per the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour <12:
        speak("Good Morning" + MASTER)
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon" + MASTER)
        
    else:
        speak("Good Evening" + MASTER)

    speak("I am Jarvis. a Voice Desktop assistant artificial intelligence")
    speak("How may i help you?")

# this function will take command from the micrphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
       print("Listening...")
       audio = r.listen(source)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}\n")
        
    except Exception as e:
        print("Say that again please...")
        query = None
        
    return query    
                
def play_music():
    music_dir = "C:\\Users\\lenovo\\Music\\My Favorite"
    songs = [file for file in os.listdir(music_dir) if file.endswith(('.mp3', '.mp4'))]
    print("Found the following music files:")
    for song in songs:
        print(f"- {song}")
    if songs:
        selected_song = random.choice(songs)
        print(f"Playing {selected_song}")
        subprocess.call(['start', os.path.join(music_dir, selected_song)], shell=True)
    else:
        print("No music files found.")
        result = subprocess.call(['start', os.path.join(music_dir, selected_song)], shell=True)
        print(f"subprocess.call() returned {result}")    
     
    
def tell_time():
    now = datetime.datetime.now()
    str_time = now.strftime("%H:%M:%S")
    print(f"The current time is {str_time}")

def sendemail(to,content):
        server = smtplib.SMTP('smpt.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('arman.forouharfard@gmail.com', 'password')
        server.sendmail("armanforouharfard@gmail.com", to, content)   
        server.close()
      
def main():
        
    #Main program starts here...
    wishMe()
    query = takeCommand()
            
    if 'wikipedia' in query.lower():
        speak('Searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences = 2)
        print(results)
        speak(results)
        
    elif 'open google on chrome' in query.lower():
        url = "google.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        
    elif 'open google on mirosoft edge' in query.lower():
        url = "google.com"
        msedge_path= 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe %s'
        webbrowser.get(msedge_path).open(url)   
    
    elif 'open gmail' in query.lower():
        url = "mail.google.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        
    elif 'open youtube' in query.lower():
        url = "youtube.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        
    elif 'open facebook' in query.lower():
        url = "facebook.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        
    elif 'open twitter' in query.lower():
        url = "twitter.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        
    elif 'open instagram' in query.lower():
        url = "instagram.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        
    elif 'open w3schools' in query.lower():
        url = "w3schools.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        
    elif 'open stackoverflow' in query.lower():
        url = "stackoverflow.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
    
    elif 'play music' in query.lower():
        music_dir = "C:\\Users\\lenovo\\Music\\My Favorite"
        songs = [file for file in os.listdir(music_dir) if file.endswith(('.mp3', '.mp4'))]
        print("Found the following music files:")
        for song in songs:
            print(f"- {song}")
        
    elif 'what time is it' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir, the time is {strTime}")
        print(f"Sir, the time is {strTime}")
        
        #again this part is not working!    
    elif 'email to arman' in query.lower():
        try:
            speak("What should i send?")
            content = takeCommand()
            to = "armanforouharfard@gmail.com"
            sendemail(to, content)
            speak("Email has been sent successfully")
        except Exception as e:
            print(e) 
            speak("Sorry my friend harry bhai. I am not able to send this email")   
        
        #open visual code (passed)
    elif 'open code' in query.lower():
        codePath = "C:\\Users\\lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
        
    elif 'open photoshop' in query.lower():
        codePath = "C:\\Program Files\\Adobe\\Adobe Photoshop CC 2019\\Photoshop.exe"
        os.startfile(codePath)
        
    elif 'who are you' in query.lower():
        speak("i'm a voice assistent AI")
        print("i'm a voice assistent AI")
        
    elif 'who created you' in query.lower():
        speak("Arman Forouharfard, a student of software Development programmed me. his perpose was to create an internet of thing Ai!")
        print("Arman Forouharfard, a student of software Development programmed me. his perpose was to create an internet of thing Ai!")
    
    elif 'thank you' in query.lower():
        speak("You're welcome!")
        print("You're welcome!")
    
    elif 'goodbye' in query.lower():
        speak("Goodbye!")
        print("Goodbye!")
        exit()
        
    else:
        speak("Sorry, I didn't understand that.")
        print("Sorry, I didn't understand that.")

if __name__ == "__main__":
    while True:
        main()