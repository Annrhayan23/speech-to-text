

# 🎤 Speech-to-Text App

A simple **AI-based Speech Recognition** project built using Python.
This app listens to your voice and converts it into text using Google’s Speech Recognition API.
Perfect for beginners exploring AI and Natural Language Processing (NLP)!

---

## 🧩 Features

* 🎙️ Records audio from your microphone
* 🧠 Converts speech to text instantly
* ⚠️ Handles background noise
* 💬 Prints recognized text in the terminal

---

## 🗂️ Project Structure

```
speech_to_text/
│
├── main.py                # Main Python file (runs the app)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## ⚙️ Installation

### 1. Clone or Download the Project

```bash
git clone https://github.com/Annrhayan23/speech_to_text.git
cd speech_to_text
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

> 💡 If `pyaudio` doesn’t install directly:
>
> ```
> pip install pipwin
> pipwin install pyaudio
> ```

---

## ▶️ Run the App

```bash
python main.py
```

Then, **speak into your microphone** — the program will convert your speech to text and display it in the console.

---

## 🧠 How It Works

1. The `speech_recognition` library listens to your voice through the microphone.
2. It sends the audio to Google’s free Speech Recognition API.
3. The text result is displayed in real-time.

---

## 📚 Requirements

* Python 3.7+
* Internet connection (for Google API)
* Working microphone

---

## 🧰 Libraries Used

* `speechrecognition`
* `pyaudio`

---

## 🚀 Future Enhancements

* Add GUI using **Tkinter** or **Streamlit**
* Save transcribed text to a file
* Add multi-language speech recognition

---

## 👨‍💻 Author

**ANN RHAYAN**
💬 Simple AI Project | Beginner Friendly | Python-based

