import speech_recognition as sr
import datetime
import pyttsx3
import pyaudio
import webbrowser

# Initialize the recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)

# Function to recognize voice commands and perform actions
def listen_and_respond():
    with sr.Microphone() as source:
        print("Ask me anything...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"User said: {command}")

            if "hello" in command:
                respond("Hello! How can I assist you today?")
            elif "time" in command:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                respond(f"The current time is {current_time}")
            elif "date" in command:
                current_date = datetime.date.today().strftime("%B %d, %Y")
                respond(f"Today's date is {current_date}")
            elif "search" in command:
                query = command.split("search")[-1].strip()
                search_web(query)
            elif 'open youtube' in command:
                webbrowser.open("youtube.com")
                respond("youtube")
            else:
                respond("Sorry, I didn't understand the command.")

        except sr.UnknownValueError:
            respond("I couldn't understand what you said.")
        except sr.RequestError:
            respond("I couldn't request results. Check your network connection.")

# Function to generate a voice response
def respond(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

# Function to search the web
def search_web(query):
    import webbrowser
    url = f"https://www.google.com/search?q={query}"
    respond(f"Open google search {query}")
    webbrowser.open(url)

if __name__ == "__main__":
    respond("Hello! How can I assist you today?")
    while True:
        listen_and_respond()