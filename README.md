# aiTransform: Language Detector & Text Cleaner

**Task Reference:** TPT-2026-03084 | ZR-26-00741  
**Live Application URL:** https://aitransform-ddmnkgbfnwjuql68598rdm.streamlit.app/
**GitHub Repository:** https://github.com/shaheerbaig095/aitransform.git

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



   Test ID,Category,Raw Input Text,Detected Language,Confidence Score,Cleaned Output Result
TC-01,Standard English & Extra Spaces,This   is a    simple test  sentence.,English,99.8%,This is a simple test sentence.
TC-02,Excessive Punctuation,Are you serious??? This is amazing!!!!!,English,99.5%,Are you serious? This is amazing!
TC-03,Inconsistent Line Breaks,Paragraph 1\n\n\n\n\nParagraph 2 with extra   spaces.,English,99.9%,Paragraph 1\n\nParagraph 2 with extra spaces.
TC-04,Standard Urdu Script,یہ ایک سادہ سا جملہ ہے۔,Urdu,100.0%,یہ ایک سادہ سا جملہ ہے۔
TC-05,Noisy Urdu Script,کیا حال    ہے؟؟؟  سب   ٹھیک ہے!!!!,Urdu,98.7%,کیا حال ہے؟ سب ٹھیک ہے!
TC-06,Short English Word,Hello,English,88.4%,Hello
TC-07,Short Urdu Word,سلام,Urdu,91.2%,سلام
TC-08,Mixed Script (EN Dominant),Welcome to our platform! ہم آپ کو خوش آمدید کہتے ہیں۔,English,78.6%,Welcome to our platform! ہم آپ کو خوش آمدید کہتے ہیں۔
TC-09,Mixed Script (UR Dominant),آج کا موسم بہت اچھا ہے and I love it.,Urdu,74.2%,آج کا موسم بہت اچھا ہے and I love it.
TC-10,Roman Urdu / Slang,Aap kaise    ho??? Mein   teek hoon.,English (Latin),82.1%,Aap kaise ho? Mein teek hoon.
TC-11,Standard French,Bonjour Tout le   monde!  Comment allez-vous???,French,99.1%,Bonjour Tout le monde! Comment allez-vous?
TC-12,Standard Spanish,Hola   amigos!!!   ¿Cómo estás?,Spanish,98.9%,Hola amigos! ¿Cómo estás?
TC-13,Tabbed / Indented Text,\t\tHeader Title\n\t\t\tSub-content with   spaces.,English,99.7%,Header Title\nSub-content with spaces.
TC-14,Ellipsis Normalization,To be continued...... stay tuned.....,English,99.3%,To be continued... stay tuned...
TC-15,Multiline Mixed Script,TechAbout Company   \n\n\n\nخدمات اور ٹیکنالوجی!!   \n   Join us today.,English,71.5%,TechAbout Company\n\nخدمات اور ٹیکنالوجی!\nJoin us today.
