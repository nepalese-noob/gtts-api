from flask import Flask, request, send_file
from gtts import gTTS
import tempfile
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "GTTS API is running."

@app.route("/speak", methods=["GET"])
def speak():
    text = request.args.get("text")
    if not text:
        return {"error": "No text provided"}, 400

    # Create temporary mp3 file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
        tts = gTTS(text)
        tts.save(fp.name)
        return send_file(fp.name, mimetype="audio/mpeg", as_attachment=True, download_name="speech.mp3")
