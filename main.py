#pip install speechrecognition
#python -m pip install pyaudio
#pip install gTTS
#pip install playaudio

#importing libraries

import speech_recognition as sr
import os
import time
import webbrowser
import random
import playsound
from gtts import gTTS
from time import ctime

def record_audio(ask=False):
    if ask:
        print(ask)
    r=sr.Recognizer()
    print('listening')
    with sr.Microphone() as source:
        audio=r.listen(source)
    voice_data=''
    try :
        voice_data=r.recognize_google(audio)
        print('You said :' + voice_data)
    except sr.UnknownValueError:
        speak('Cant not understand what you saying')
    except sr.RequestError:
        speak('Service is error')

    return voice_data


def speak(audio_string):
    tts=gTTS(text=audio_string,lang='en')
    r=random.randint(1,10000000)
    audio_file='audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)


def respond(voice_data):
    if 'what is your name' in voice_data:
        speak('My name is SIRO')
    if 'what time is it' in voice_data:
        speak(ctime())
    if 'open Google' in voice_data:
        speak('what do you want to search')
        search=record_audio('what do you want to search')
        url='https://google.com/search?q='+ search
        webbrowser.get().open(url)
        speak('Here is what i found ' + search)
    if 'exit' in voice_data:
        exit()

time.sleep(1)
speak('How can I help You')
while 1:
    voice_data = record_audio()
    respond(voice_data)
