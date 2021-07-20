import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os   


engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')

# print(voices)

engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <=12:
        speak("Good morning!")

    elif hour>=12 and hour <18:
        speak("Good Aftenoon!")  

    else:
        speak("Good Evening")

    speak("I am your AI assistant. I am here to help you")         

def takeCommand():
#It takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening...")
         r.pause_threshold = 1 
         audio = r.listen(source)

    try:
         print('Recognising...')
         query = r.recognize_google(audio, language='en-in')
         print(f"You said:{query}\n")

    except Exception as e:
         print(e)   #print type as error
         print("Say that again please....")
         return "None"
    return query


if __name__== "__main__":
    wishMe()
    while True:       
        query = takeCommand().lower()

        #For executing tasks
        if 'wikipedia' in query:
            speak('Searching wikipedia....')
            query = query.replace("wikipedia","")

            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music'in query:
            music_dir = 'F:\\Audio\\Lover'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            


