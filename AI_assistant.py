import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os   
import smtplib
import pyjokes
from ecapture import ecapture as ec


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



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('yore_email@gmail.com','email_password')
    server.sendmail('your_email@gmail.com',to,content)
    server.close()



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

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')   
            speak(f"The time is {strTime}")


        elif 'open code' in query:
             codePath = "C:\\Users\\Asus\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
             os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("What should I send to Ayush")
                content = takeCommand()
                to = 'ayushunplugged22@gmail.com';
                sendEmail(to,content)
                speak('Email has been sent!')

            except Exception as e:
                print(e)
                speak("Sorry!, I am not able to send this email at this moment")
                              
        elif 'joke' in query:
            speak(pyjokes.get_joke())


        elif "who are you" in query:
            speak("I am your virtual assistant created by Ayush Narayan") 

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Ayush Camera ", "img.jpg") 


        elif "how are you" in query:
            speak("I am fine Thank you for checking on me")       


        elif 'exit' in query:
             exit()       








