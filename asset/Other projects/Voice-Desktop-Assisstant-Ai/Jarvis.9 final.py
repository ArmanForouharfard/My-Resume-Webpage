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
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}\n")
            return query

        except Exception as e:
            print("Say that again please...")
            speak("Say that again please...")   
                
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

#not working
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
            
    # the web links
            
    if 'wikipedia' in query.lower():
        speak('Searching wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences = 2)
        print(results)
        speak(results)
        
    elif 'open google' in query.lower():
        url = "https://www.google.com/"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        speak(f"Opening google now")
        print(f"Opening google now")
        
    elif 'open maps' in query.lower():
        url = "https://www.google.com/maps"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        speak(f"Opening google map now")
        print(f"Opening google map now")
        
    #elif 'open google on mirosoft edge' in query.lower():
    #    url = "google.com"
    #    msedge_path= 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe %s'
    #    webbrowser.get(msedge_path).open(url)   
     
    elif 'open gmail' in query.lower():
        url = "mail.google.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        speak(f"Opening gmail now")
        print(f"Opening gmail now")
        
    elif 'open youtube' in query.lower():
        url = "youtube.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        speak(f"Opening youtube now")
        print(f"Opening youtube now")
        
    elif 'open facebook' in query.lower():
        url = "facebook.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        speak(f"Opening facebook now")
        print(f"Opening facebook now")
        
    elif 'open twitter' in query.lower():
        url = "twitter.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        speak(f"Opening twitter now")
        print(f"Opening twitter now")
        
    elif 'open instagram' in query.lower():
        url = "instagram.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        speak(f"Opening instagram now")
        print(f"Opening instagram now")
        
    elif 'open w3schools' in query.lower():
        url = "w3schools.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        speak(f"Opening w3schools now")
        print(f"Opening w3schools now")
        
    elif 'open overflow' in query.lower():
        url = "stackoverflow.com"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        speak(f"Opening overflow now")
        print(f"Opening overflow now")
        
# opening system's applications
     
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
        
    elif 'open code' in query.lower():
        codePath = "C:\\Users\\lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)
        speak(f"opening visualcode now")
        print(f"opening visualcode now")
     
    elif 'open photoshop' in query.lower():
        codePath = "C:\\Program Files\\Adobe\\Adobe Photoshop CC 2019\\Photoshop.exe"
        os.startfile(codePath)
        speak(f"opening photoshop now")
        print(f"opening photoshop now")
        
    elif 'open phantom pain' in query.lower():
        codePath =  "C:\Games\Metal Gear Solid V - The Phantom Pain\mgsvtpp.exe"
        os.startfile(codePath)
        speak(f"opening metal gear solid phantom pain now")
        print(f"opening metal gear solid phantom pain now")
     
# Answering Questions (Writen by the programmer!)
    
    elif 'who are you' in query.lower():
        speak("i'm a voice assistent AI")
        print("i'm a voice assistent AI")
        
    elif 'who is your creator' in query.lower():
        speak("Arman, Forouharfard, a student of software Development programmed me. his perpose, was to make an internet of thing Ai!")
        print("Arman, Forouharfard, a student of software Development programmed me. his perpose, was to make an internet of thing Ai!")
     
     
# Sending E-mail
    # this part is not working!    
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
     
# Find my location
    # this is just a sample, it needs a new type of code still working on it
    elif 'find my location' in query.lower():
        url = "https://www.google.com/maps/place/35%C2%B043'27.3%22N+51%C2%B022'27.9%22E/@35.7242459,51.371847,17z/data=!3m1!4b1!4m7!1m2!10m1!1e2!3m3!8m2!3d35.7242416!4d51.3744219?entry=ttu"
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open(url)
        speak(f"Sir, you're now at this Location")
        print(f"Sir, you're now at this Location")
      
# exit 

    elif 'thank you' in query.lower():
        speak("You're welcome!")
        print("You're welcome!")
        exit()
     
    elif 'goodbye' in query.lower():
        speak("Goodbye!")
        print("Goodbye!")
        exit()
       
# else incase your sences were not clear to AI
        
    else:
        speak("Sorry, I didn't understand that.")
        print("Sorry, I didn't understand that.")

if __name__ == "__main__":
    while True:
        main() 
