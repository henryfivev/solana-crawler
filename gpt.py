import os
from dotenv import load_dotenv, find_dotenv
import requests

load_dotenv(find_dotenv())

api_key = os.environ.get("OPENAI_API_KEY"),
url = "https://api.gptapi.us/v1/chat/completions"

# os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'
# os.environ["HTTP_PROXY"] = 'http://127.0.0.1:7890'

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer '+api_key
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
            "content": "Hello! What can you do for me?"
        }
    ]
}
response = requests.post(url, json=data, headers=headers)

# 打印返回结果
print(response.status_code)
print(response.json(), '\n')
