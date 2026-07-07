# 🌐 Language Translator

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)

A web-based translation tool that translates text between 25+ languages using Google Translate, with text-to-speech playback of the result. Built with [Streamlit](https://streamlit.io/) so it runs entirely in the browser and deploys straight to Streamlit Community Cloud.

## Features

- Translate text between 25+ languages, including regional languages like Hindi, Nepali, Tibetan, Punjabi, Bengali, Tamil, and Telugu
- Auto-detect the source language
- One-click swap between source and target languages
- Listen to the translation via text-to-speech, generated as in-browser playable audio
- Clean, responsive interface — no desktop install required

## Tech Stack

| Library | Purpose |
|---|---|
| [Streamlit](https://streamlit.io/) | Web UI framework |
| [deep-translator](https://github.com/nidhaloff/deep-translator) | Google Translate backend (no API key required) |
| [gTTS](https://github.com/pndurette/gTTS) | Converts translated text into playable audio |

## Project Structure

```
codealpha_translator-app/
├── translator_app.py   # Main Streamlit app
├── requirements.txt    # Python dependencies
└── README.md
```

## Getting Started (Local)

```bash
# Clone the repo
git clone https://github.com/swasxtik/codealpha_translator-app.git
cd codealpha_translator-app

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run translator_app.py
```

Then open the local URL Streamlit prints in your terminal (usually `http://localhost:8501`).

## Deployment

Deployed on [Streamlit Community Cloud](https://streamlit.io/cloud):

1. Push the code to a GitHub repo
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect the repo
3. Set the main file path to `translator_app.py`
4. Deploy — Streamlit Cloud installs everything in `requirements.txt` automatically

**Live app:** https://codealphatranslator-app-xtip9syg8yjnigixh7abhl.streamlit.app/

## How to Use

1. Select a source language (or leave on **Auto Detect**)
2. Select a target language
3. Type or paste text into the **Enter text** box
4. Click **Translate**
5. Click **🔊 Speak result** to hear the translation read aloud
6. Use **⇄ Swap** to quickly reverse source and target languages

## Supported Languages

English, Hindi, Spanish, French, German, Italian, Portuguese, Russian, Chinese (Simplified), Japanese, Korean, Arabic, Bengali, Punjabi, Urdu, Nepali, Tibetan, Tamil, Telugu, Turkish, Dutch, Greek, Polish, Vietnamese, Thai — plus Auto Detect for the source language.

## Notes

- Translation and text-to-speech both call Google's services in the background, so an internet connection is required.
- **Auto Detect** is only available as a source language option, not a target.

## Acknowledgments

Built as part of the **CodeAlpha**  artifical intelligence internship.
