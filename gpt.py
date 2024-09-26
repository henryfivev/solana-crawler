import os
from dotenv import load_dotenv, find_dotenv
import requests

load_dotenv(find_dotenv())
url = "https://api.gptapi.us/v1/chat/completions"
api_key = os.environ.get("OPENAI_API_KEY")

def askGPT(messages):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": messages
    }
    response = requests.post(url, json=data, headers=headers)

    # 打印返回结果
    print(response.status_code)
    print(response.json(), '\n')
    return response.json()

if __name__ == "__main__":
    messages = [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            }
        ]
    
    content = [
            "could you tell me how to fry eggs?",
            "now i know how to fry egss. could you tell me how to make a sandwith with a fried egg?"
        ]
    
    for i in range(len(content)):
        messages.append({
                "role": "user",
                "content": content[i]
            })
        response_json = askGPT(messages)
        messages.append(response_json['choices'][0]['message'])