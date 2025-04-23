import requests
import os

API_KEY = os.getenv("GPT_API_KEY")
API_URL = "https://platform.krd/api/chat"

def ask_gpt(prompt, context):
    response = requests.post(API_URL, json={
        "question": prompt,
        "context": context
    }, headers={"Authorization": f"Bearer {API_KEY}"})
    return response.json().get("answer", "❌ خطا در پاسخ")
