import google.generativeai as genai
import re
import string
import os

# --- SETUP ---
# Replace with your actual key from aistudio.google.com
API_KEY = "YOUR_GEMINI_API_KEY" 

def preprocess_input(user_text):
    # 1. Lowercase
    text = user_text.lower()
    # 2. Remove punctuation
    text = re.sub(f"[{string.punctuation}]", "", text)
    # 3. Tokenize
    tokens = text.split()
    # Rejoin for API
    processed_text = " ".join(tokens)
    return processed_text, tokens

def get_gemini_response(prompt):
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"API Error: {e}"

def main():
    print("--- CLI NLP Q&A (Gemini) ---")
    while True:
        q = input("\nAsk a question (or 'exit'): ")
        if q.lower() == 'exit': break
        
        processed, tokens = preprocess_input(q)
        print(f"[DEBUG] Tokens: {tokens}")
        
        print("Thinking...")
        answer = get_gemini_response(processed)
        print(f"\nAnswer: {answer}\n" + "-"*30)

if __name__ == "__main__":
    main()