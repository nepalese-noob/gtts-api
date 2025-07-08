from flask import Flask, request, send_file
from gtts import gTTS
import tempfile
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "GTTS Nepali API is running."

@app.route("/speak", methods=["GET"])
def speak():
    text = request.args.get("text")
    lang = request.args.get("lang", "ne")  # default to Nepali

    if not text:
        return {"error": "No text provided"}, 400

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            tts = gTTS(text=text, lang=lang)
            tts.save(fp.name)
            return send_file(fp.name, mimetype="audio/mpeg", as_attachment=True, download_name="speech.mp3")
    except ValueError:
        return {"error": "Unsupported language code or invalid text."}, 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
