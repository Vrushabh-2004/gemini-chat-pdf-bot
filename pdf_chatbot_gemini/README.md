# 📄 Chat with Your Notes (Google Gemini Version)

This project allows you to upload a PDF file and ask questions about its content using Google's Gemini AI model.

## 🧠 Technologies
- Streamlit
- Google Gemini (via google-generativeai)
- PyMuPDF for PDF reading
- dotenv for key handling

## 🚀 How to Run

1. Install packages:
```
pip install -r requirements.txt
```

2. Add your Gemini API key in the `.env` file:
```
GEMINI_API_KEY=your-real-gemini-key-here
```

Get one from: https://makersuite.google.com/app/apikey

3. Run the app:
```
streamlit run main.py
```