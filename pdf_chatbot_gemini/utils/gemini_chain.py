import os
from dotenv import load_dotenv
import google.generativeai as genai
from .pdf_reader import extract_text_from_pdf

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def get_gemini_answer(pdf_path, query, detail_level="Balanced", max_pages=5, context=None):
    if not api_key:
        return "⚠️ Gemini API key not found. Please check your .env"

    try:
        pdf_text = extract_text_from_pdf(pdf_path, max_pages=max_pages)

        prompt = f"""
You are an intelligent assistant. Answer the user's question in a {detail_level.lower()} and helpful way based only on the provided PDF content.

PDF Content:
{pdf_text}

"""
        if context:
            prompt += f"\nPrevious Answer for Reference:\n{context}\n"

        prompt += f"\nUser's Question:\n{query}"

        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        return f"❌ Gemini API error: {e}"
