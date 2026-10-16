import re
import streamlit as st
from lingua import Language, LanguageDetectorBuilder

# Initialize Lingua detector for accurate detection & confidence score
# Includes English, Urdu, Hindi, Arabic, Spanish, French, German, etc.
languages = [
    Language.ENGLISH,
    Language.URDU,
    Language.ARABIC,
    Language.HINDI,
    Language.FRENCH,
    Language.SPANISH,
    Language.GERMAN,
]
detector = LanguageDetectorBuilder.from_languages(*languages).with_low_accuracy_mode().build()


def clean_text(text: str) -> str:
    """Performs basic text cleanup:

    - Standardizes line breaks (max 2 consecutive newlines)
    - Replaces multiple spaces/tabs with a single space
    - Normalizes repeated punctuation (e.g., '!!!' -> '!', '???' -> '?')
    - Strips whitespace from each line and overall text
    """
    if not text:
        return ""

    # 1. Normalize line endings (CRLF -> LF)
    text = text.replace("\r\n", "\n").replace("\r", "\n")

    # 2. Trim whitespace from individual lines
    lines = [line.strip() for line in text.split("\n")]
    text = "\n".join(lines)

    # 3. Collapse 3 or more consecutive newlines into 2 (clean paragraphs)
    text = re.sub(r"\n{3,}", "\n\n", text)

    # 4. Collapse multiple spaces or tabs into a single space (preserving newlines)
    text = re.sub(r"[ \t]+", " ", text)

    # 5. Normalize repeated punctuation (!, ?, .)
    text = re.sub(r"\!{2,}", "!", text)
    text = re.sub(r"\?{2,}", "?", text)
    text = re.sub(r"\.{4,}", "...", text)  # Keep standard ellipsis '...'

    return text.strip()


def detect_language_with_confidence(text: str):
    """Detects language and returns (Language Name, Confidence Percentage)."""
    if not text.strip():
        return "Unknown", 0.0

    # Get confidence values for top languages
    confidence_values = detector.compute_language_confidence_values(text)

    if not confidence_values:
        return "Unknown", 0.0

    top_result = confidence_values[0]
    lang_name = top_result.language.name.title()
    confidence_pct = round(top_result.value * 100, 2)

    return lang_name, confidence_pct


# --- Streamlit UI Setup ---
st.set_page_config(page_title="aiTransform | Language Detector & Text Cleaner", layout="wide")

st.title("🌐 aiTransform")
st.caption("Language Detector & Text Cleaner")

st.markdown("---")

# User Input
user_input = st.text_area(
    "Paste your text below:",
    height=180,
    placeholder="Type or paste text here (e.g., English, Urdu, or mixed content)...",
)

if st.button("✨ Transform Text", type="primary"):
    if user_input.strip():
        cleaned = clean_text(user_input)
        lang, confidence = detect_language_with_confidence(user_input)

        # Language Detection Banner
        st.subheader("📊 Language Detection Result")
        col_lang, col_conf = st.columns(2)
        with col_lang:
            st.metric(label="Detected Language", value=lang)
        with col_conf:
            st.metric(label="Confidence Score", value=f"{confidence}%")

        st.markdown("---")

        # Side-by-Side Comparison
        st.subheader("🔍 Side-by-Side Comparison")
        col_orig, col_clean = st.columns(2)

        with col_orig:
            st.markdown("**Original Text**")
            st.text_area("Original Output", value=user_input, height=250, disabled=True, label_visibility="collapsed")
            st.caption(f"Character count: {len(user_input)}")

        with col_clean:
            st.markdown("**Cleaned Text**")
            st.text_area("Cleaned Output", value=cleaned, height=250, disabled=True, label_visibility="collapsed")
            st.caption(f"Character count: {len(cleaned)}")

    else:
        st.warning("Please enter some text to process.")