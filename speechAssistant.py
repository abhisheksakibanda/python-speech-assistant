import speech_recognition as sr
import time
import webbrowser
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()


def recordAudio(ask=False):
    with sr.Microphone() as source:
        if ask:
            aliceSpeak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
            aliceSpeak(voice_data)
        except sr.UnknownValueError:
            aliceSpeak('Sorry, I did not get that')
        except sr.RequestError:
            aliceSpeak('Sorry, my speech service is down')
        return voice_data


def aliceSpeak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 10_000_000)
    audio_file = f'audio-{str(r)}.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def Respond(voice_data):
    if 'what is your name' in voice_data:
        aliceSpeak('My name is Alice')
    if 'what time is it' in voice_data:
        aliceSpeak(ctime())
    if 'search' in voice_data:
        search = recordAudio('What do you want to search for?')
        url = f'https://www.google.co.in/search?q={search}'
        webbrowser.get().open(url)
        aliceSpeak(f'Here is what I found for {search}')
    if 'find location' in voice_data:
        location = recordAudio('What is the location you want to find?')
        url = f'https://www.google.com/maps/search/?api=1&query={location}'
        webbrowser.get().open(url)
        aliceSpeak(f'Here is the location of {location}')
    if 'exit' in voice_data:
        aliceSpeak('Have a nice day!')
        exit()


time.sleep(1)
aliceSpeak('How may I help you?')
print('I can help you to: \n1.Search \n2.Find Location \n3.Tell you the time')
print("Tell 'exit' to stop the application")
while 1:
    voice_data = recordAudio()
    Respond(voice_data)
