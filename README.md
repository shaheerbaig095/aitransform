# aiTransform: Language Detector & Text Cleaner

**Task Reference:** TPT-2026-03084 | ZR-26-00741  
**Live Application URL:** [Insert Streamlit Community Cloud / Render Link Here]  
**GitHub Repository:** [Insert Repository Link Here]

---

## 📌 Project Overview
`aiTransform` is a web application designed to process unstructured user-submitted text by:
1. **Detecting Language & Confidence Score**: Identifying the dominant language (e.g., English, Urdu, French, Spanish) along with a percentage confidence metric using the `Lingua` statistical NLP library.
2. **Text Cleanup**: Normalizing messy user input by removing excess whitespace, collapsing repeated punctuation (`???` → `?`), and standardizing line breaks.
3. **Side-by-Side Visual Comparison**: Presenting original and cleaned text in a dual-column interface.

---

## 🚀 Features
- **Accurate Language Detection**: Supports multi-language detection including script-based languages like Urdu and Arabic.
- **Rule-Based Text Normalization**:
  - Replaces multiple spaces/tabs with a single space.
  - Collapses 3+ line breaks into clean paragraph breaks (`\n\n`).
  - Normalizes excessive exclamation and question marks.
- **Side-by-Side UI**: Instant visual comparison with character counts for both raw and processed text.

---

## 🛠️ Tech Stack
- **Language**: Python 3.10+
- **Frontend / Framework**: Streamlit
- **Language Detection Engine**: `lingua-language-detector`
- **Text Processing**: Python `re` (Regular Expressions)

---

## 💻 Local Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/aitransform.git](https://github.com/YOUR_USERNAME/aitransform.git)
   cd aitransform