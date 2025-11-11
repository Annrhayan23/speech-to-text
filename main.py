import speech_recognition as sr

def speech_to_text():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use microphone as source
    with sr.Microphone() as source:
        print("🎤 Say something... I’m listening!")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        # Convert speech to text using Google’s API
        print("🧠 Recognizing...")
        text = recognizer.recognize_google(audio)
        print(f"✅ You said: {text}")

    except sr.UnknownValueError:
        print("❌ Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("⚠️ Could not request results — check your internet connection.")

if __name__ == "__main__":
    speech_to_text()
