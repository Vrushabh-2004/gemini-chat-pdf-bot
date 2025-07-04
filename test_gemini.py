import google.generativeai as genai

# Paste your real Gemini API key directly here for quick test
genai.configure(api_key="YOUR_GEMINI_API_KEY_HERE")

try:
    model = genai.GenerativeModel("models/gemini-pro")
    response = model.generate_content("Say hello in Kannada")
    print("✅ Gemini API Response:")
    print(response.text)
except Exception as e:
    print("❌ Error:", e)
