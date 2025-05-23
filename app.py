from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

LANGUAGES = {
    "en": "English",
    "te": "Telugu",
    "hi": "Hindi",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "zh": "Chinese",
    "ja": "Japanese",
    "ru": "Russian"
}

@app.route("/", methods=["GET", "POST"])
def index():
    translated_text = ""
    input_text = ""
    src_lang = "en"
    dest_lang = "te"

    if request.method == "POST":
        input_text = request.form.get("text", "").strip()
        src_lang = request.form.get("src_lang", "en")
        dest_lang = request.form.get("dest_lang", "te")

        if input_text:
            try:
                translated_text = GoogleTranslator(source=src_lang, target=dest_lang).translate(input_text)
            except Exception as e:
                translated_text = f"Error: {e}"

    return render_template("index.html",
                           input_text=input_text,
                           translated_text=translated_text,
                           src_lang=src_lang,
                           dest_lang=dest_lang,
                           languages=LANGUAGES)

@app.route("/history")
def history():
    return render_template("history.html")

if __name__ == "__main__":
    app.run(debug=True)
