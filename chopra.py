import speech_recognition as sr
import pyttsx3
import datetime

import webbrowser


speech = sr.Recognizer()
try:
    engine = pyttsx3.init()
except ImportError:
    print('Requested driver is not found')
except RuntimeError:
    print('driver faild to intilize')

voices = engine.getProperty('voices')
''''
for voice in voices:
    print(voice.id)
'''
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate)


def speak_text_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()

def read_voice_cmd():
    voice_text = ''
    print('I am listening you...')

    with sr.Microphone() as source:
        audio = speech.listen(source)

    try:

        voice_text = speech.recognize_google(audio)

    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print('Network error.')
    return voice_text


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour=int(datetime.datetime.now().hour)


    if hour>=0 and hour<12:
        speak('Good Morning Arafat.')

    elif hour>=12 and hour<= 17:
        speak('Good Afternoon Arafat.')

    elif hour>17 and hour<=19:
        speak('Good evening Arafat.')

    else:
        speak('Good night Arafat.')


if __name__=='__main__':
    wishMe()
    speak_text_cmd('Hi, I am Chopra, Your artificial friend. How can i help you?')


    while True:
        voice_note=read_voice_cmd()
        print('cmd:{}'.format(voice_note))


        if 'hello' in voice_note:
            speak_text_cmd('Hello Arafat. How can i help you?')
            continue


        elif 'who are you' in voice_note:
            speak_text_cmd('I am Chopra. An  artificial friend of Mr. Arafat, Mr. Arafat created me on 30 december, '
                           '2020.')
            continue

        elif 'what is your name' in voice_note:
            speak_text_cmd('I am Chopra, Your artificial friend.')
            continue



        elif 'goodbye Chopra' in voice_note:
            speak_text_cmd('Bye Mr. Arafat. Happy to help you. Have a good day.')
            exit()




        elif 'open YouTube' in voice_note:
            speak_text_cmd('opening youtube for you.')
            webbrowser.open('https://www.youtube.com/')

        elif 'open Twitter' in voice_note :
            speak_text_cmd('opening Twitter for you.')
            webbrowser.open('https://www.twitter.com/home')