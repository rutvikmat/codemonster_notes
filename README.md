# 🎥 AI Explainer Video Generator — Flask Web App

A full-stack automation system that converts structured text input into professional explainer videos using Python, MoviePy, and Flask.

Users submit event details through a web interface, and the backend automatically generates narrated videos with subtitles, animations, background music, and downloadable output.

---

## 🚀 Features

* 🌐 Web-based user interface (no CLI needed)
* 📝 Form-based input for event details
* 🎨 Multiple visual templates (Dark / Light themes)
* 🖼 Auto slide generation per content block
* 🔊 Text-to-speech narration (gTTS)
* 🟡 Word-by-word karaoke subtitles
* 🎬 Fade-in animated transitions
* 🎵 Background music mixing
* 👀 Video preview before download
* ⬇ One-click MP4 download
* ⚙ Fully automated rendering pipeline

---

## 🏗 Architecture Overview

```
Browser UI
   ↓
Flask Web Server
   ↓
Input Parsing
   ↓
Slide Image Generation (Pillow)
   ↓
Audio Generation (gTTS)
   ↓
Subtitle Timing Engine
   ↓
MoviePy Video Composition
   ↓
Preview + Download
```

All video creation is handled server-side without manual editing.

---

## 📁 Project Structure

```
Assessment2_WebApp/
│
├── app.py
├── requirements.txt
│
├── templates/
│   ├── index.html        # Input form UI
│   └── preview.html     # Video preview & download
│
├── backgrounds/
│   ├── dark/
│   │   ├── bg1.jpg
│   │   └── bg2.jpg
│   └── light/
│       ├── bg1.jpg
│       └── bg2.jpg
│
├── music/
│   └── bg_music.mp3
│
└── output/
    └── final_video.mp4
```

---

## ⚙ Installation

### 1. Create Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install FFmpeg (macOS)

```bash
brew install ffmpeg
```

Verify:

```bash
ffmpeg -version
```

---

## ▶ Running the Application

From the project directory:

```bash
python app.py
```

Open in browser:

```
http://127.0.0.1:5000
```

### User Flow

1. Enter title, date, duration, and bullet points
2. Select visual theme
3. Click **Generate Video**
4. Loader displays during rendering
5. Preview page shows generated video
6. Download MP4 with one click

---

## 🎯 Automation Logic

### Slide Timing

Each slide duration is calculated from narration audio length:


slide_duration = audio_clip.duration


Ensures perfect sync between visuals and voice.

### Subtitle Timing

Karaoke subtitles are generated word-by-word based on:


per_word_time = audio_duration / total_words


### Audio Mixing

Final audio track is composed as:

final_audio = narration + background_music


With music volume scaled for clarity.

---

## 🧠 Technical Highlights

* Dynamic multimedia timelines
* Template-based visual theming
* Programmatic animation effects
* Server-side rendering
* No manual video editing
* Fully repeatable pipeline

---

## 🧪 Tested On

* macOS
* Python 3.10+
* MoviePy 2.x
* Flask 2.x

---

## 🔮 Possible Enhancements

* CSV upload for batch video generation
* User authentication and history dashboard
* Logo watermark and branding options
* Progress bar using AJAX / WebSockets
* Cloud deployment (Render, Railway, AWS)

---

## 👤 Author

**Rutvik Mathapati**
MCA Graduate | Python 
Skills required for this project : Python, Flask, Django, SQL, Machine Learning, Automation, Multimedia Processing

---

## 📜 License

This project is intended for educational and academic demonstration purposes.
