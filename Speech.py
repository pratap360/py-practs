import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voices',voices[0].id)

def wishme():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")   
    
    elif hour>=12 and hour<=18:
        speak("Good Afternoon")

    else:
        speak("Good Night")

    speak("Hiya! i am Jarvis , How can i help you?")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone()as source:
        print('Listening......')
        r.pause_threshold = 3
        audio = r.listen(source)
    
    try:
        print('Command Recognised')
        query = r.recognize_google(audio , Language='en-in') #jo query user dega usko google se recognise karo , it can even di it from bin or google cloud but here we are using gooogle only
        print('The command is : ',query)
    
    except Exception as e:
        print(e)
        print("Please repeat")
        return'None'

if __name__ == "__main__" :
    wishme()
    while True:
        query= takecommand().lower()

        if wikipedia in query:
            speak('Searching wikipedia...')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia ...")
            speak(results)