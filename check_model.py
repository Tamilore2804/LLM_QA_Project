import google.generativeai as genai

# Paste your REAL key here
API_KEY = "AIzaSyDgkS29rhsJQ2i0Dmcl9xMdW713G0Sdgpg" 
genai.configure(api_key=API_KEY)

print("Checking available models...")
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(f"- {m.name}")
except Exception as e:
    print(f"Error: {e}")