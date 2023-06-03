# 211119 
#Shivam Deswal 
#Desktop Assistant
#Importing Modules
import wikipedia 
import webbrowser
import os
import pyttsx3 
import speech_recognition as sr
import datetime

#sapi5 to take voice from user depending on your system it is an api
engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    '''This Function is used to take string and convert that into voice'''
    engine.say(audio)
    engine.runAndWait()


def greet():
    '''This function wish user according to time'''
    speak("Hello ANKIT DESWAL ")
    speak("I'm Desktop Assistant. What I'm suppose to do")       

def takeVoiceinput():
    '''It takes microphone input from the user and returns string output'''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Try Saying...")
        r.pause_threshold = 1 #Seconds of non-speaking audio before a phrase is considered complete
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        voice = r.recognize_google(audio, language='en-in')
        print(f"User said: {voice}\n")

    except Exception as e:    
        print("Repeat again ..")  
        return "None"
    return voice

if __name__ == "__main__":
    greet()
    while True:
        str = takeVoiceinput().lower()

        if 'wikipedia' in str:
            speak('Searching Wikipedia...')
            str = str.replace("wikipedia", "")
            results = wikipedia.summary(str, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
         # For Web Search   
        elif 'open spotify' in str:
            webbrowser.open("spotify.com") #open spotify

        elif 'open youtube' in str:
            webbrowser.open("youtube.com") #open youtube

        elif 'open google' in str:
            webbrowser.open("google.com") #open google
            
        elif 'open gmail' in str:
            webbrowser.open("gmail.com")  #open gmail 
        
        elif 'open instagram' in str:
            webbrowser.open("instagram.com") #open instagram
            
        elif 'open facebook' in str:
            webbrowser.open("facebook.com") #open facebook
        
        elif 'open flipkart' in str:
            webbrowser.open("flipkart.com") #open flipkart
  
        #Play Favourite song
        elif 'play music' in str:
            music_dir ='C:\\Users\\SHIVAM\\Music\\music'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
                
        # Tell current date and time    
        elif 'the time' in str:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            print(strTime)   
            speak(f"Current, time is {strTime}")
            
        # Open vs code code
        elif 'vs code' in str:
            vsCode = "C:\\Users\\SHIVAM\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vsCode) 
            
        #close or exit
        elif 'shutdown' in str: 
            speak("Good Bye Sir")           
            quit() 
 
 