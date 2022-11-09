import speech_recognition as sr # recognise speech
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
from time import ctime # get time details
import webbrowser # open browser
import ssl
import certifi
import time
import os # to remove created audio files
import datetime
import requests, json

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
r = sr.Recognizer() # initialise a recogniser

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

def there_exists1(terms):
    for term in terms:
        if term in voice_data1:
            return True


# listen for audio and convert it to text:
def record_audio(ask=False):
    with sr.Microphone() as source: # microphone as source
        voice_data = ''
        if ask:
            speak(ask)
        audio = r.listen(source, 5, 5)  # listen for the audio via source
        print("Done Listening")
        
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            speak('I did not get that')
        except sr.RequestError:
            speak('Sorry, the service is down') # error: recognizer is not connected
        return voice_data.lower()

# get string and make a audio file to be played
def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    #print(audio_string) # print what app said
    os.remove(audio_file) # remove audio file

def respond(voice_data):
    if'what is your name'in voice_data:
        speak('My Name is Test')
    if there_exists(["what's the time","tell me the time","what time is it","what is the time"]):
        speak(ctime())
    if 'hello'in voice_data:
        speak("What's your mood today?")
        voice_data = record_audio() 
        return mood(voice_data)
    if'search'in voice_data:
        search = record_audio('what do you want to search for ?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('Here is what I found for ' + search)
    if 'say hello'in voice_data:
        speak('hello')   
    if there_exists(["exit", "quit", "goodbye"]):
        speak("going offline")
        exit()

def there_exists1(terms):
    for term in terms:
        if term in voice_data1:
            return True
def mood(voice_data):
    if 'happy' in voice_data:
        speak("What if we go to walk ?")
        if 'Is the weather good today to walk ?' in voice_data:
            speak("I think it's good but if isn't you can do some excercise in you'r room")
        #elif there_exists(["bad","sad","ugly","angry","i'm not ok","stressed","upset"]):
    if there_exists(["hungry"]):
        speak('Do you want to eat some delicious food')
    if there_exists(["sick","got cold","got a temperatare"]):
        speak('Do you want me to call a doctor ?')
        if "yes" in voice_data:
            print('call doctor')
        else:
            speak('Try to eat some healthy food')

time.sleep(1)
currentTime = datetime.datetime.now()
currentTime.hour
if currentTime.hour < 12:
    speak("Good morning")
    print('Good morning.')
elif 12 <= currentTime.hour < 18:
    speak("Good afternoon")
    print('Good afternoon.')
else:
    speak("Good evening")
    print('Good evening.')


while 1:
    voice_data = record_audio() # get the voice input
    respond(voice_data) # respond

