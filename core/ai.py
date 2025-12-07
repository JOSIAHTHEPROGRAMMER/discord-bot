import os
import groq


# Gemini setup

try:
    from google import genai
    GEMINI_KEY = os.getenv("GEMINI_API_KEY")
    if GEMINI_KEY:
        gemini_client = genai.Client(api_key=GEMINI_KEY)
        GEMINI_AVAILABLE = True
    else:
        gemini_client = None
        GEMINI_AVAILABLE = False
        print("[AI] GEMINI_API_KEY not set. Gemini disabled.")
except ImportError:
    gemini_client = None
    GEMINI_AVAILABLE = False
    print("[AI] google-genai library not installed. Gemini disabled.")


# Groq setup

GROQ_KEY = os.getenv("GROQ_API_KEY")
groq_client = None
if GROQ_KEY:
    groq_client = groq.Groq(api_key=GROQ_KEY)
else:
    print("[AI] GROQ_API_KEY not set. Groq disabled.")


# Ask Gemini

def ask_gemini(prompt: str) -> str:
    if not GEMINI_AVAILABLE or not gemini_client:
        return None
    try:
        response = gemini_client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text.strip()
    except Exception as e:
        print(f"[Gemini Error] {e}")
        return None


# Ask Groq (chat-style)

def ask_groq_chat(prompt: str) -> str:
    if not groq_client:
        return None
    try:
        chat_completion = groq_client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile"
        )
        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        print(f"[Groq Chat Error] {e}")
        return None


# Unified AI function (fallback)

def ask_ai(prompt: str) -> str:
   

    answer = ask_groq_chat(prompt)
    if answer:
        print("[AI] Groq responded")
        return answer, "Groq"
    
    answer = ask_gemini(prompt)
    if answer:
        print("[AI] Gemini responded")
        return answer, "Gemini"

    return "Both AI services are unavailable. Try again later."
