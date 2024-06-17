import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(command):
    command = command.lower()
    print(f"Processing command: {command}")  # Debug print
    if "open google" in command:
        speak("Opening Google")
        webbrowser.open("http://google.com")
    elif "open facebook" in command:
        speak("Opening Facebook")
        webbrowser.open("http://facebook.com")
    elif "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("http://youtube.com")
    elif "open linkedin" in command:
        speak("Opening LinkedIn")
        webbrowser.open("http://linkedin.com")
    elif "open github" in command:
        speak("Opening GitHub")
        webbrowser.open("http://github.com")
    elif "open chatgpt" in command:
        speak("Opening ChatGPT")
        webbrowser.open("https://chatgpt.com/c/09f6b37e-339f-45d7-a577-f2c034423350")
    elif command.startswith("play"):
        song = command.split(" ", 1)[1].strip()
        if song in musicLibrary.naat:
            url = musicLibrary.naat[song]
            speak(f"Now playing {song}")
            webbrowser.open(url)
        else:
            speak(f"Sorry, I couldn't find the nasheed {song}")


    else:
        speak("Command not recognized, please try again.")

if __name__ == "__main__":
    speak("Initializing Jarvis..")
    while True:
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source)
                print("Listening for wake word 'Jarvis'..")
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)
            word = recognizer.recognize_google(audio).lower()
            if word == "jarvis":
                speak("Yes, how can I help you?")
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source)
                    print("Listening for command..")
                    audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
                command = recognizer.recognize_google(audio)
                if "exit" in command.lower() or "stop" in command.lower():
                    speak("Goodbye!")
                    break
                processCommand(command)
        except sr.UnknownValueError:
            print("Sorry, I did not catch that. Please try again.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"Error: {e}")


