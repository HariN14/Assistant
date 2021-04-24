import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import sys
import calc
import requests



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

               
def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning maam!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon maam!")  

    else:
        speak("Good Evening maam!")
    speak("I am Zen, Your personal voice assistant. How may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=7)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ranasakshi473@gmail.com', '')
    server.sendmail('ranasakshi473@gmail.com', to, content)
    server.close()

def addsub():
    os.system('python calc.py')

def playquiz():
    os.system('python quiz.py')

def pygame():
    os.system('python tiktac.py')    
    


if __name__ == "__main__":
    wishMe()
  
    while True:
        query = takeCommand().lower()

    #logic for tasks based on query
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")    
        
        elif 'open google' in query:
            webbrowser.open("google.com")  

        elif 'open stack over flow' in query:
            webbrowser.open("stackoverflow.com")    

        elif 'play music' in query:
            music_dir = 'C:\\Users\\sunil rana\\Desktop\\bollywood songs\\new songs 2017'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            speak(f"The time is {strTime}")

        elif 'open code' in query: 
            codePath = "C:\\Program Files\\Microsoft VS Code\\Code.exe" 
            os.startfile(codePath)  

        elif 'open python' in query: 
            pypath = "C:\\Users\\sunil rana\\AppData\\Local\\Programs\\Python\\Python38-32\\python.exe"
            os.startfile(pypath)

        elif 'How are you' in query:
            speak("I am fine")

        elif 'what\'s up' in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs)) 

        elif 'nothing' in query or 'exit' in query or 'bye' in query:
            speak("okay")
            speak("Bye maam , have a good day")
            sys.exit() 

        elif 'remember that' in query:
            query = query.split(" ")
            remember_text = query[3]
            speak("got it")

        elif 'am i forgetting something' in query:
            speak("Yes" + remember_text + ".")  

        elif "shutdown" in query:
            os.system("shutdown /s /t 1")  

        elif 'open calculator' in query:
            speak("opening calculator...")
            addsub()        
   
        elif 'open quiz' in query:
            speak("ok If u say so...")
            playquiz()

        elif 'email to sakshi' in query:
            try:
                speak("what should I say")
                content = takeCommand()
                to = "ranasakshi473@gmail.com"
                sendEmail(to, content)
                speak("email has been sent")

            except Exception as e:
                print(e)
                speak("sorry maam! i am not able to send this email at the moment")

        elif 'who are you' in query:
            speak("I am Zen and i want love")

        elif 'i want to play' in query:
            speak("okay")
            pygame()        

       
        
    
            
	    