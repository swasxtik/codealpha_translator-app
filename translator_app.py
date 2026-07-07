
import io

import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS

# Languages supported by GoogleTranslator, as {display_name: language_code}
LANGUAGES = {
    "Auto Detect": "auto",
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Italian": "it",
    "Portuguese": "pt",
    "Russian": "ru",
    "Chinese (Simplified)": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Arabic": "ar",
    "Bengali": "bn",
    "Punjabi": "pa",
    "Urdu": "ur",
    "Nepali": "ne",
    "Tibetan": "bo",
    "Tamil": "ta",
    "Telugu": "te",
    "Turkish": "tr",
    "Dutch": "nl",
    "Greek": "el",
    "Polish": "pl",
    "Vietnamese": "vi",
    "Thai": "th",
}

# gTTS uses its own (smaller) set of language codes. Map where they differ;
# languages not listed here just reuse the GoogleTranslator code.
GTTS_LANG_OVERRIDES = {
    "zh-CN": "zh-CN",
    "auto": "en",  # gTTS has no auto-detect; fall back to English voice
}

st.set_page_config(page_title="Language Translator", page_icon="🌐", layout="wide")

if "translated_text" not in st.session_state:
    st.session_state.translated_text = ""
if "source_lang" not in st.session_state:
    st.session_state.source_lang = "Auto Detect"
if "target_lang" not in st.session_state:
    st.session_state.target_lang = "Hindi"

st.title("🌐 Language Translator")

# --- Language selector row ---
col_from, col_swap, col_to = st.columns([4, 1, 4])

lang_names = list(LANGUAGES.keys())
target_names = [l for l in lang_names if l != "Auto Detect"]

with col_from:
    source_lang = st.selectbox(
        "From", lang_names, index=lang_names.index(st.session_state.source_lang)
    )

with col_swap:
    st.write("")
    st.write("")
    if st.button("⇄ Swap"):
        if st.session_state.source_lang == "Auto Detect":
            st.warning("Pick a specific source language before swapping.")
        else:
            st.session_state.source_lang, st.session_state.target_lang = (
                st.session_state.target_lang,
                st.session_state.source_lang,
            )
            st.rerun()

with col_to:
    target_lang = st.selectbox(
        "To", target_names, index=target_names.index(st.session_state.target_lang)
    )

st.session_state.source_lang = source_lang
st.session_state.target_lang = target_lang

# --- Text areas ---
col_in, col_out = st.columns(2)

with col_in:
    input_text = st.text_area("Enter text", height=220, key="input_text")

with col_out:
    st.text_area(
        "Translation", value=st.session_state.translated_text, height=220, disabled=True
    )

# --- Action buttons ---
col_btn1, col_btn2 = st.columns([1, 1])

with col_btn1:
    translate_clicked = st.button("Translate", type="primary")

if translate_clicked:
    text = input_text.strip()
    if not text:
        st.warning("Type or paste some text first.")
    else:
        src_code = LANGUAGES[source_lang]
        tgt_code = LANGUAGES[target_lang]
        with st.spinner("Translating..."):
            try:
                result = GoogleTranslator(source=src_code, target=tgt_code).translate(text)
                st.session_state.translated_text = result
                st.rerun()
            except Exception as exc:
                st.error(f"Translation failed: {exc}")

# --- Speak result ---
if st.session_state.translated_text:
    with col_btn2:
        speak_clicked = st.button("🔊 Speak result")

    if speak_clicked:
        tgt_code = LANGUAGES[target_lang]
        tts_code = GTTS_LANG_OVERRIDES.get(tgt_code, tgt_code)
        try:
            with st.spinner("Generating audio..."):
                tts = gTTS(text=st.session_state.translated_text, lang=tts_code)
                buf = io.BytesIO()
                tts.write_to_fp(buf)
                buf.seek(0)
            st.audio(buf, format="audio/mp3")
        except Exception as exc:
            st.error(f"Couldn't generate speech: {exc}")

st.caption(
    "Tip: use your browser's copy shortcut (Ctrl/Cmd+C) after selecting the "
    "translated text in the box above to copy it."
)
