import pyttsx3  # For text-to-speech
import speech_recognition as sr  # For speech recognition

def main():
    engine = pyttsx3.init()
    engine.say("Hello, I am Holly, your friendly assistant.")
    engine.runAndWait()

if __name__ == "__main__":
    main()
