import os
import csv
import textwrap
from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont
from moviepy import (
    ImageClip, AudioFileClip, CompositeVideoClip,
    concatenate_videoclips, CompositeAudioClip, TextClip, vfx
)

# ---------------- CONFIG ----------------

VIDEO_W, VIDEO_H = 1280, 720
FONT_SIZE_MAIN = 50
FONT_SIZE_SUB = 28

BG_DIR = "backgrounds"
MUSIC_FILE = "music/bg_music.mp3"
OUTPUT_DIR = "output"

CSV_FILE = "input.csv"

FADE_DURATION = 0.5

# --------------------------------------


def read_csv():
    if not os.path.exists(CSV_FILE):
        raise FileNotFoundError("CSV file not found")

    slides = []
    date = ""
    duration = ""

    with open(CSV_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            row_type = row["type"].strip().lower()
            text = row["text"].strip()

            if row_type == "title":
                slides.append(text)
                date = row.get("date", "").strip()
                duration = row.get("duration", "").strip()

            elif row_type == "point":
                slides.append(text)

    if not slides:
        raise ValueError("CSV file contains no slide content")

    footer = f"Date {date}. Duration {duration}"
    slides.append(footer)

    return slides


def load_backgrounds():
    imgs = []
    for f in os.listdir(BG_DIR):
        if f.lower().endswith((".jpg", ".png")):
            imgs.append(os.path.join(BG_DIR, f))
    if not imgs:
        raise RuntimeError("No background images found")
    return imgs


def create_image(bg_path, text, filename):
    img = Image.open(bg_path).resize((VIDEO_W, VIDEO_H))
    draw = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial.ttf", FONT_SIZE_MAIN)
    except:
        font = ImageFont.load_default()

    wrapped = textwrap.fill(text, 40)
    bbox = draw.multiline_textbbox((0, 0), wrapped, font=font)
    w, h = bbox[2]-bbox[0], bbox[3]-bbox[1]

    x = (VIDEO_W - w)//2
    y = (VIDEO_H - h)//2

    draw.multiline_text((x, y), wrapped, fill="white", font=font, align="center")
    img.save(filename)


def generate_audio(text, filename):
    gTTS(text).save(filename)


def karaoke_subtitles(words, start, audio_dur):
    clips = []
    per_word = audio_dur / max(len(words), 1)

    for i in range(len(words)):
        txt = " ".join(words[:i+1])

        clip = (
            TextClip(
                text=txt,
                font_size=FONT_SIZE_SUB,
                color="yellow",
                size=(VIDEO_W - 100, None),
                method="caption"
            )
            .with_position(("center", VIDEO_H - 90))
            .with_start(start + i * per_word)
            .with_duration(per_word)
        )

        clips.append(clip)

    return clips


def main():
    print("Starting CSV Based Video Automation...")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    texts = read_csv()
    backgrounds = load_backgrounds()

    slides, audios = [], []
    video_clips = []
    subtitle_clips = []

    # -------- CREATE MEDIA --------
    for i, text in enumerate(texts):
        bg = backgrounds[i % len(backgrounds)]
        img = f"slide{i}.png"
        aud = f"audio{i}.mp3"

        create_image(bg, text, img)
        generate_audio(text, aud)

        slides.append(img)
        audios.append(aud)

    # -------- BUILD VIDEO --------
    current_time = 0

    for img, aud, text in zip(slides, audios, texts):
        audio_clip = AudioFileClip(aud)
        duration = audio_clip.duration

        base = (
            ImageClip(img)
            .with_duration(duration)
            .with_effects([vfx.FadeIn(FADE_DURATION)])
        )

        base = base.with_audio(audio_clip)
        video_clips.append(base)

        words = text.split()
        subs = karaoke_subtitles(words, current_time, duration)
        subtitle_clips.extend(subs)

        current_time += duration

    video = concatenate_videoclips(video_clips, method="compose")
    video = CompositeVideoClip([video] + subtitle_clips)

    # -------- BACKGROUND MUSIC --------
    if os.path.exists(MUSIC_FILE):
        music = (
            AudioFileClip(MUSIC_FILE)
            .with_volume_scaled(0.18)
            .with_duration(video.duration)
        )
        final_audio = CompositeAudioClip([video.audio, music])
        video = video.with_audio(final_audio)

    output_path = os.path.join(OUTPUT_DIR, "final_video.mp4")
    video.write_videofile(output_path, fps=24)

    # -------- CLEANUP --------
    for f in slides + audios:
        if os.path.exists(f):
            os.remove(f)

    print("Video generated successfully:", output_path)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Automation Failed:", e)
