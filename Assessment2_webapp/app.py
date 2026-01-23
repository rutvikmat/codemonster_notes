import os
import textwrap
from flask import Flask, render_template, request, send_file
from gtts import gTTS
from PIL import Image, ImageDraw, ImageFont
from moviepy import (
    ImageClip, AudioFileClip, CompositeVideoClip,
    concatenate_videoclips, CompositeAudioClip, TextClip, vfx
)

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
BG_DIR = os.path.join(BASE_DIR, "backgrounds")
MUSIC_FILE = os.path.join(BASE_DIR, "music", "bg_music.mp3")

VIDEO_W, VIDEO_H = 1280, 720
FONT_SIZE_MAIN = 48
FONT_SIZE_SUB = 26
FADE_DURATION = 0.4

os.makedirs(OUTPUT_DIR, exist_ok=True)


# ---------- IMAGE CREATION ----------
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


# ---------- VIDEO GENERATOR ----------
def generate_video(title, points, date, duration, template):
    template_dir = os.path.join(BG_DIR, template)
    backgrounds = [os.path.join(template_dir, f) for f in os.listdir(template_dir) if f.endswith((".jpg", ".png"))]
    if not backgrounds:
        raise RuntimeError("No background images found for selected template")

    texts = [title] + points + [f"Date {date}. Duration {duration}"]

    clips, subtitles = [], []
    temp_files = []
    current_time = 0

    for i, text in enumerate(texts):
        img = os.path.join(BASE_DIR, f"slide{i}.png")
        aud = os.path.join(BASE_DIR, f"audio{i}.mp3")

        create_image(backgrounds[i % len(backgrounds)], text, img)
        gTTS(text).save(aud)

        temp_files.extend([img, aud])

        audio_clip = AudioFileClip(aud)
        dur = audio_clip.duration

        base = (
            ImageClip(img)
            .with_duration(dur)
            .with_effects([vfx.FadeIn(FADE_DURATION)])
            .with_audio(audio_clip)
        )
        clips.append(base)

        words = text.split()
        per_word = dur / max(len(words), 1)

        for j in range(len(words)):
            txt = " ".join(words[:j+1])
            sub = (
                TextClip(text=txt, font_size=FONT_SIZE_SUB, color="yellow",
                         size=(VIDEO_W-100, None), method="caption")
                .with_position(("center", VIDEO_H-90))
                .with_start(current_time + j * per_word)
                .with_duration(per_word)
            )
            subtitles.append(sub)

        current_time += dur

    video = concatenate_videoclips(clips, method="compose")
    video = CompositeVideoClip([video] + subtitles)

    voice_audio = video.audio

    if os.path.exists(MUSIC_FILE):
        music = AudioFileClip(MUSIC_FILE).with_volume_scaled(0.25).with_duration(video.duration)
        final_audio = CompositeAudioClip([voice_audio, music])
    else:
        final_audio = voice_audio

    video = video.with_audio(final_audio)

    output_path = os.path.join(OUTPUT_DIR, "final_video.mp4")
    video.write_videofile(output_path, fps=24)

    for f in temp_files:
        if os.path.exists(f):
            os.remove(f)

    return output_path


# ---------- ROUTES ----------
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form["title"]
        date = request.form["date"]
        duration = request.form["duration"]
        points = request.form["points"].split("\n")
        template = request.form["template"]

        video_path = generate_video(title, points, date, duration, template)
        filename = os.path.basename(video_path)
        return render_template("preview.html", video_file=filename)

    return render_template("index.html")


@app.route("/video/<filename>")
def serve_video(filename):
    return send_file(os.path.join(OUTPUT_DIR, filename))


if __name__ == "__main__":
    app.run(debug=True)
