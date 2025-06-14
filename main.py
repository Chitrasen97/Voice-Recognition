# import speech_recognition as sr
# import webbrowser
# import pyttsx3
# import music_library
# import requests


# recognizer=sr.Recognizer()
# engine=pyttsx3.init()
# newsapi="15dfd52de93743179c2620c38912eb7c"

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def processCommand(c):
#     if "open google" in c.lower():
#          webbrowser.open("https://google.com")

#     elif "open instagram" in c.lower():
#          webbrowser.open("https://instagram.com")

#     elif "open facebook" in c.lower():
#          webbrowser.open("https://facebook.com")
    
#     elif "open youtube" in c.lower():
#          webbrowser.open("https://youtube.com")
    
#     elif "open linkedin" in c.lower():
#          webbrowser.open("https://linkedin.com")

#     elif c.lower().startswith("play"):
#         song = c.lower().split(" ")[1]
#         link= music_library.music[song]
#         webbrowser.open(link)

#     elif "news" in c.lower():
#         r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
#         print(f"Status Code: {r.status_code}")
#         print(f"Response: {r.text}") 
#         if r.status_code == 200:
#             data = r.json()
#             articles = data.get('articles', [])

#             for article in articles[:5]:
#                  speak(article['title'])
#         else:
#             speak("Sorry, I couldn't fetch the news.") 

# if __name__=="__main__":
#     speak("Hey Nikita this side. How may I help you?")
#     while True:
#         r = sr.Recognizer()
#         print("recognizing...")

#         try:
#             with sr.Microphone() as source:
#                 print("Listening...")
#                 r.adjust_for_ambient_noise(source, duration=1)
#                 audio = r.listen(source, timeout=2, phrase_time_limit=1)
#                 word=r.recognize_google(audio)
#                 if (word.lower() == "nikita"):
#                     speak("Yes please")
#                     # listen for command
#                     with sr.Microphone() as source:
#                         print("Nikita Activated...")
#                         audio = r.listen(source)
#                         command=r.recognize_google(audio)
#                         processCommand(command)
#         except Exception as e:
#                     print("Error; {0}".format(e))



# import speech_recognition as sr
# import webbrowser
# import pyttsx3
# import music_library
# import requests

# recognizer = sr.Recognizer()
# engine = pyttsx3.init()

# # ✅ Replace with your actual GNews API key
# gnews_api_key = "44d67fc83fad26ad29950d66d46c630d"

# def speak(text):
#     engine.say(text)
#     engine.runAndWait()

# def processCommand(c):
#     if "open google" in c.lower():
#         webbrowser.open("https://google.com")

#     elif "open instagram" in c.lower():
#         webbrowser.open("https://instagram.com")

#     elif "open facebook" in c.lower():
#         webbrowser.open("https://facebook.com")
    
#     elif "open youtube" in c.lower():
#         webbrowser.open("https://youtube.com")
    
#     elif "open linkedin" in c.lower():
#         webbrowser.open("https://linkedin.com")

#     elif c.lower().startswith("play"):
#         song = c.lower().split(" ")[1]
#         link = music_library.music.get(song)
#         if link:
#             webbrowser.open(link)
#         else:
#             speak("Sorry, I couldn't find that song.")

#     elif "news" in c.lower():
#         url = f"https://gnews.io/api/v4/top-headlines?country=in&token={gnews_api_key}"
#         try:
#             r = requests.get(url)
#             print(f"Status Code: {r.status_code}")
#             print(f"Response: {r.text}") 
#             if r.status_code == 200:
#                 data = r.json()
#                 articles = data.get('articles', [])
#                 if not articles:
#                     speak("Sorry, I couldn't find any news at the moment.")
#                 else:
#                     speak("Here are the top headlines.")
#                     for article in articles[:5]:
#                         speak(article.get('title', 'No title available'))
#             else:
#                 speak("Sorry, I couldn't fetch the news.")
#         except Exception as e:
#             print(f"Error fetching news: {e}")
#             speak("There was an error getting the news.")

# if __name__ == "__main__":
#     speak("Hey Nikita this side. How may I help you?")
#     while True:
#         r = sr.Recognizer()
#         print("recognizing...")

#         try:
#             with sr.Microphone() as source:
#                 print("Listening...")
#                 r.adjust_for_ambient_noise(source, duration=1)
#                 audio = r.listen(source, timeout=2, phrase_time_limit=1)
#                 word = r.recognize_google(audio)
#                 if word.lower() == "nikita":
#                     speak("Yes please")
#                     with sr.Microphone() as source:
#                         print("Nikita Activated...")
#                         audio = r.listen(source)
#                         command = r.recognize_google(audio)
#                         processCommand(command)
#         except Exception as e:
#             print("Error; {0}".format(e))


