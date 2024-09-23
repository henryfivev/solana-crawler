import os
from dotenv import load_dotenv, find_dotenv
import requests

url = "https://api.gptapi.us/v1/chat/completions"
api_key = os.environ.get("OPENAI_API_KEY")
# os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'
# os.environ["HTTP_PROXY"] = 'http://127.0.0.1:7890'

def askGPT(content):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": content
            }
        ]
    }
    response = requests.post(url, json=data, headers=headers)

    # 打印返回结果
    print(response.status_code)
    print(response.json(), '\n')
    return response.json()

if __name__ == "__main__":
    load_dotenv(find_dotenv())
    askGPT("could you tell me how to fry eggs?")    