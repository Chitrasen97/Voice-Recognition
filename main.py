import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library

recognizer=sr.Recognizer()
engine=pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
         webbrowser.open("https://google.com")

    elif "open instagram" in c.lower():
         webbrowser.open("https://instagram.com")

    elif "open facebook" in c.lower():
         webbrowser.open("https://facebook.com")
    
    elif "open youtube" in c.lower():
         webbrowser.open("https://youtube.com")
    
    elif "open linkedin" in c.lower():
         webbrowser.open("https://linkedin.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link= music_library.music[song]
        webbrowser.open(link)

if __name__=="__main__":
    speak("Hey Nick this side. How may I help you?")
    while True:
        r = sr.Recognizer()
        print("recognizing...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                r.adjust_for_ambient_noise(source, duration=1)
                audio = r.listen(source, timeout=1, phrase_time_limit=4)
                word=r.recognize_google(audio)
                if (word.lower() == "nick"):
                    speak("Yes please")
                    # listen for command
                    with sr.Microphone() as source:
                        print("nick Activated...")
                        audio = r.listen(source)
                        command=r.recognize_google(audio)
                        processCommand(command)
        except Exception as e:
                    print("Error; {0}".format(e))