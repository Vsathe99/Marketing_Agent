import os, requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={api_key}"

data = {
  "contents": [{"parts":[{"text":"Who invented Transformer architecture?"}]}]
}

resp = requests.post(url, json=data)
print(resp.status_code, resp.text)
