# gpt_service.py
import requests
import json
from decouple import config

def get_summary_from_gpt(content):
    api_key = config('GPT_API_KEY')
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Summarize the following text extracted from a powerpoint or word file :\n{content}"}
        ]
    }
    
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json={"model": "gpt-4", "messages": data["messages"]})
    
    if response.status_code == 200:
        result = json.loads(response.text)
        summary = result['choices'][0]['message']['content'].strip()
        return summary
    else:
        return f"Error in summarization: {response.text}"