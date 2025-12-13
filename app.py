from flask import Flask, render_template, request
import google.generativeai as genai
import re
import string
import os

app = Flask(__name__)

# --- SETUP ---
API_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyDgkS29rhsJQ2i0Dmcl9xMdW713G0Sdgpg")
genai.configure(api_key=API_KEY)

def preprocess_input(user_text):
    text = user_text.lower()
    text = re.sub(f"[{string.punctuation}]", "", text)
    tokens = text.split()
    return " ".join(tokens), tokens

@app.route('/', methods=['GET', 'POST'])
def home():
    data = {}
    if request.method == 'POST':
        question = request.form.get('question')
        if question:
            # Preprocess
            processed, tokens = preprocess_input(question)
            
            # API Call
            try:
                model = genai.GenerativeModel('gemini-2.5-flash')
                response = model.generate_content(processed)
                answer = response.text
            except Exception as e:
                answer = f"Error: {e}"
            
            data = {
                'question': question,
                'processed': processed,
                'tokens': tokens,
                'answer': answer
            }
    
    return render_template('index.html', **data)

if __name__ == '__main__':
    app.run(debug=True)