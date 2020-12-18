import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import time
import sys
from wappdriver import WhatsApp
import pyautogui





engine = pyttsx3.init('sapi5')

voices= engine.getProperty('voices') #getting details of current voice

engine.setProperty('voice', voices[1].id)
print(voices[1].id)

def speak(audio):
    engine.say(audio) 
    engine.runAndWait() #Without this command, speech will not be audible to us.


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afernoon!")
    else:
        speak("Good Evening!")

    speak("I am Ella sir. Please tell me how may I help you") 

def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        r.energy_threshold = 2000
        audio = r.listen(source)
    
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

if __name__ == "__main__":
    wishme()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'thank you' in query: #for closing while loop using 'thank you'
            speak('thank you sir')
            print('Thank you Sir')
            break
        
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/?gl=IN")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")

        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com")

        elif 'message' in query:
            query = query.replace("message ", "")
            name = query
            name = name.capitalize()
            # print(name)
            time.sleep(2)
            print("What should I message")
            speak("What should I message")
            message = takeCommand()
            # message = 'hi'
            print(message)
            print('Wait opening whatsapp')
            speak('wait opening whatsapp')
            with WhatsApp() as bot:
                bot.send(name, # name of recipient
                message)
                print('Message Sent')
                speak('Message Sent')
                time.sleep(5)
              # message
# The name of the recipient should be in your contacts
            

        elif 'the time' in query:
            speak(f"Sir, the time is {strTime}")
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            print(strTime)

        elif 'search' in query: #for searching any element
            # local=query
            # leng=len(local)
            # l=local.find(' ')
            # word=local[l:leng]
            query = query.replace("search", "")
            webbrowser.open("https://www.google.com/search?q="+query)
        
