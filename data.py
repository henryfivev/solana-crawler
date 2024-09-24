import os
import json
import time
from dotenv import load_dotenv, find_dotenv
import requests
import pandas as pd

url = "https://api.gptapi.us/v1/embeddings"
api_key = os.environ.get("GPTAPI_EMBEDDING_KEY")
# os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:7890'
# os.environ["HTTP_PROXY"] = 'http://127.0.0.1:7890'

embeddings = []

def getEmbedding(content):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    data = {
        "model": "text-embedding-3-small",
        'input': str(content)
    }
    response = requests.post(url, json=data, headers=headers)
    time.sleep(1)

    if response.status_code == 200:
        embedding = response.json()['data'][0]['embedding']
        embeddings.append(embedding)
    else:
        print(f"Error: {response.status_code}, {response.text}")

    # 打印返回结果
    print(response.status_code)
    print(response.json(), '\n')
    return response.json()

if __name__ == "__main__":
    load_dotenv(find_dotenv())
    with open('./result/phishing_10.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    for item in data:
        print(item)
        getEmbedding(item)

    df = pd.DataFrame(embeddings)
    df.to_csv('embeddings.csv', index=False)