# 


import speech_recognition as sr
import webbrowser
import pyttsx3
import music_library
import requests
import google.generativeai as genai
import json

# ----------------------------
# 🔐 API KEYS
# ----------------------------
gnews_api_key = "44d67fc83fad26ad29950d66d46c630d"
gemini_api_key = "AIzaSyDHj1_gF6T0wJxJBjjWecK4WgIc8slovKY"

# ----------------------------
# 🔊 Text-to-Speech
# ----------------------------
engine = pyttsx3.init()

def speak(text):
    print(f"[TTS] Speaking: {text}")
    engine.say(text)
    engine.runAndWait()

# ----------------------------
# 🤖 Configure Gemini
# ----------------------------
genai.configure(api_key=gemini_api_key)
gemini_model = genai.GenerativeModel("models/gemini-1.5-flash")

def ask_gemini_fallback(query):
    print(f"[GEMINI] Sending unknown command to Gemini: '{query}'")
    try:
        response = gemini_model.generate_content(query)
        answer = response.text.strip()
        print(f"[GEMINI] Response: {answer}")
        return answer
    except Exception as e:
        print(f"[ERROR] Gemini fallback failed: {e}")
        return "I tried asking Gemini, but something went wrong."

# ----------------------------
# 🧠 Command Processor
# ----------------------------
def processCommand(c):
    print(f"[INFO] Received command: {c}")
    command = c.lower()

    if "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google.")

    elif "open instagram" in command:
        webbrowser.open("https://instagram.com")
        speak("Opening Instagram.")

    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
        speak("Opening Facebook.")

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube.")

    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
        speak("Opening LinkedIn.")

    elif command.startswith("play"):
        song = command.split(" ")[1]
        link = music_library.music.get(song)
        if link:
            webbrowser.open(link)
            speak(f"Playing {song}.")
        else:
            speak(f"Sorry, I couldn't find the song {song}.")
            print(f"[WARN] Song '{song}' not found in music library.")

    elif "news" in command:
        url = f"https://gnews.io/api/v4/top-headlines?country=in&token={gnews_api_key}"
        print(f"[INFO] Fetching news from: {url}")
        try:
            r = requests.get(url)
            print(f"[DEBUG] HTTP Status Code: {r.status_code}")
            print(f"[DEBUG] Response JSON: {r.text}")

            if r.status_code == 200:
                try:
                    data = r.json()
                    articles = data.get('articles', [])
                    if not articles:
                        print("[WARN] No articles found in response.")
                        speak("Sorry, no news articles were found.")
                    else:
                        speak("Here are the top headlines.")
                        for i, article in enumerate(articles[:5]):
                            title = article.get('title', 'No title available')
                            print(f"[{i+1}] {title}")
                            speak(title)
                except json.JSONDecodeError:
                    speak("Sorry, I couldn't understand the news data.")
                    print("[ERROR] Failed to parse JSON response.")
            else:
                speak("Sorry, I couldn't fetch the news. The server responded with an error.")
                print(f"[ERROR] Failed to fetch news. Status Code: {r.status_code}")
        except Exception as e:
            print(f"[ERROR] Exception while fetching news: {e}")
            speak("There was an error getting the news.")

    else:
        # Fallback to Gemini
        print("[FALLBACK] Command not recognized. Using Gemini.")
        reply = ask_gemini_fallback(command)
        speak(reply)

# ----------------------------
# 🎤 Voice Assistant Loop
# ----------------------------
if __name__ == "__main__":
    speak("Hey Nikita this side. How may I help you?")
    recognizer = sr.Recognizer()

    while True:
        print("[LISTEN] Awaiting trigger word...")

        try:
            with sr.Microphone() as source:
                print("[MIC] Listening for wake word...")
                recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=1)
                word = recognizer.recognize_google(audio)
                print(f"[VOICE] Heard: {word}")

                if word.lower() == "nikita":
                    speak("Yes please")
                    with sr.Microphone() as source:
                        print("[MIC] Listening for command...")
                        audio = recognizer.listen(source)
                        command = recognizer.recognize_google(audio)
                        processCommand(command)

        except sr.WaitTimeoutError:
            print("[TIMEOUT] Listening timed out.")
        except sr.UnknownValueError:
            print("[ERROR] Could not understand audio.")
        except Exception as e:
            print(f"[ERROR] Unexpected error: {e}")