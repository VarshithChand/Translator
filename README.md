Sure! Here's a clear, professional **README.md** file for your Flask-based language translator web app, which includes usage, setup, features, and instructions:

````markdown
# Language Translator Web App

A simple Flask-based multilingual language translator web application with speech input/output, dark/light mode toggle, and translation history stored locally in the browser.

---

## Features

- Translate text between multiple languages using Google Translate API via `deep-translator`.
- Speech-to-text input with microphone support.
- Text-to-speech output of translated text.
- Dark and Light mode toggle with user preference saved.
- Translation history saved in browser localStorage (up to 20 entries).
- Clear translation history with a single click.
- Responsive design for desktop and mobile devices.
- No database required; all data stored locally in browser.

---

## Supported Languages

| Code | Language |
|-------|------------|
| en    | English    |
| te    | Telugu     |
| hi    | Hindi      |
| es    | Spanish    |
| fr    | French     |
| de    | German     |
| zh    | Chinese    |
| ja    | Japanese   |
| ru    | Russian    |

---

## Getting Started

### Prerequisites

- Python 3.7+
- `pip` package manager

### Installation

1. Clone the repository or download the source code.

2. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate    # On Windows use `venv\Scripts\activate`
````

3. Install dependencies:

```bash
pip install flask deep-translator
```

### Running the App

Run the Flask application:

```bash
python app.py
```

Open your web browser and navigate to:

```
http://127.0.0.1:5000/
```

---

## Project Structure

```
├── app.py            # Flask application
├── templates/
│   ├── index.html    # Main translation page
│   └── history.html  # Translation history page
├── static/
│   └── style.css     # Stylesheet with dark/light mode and responsive design
└── README.md         # This file
```

---

## Usage

* Enter text in the textarea.
* Select the source and target languages.
* Click **Translate** to get the translated text.
* Use the 🎙️ button to input text via microphone.
* Click 🔊 to listen to the translated text.
* Switch between dark and light mode using the 🌓 toggle button.
* Visit the **History** page to view or clear past translations.

---

## Notes

* Translation history is saved in your browser's localStorage, so it won't persist if you clear browser data or use another browser/device.
* Speech recognition (`webkitSpeechRecognition`) is supported only in compatible browsers (e.g., Chrome).
* Text-to-speech works if your browser supports the Web Speech API.

---

## License

This project is open-source and free to use.

---

## Acknowledgements

* Uses the [deep-translator](https://github.com/nidhaloff/deep-translator) Python package for translations.
* Powered by Google Translate through `deep-translator`.
* Inspired by simple, clean UI design with dark/light modes and mobile responsiveness.

---

Feel free to contribute or open issues if you find bugs or want new features!

```

---

If you want, I can help you generate this as a `README.md` file to save on disk. Would you like me to do that?
```
