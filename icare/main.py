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
        audio = r.listen(source, 10, 10)  # listen for the audio via source
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
    if there_exists(["what is your name","what's your name","tell me your name"]):
        speak("My Name is Test. what's your name?")
    if there_exists(["my name is"]):
        speak("nice to meet you i will remember that ,so do you want to eat or watch something!")
        
    if there_exists(["eat"]):
        speak("Here are some of the foods I recommend for you today")
    
    if there_exists(["watch"]):
        speak("What if we remember the old days and watch the Titanic ! ")
    
    if there_exists(["what's the time","tell me the time","what time is it","what is the time"]):
        speak(ctime())

    if there_exists(['hey','hi','hello','Good morning','Good afternoon','Good evening']):
        speak("What's your mood today?")

    elif there_exists(['happy','nice']):
        speak("What if we go to walk ?")

    elif there_exists(["sick","got cold","got a temperatare"]):
        speak('Do you want me to call a doctor ?')
    elif there_exists(['hungry']):
        speak('Do you want to eat some delicious food')
    elif there_exists(["bad","sad","ugly","angry","i'm not ok","stressed","upset"]):
        speak('what if we read some books !')


    if "yes" in voice_data:
        print('call doctor')
    elif "no" in voice_data:
        speak('so try to eat some healthy food')

    if there_exists(["it's good outside"]):
        search_term = voice_data.split("for")[-1]
        url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
        webbrowser.get().open(url)
        speak("I think it's a good day,but you can do some excercise in you'r room")


    if'search'in voice_data:
        search = record_audio('what do you want to search for ?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        speak('Here is what I found for ' + search)
    
    if there_exists(["what is my exact location"]):
        url = "https://www.google.com/maps/search/Where+am+I+?/"
        webbrowser.get().open(url)
        speak("You must be somewhere near here, as per Google maps")
    if there_exists(["exit", "quit", "goodbye"]):
        speak("Have a nice day ,good bye")
        exit()


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

