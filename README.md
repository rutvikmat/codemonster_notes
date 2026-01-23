GitHub README.md (Final Version)
# 🎯 Automation Assessment Projects

This repository contains two end-to-end automation projects designed to demonstrate practical skills in workflow automation, data processing, and multimedia generation using Python and no-code workflow logic.

## 📌 Assessments Included

### ✅ Assessment 1 — IT Support Ticket Automation
Automates processing of IT support tickets using validation, deduplication, routing, SLA calculation, and reporting.

### ✅ Assessment 2 — Automated Explainer Video Generator
Automatically generates short explainer videos from structured text input with narration, subtitles, animations, and background music.

---

# 🟦 Assessment 1 — IT Support Ticket Automation

## 📘 Problem Statement

University IT support receives large volumes of tickets with inconsistent and duplicate data, causing delays and manual workload.  
This automation processes tickets end-to-end with business rules and reporting.

## ⚙️ Features

- CSV-based input processing
- Email format validation
- Priority validation (Low / Medium / High)
- Text normalization
- Deduplication (same email + issue within 24 hours)
- Automatic ticket ID generation
- Issue-based routing to IT teams
- SLA deadline calculation
- Error handling and rejection logging
- Summary report generation

## 🧩 Workflow Logic



CSV Input
↓
Normalize Fields
↓
Validate Email & Priority
↓
Validate Issue Type
↓
Deduplicate Check (24 hrs)
↓
Generate Ticket ID
↓
Route to IT Team
↓
Calculate SLA Deadline
↓
Store Processed Ticket
↓
Update Summary Report


Rejected records are stored separately with error reasons.

## 📂 Folder Structure



Assessment1/
│
├── input/
│ └── tickets_input.csv
│
├── output/
│ ├── processed_tickets.csv
│ ├── rejected_tickets.csv
│ └── summary_report.csv
│
└── ticket_processor.py


## ▶ How to Run

```bash
cd Assessment1
python3 ticket_processor.py


Outputs will be generated inside the output/ folder.

🟩 Assessment 2 — Automated Explainer Video Generator
📘 Problem Statement

University departments require frequent short explainer videos for workshops and announcements.
Manual video creation is time-consuming. This automation generates videos automatically from structured text input.

⚙️ Features

Structured text input parsing

Auto slide generation for each bullet point

Text-to-speech narration (gTTS)

Word-by-word karaoke subtitles

Animated text overlays

Background image templates

Background music mixing

Configurable slide duration and resolution

Fully automated MP4 generation

🎥 Automation Pipeline
Text Input
   ↓
Parse Content
   ↓
Generate Slide Images
   ↓
Generate Narration Audio
   ↓
Create Karaoke Subtitles
   ↓
Add Background Music
   ↓
Apply Transitions & Animations
   ↓
Export Final MP4 Video

📂 Folder Structure
Assessment2/
│
├── input.txt
│
├── backgrounds/
│   └── bg1.jpg, bg2.jpg, ...
│
├── music/
│   └── bg_music.mp3
│
├── output/
│   └── final_video.mp4
│
└── video_generator.py

🛠 Dependencies

Python 3.x

MoviePy (v2.x)

Pillow

gTTS

FFmpeg

Install Requirements
pip install moviepy pillow gTTS imageio imageio-ffmpeg
brew install ffmpeg   # macOS

▶ How to Run
cd Assessment2
python3 video_generator.py


Final video will be saved as:

output/final_video.mp4

🧠 Design Highlights
Assessment 1

Simulates real-world ETL pipelines

Enforces business rules for SLA and routing

Separates operational data from error logs

Provides audit and reporting capability

Assessment 2

Converts structured text to multimedia automatically

Dynamic slide and subtitle generation

Template-based visual design

Fully script-driven video production without editors

🚀 Possible Enhancements

Database integration for ticket storage

Real-time dashboards for IT analytics

Batch video generation from CSV

Multilingual narration support

Branded templates and intros

👤 Author

Rutvik Mathapati
MCA Graduate | Python 
Skills: Python, Django, Flask, SQL, Automation, Machine Learning, Video Processing

📜 License

This project is for academic and learning purposes.


---

# ✅ What This README Does Well

✔ Explains problem clearly  
✔ Shows automation mindset  
✔ Includes workflows  
✔ Shows technical depth  
✔ Recruiter-friendly  
✔ Assessment-friendly  

This is **exactly what evaluators and interviewers like to see**.

---

# 🎯 Final Step Recommendation

To fully complete your submission, I can now help you with:

### ✅ Final PDF report structure (what to submit)
### ✅ Viva / interview questions & answers
### ✅ PowerPoint for project presentation
### ✅ Flow diagrams (draw.io format)

Tell me what you want next and I will guide you through the final polish.