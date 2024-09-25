import os
import json
import time
from dotenv import load_dotenv, find_dotenv
import requests
import pandas as pd

load_dotenv(find_dotenv())
url = "https://api.gptapi.us/v1/embeddings"
api_key = os.environ.get("GPTAPI_EMBEDDING_KEY")

file_path = 'hack_5.json'
current_label = 0

embeddings = []
labels = []

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
    # 打印返回结果
    print(response.status_code)
    print(response.json(), '\n')

    if response.status_code == 200:
        embedding = response.json()['data'][0]['embedding']
        embeddings.append(embedding)
        labels.append(current_label)
    else:
        print(f"Error: {response.status_code}, {response.text}")

    return response.json()

if __name__ == "__main__":
    with open(f'./result/{file_path}', 'r', encoding='utf-8') as file:
        data = json.load(file)
    for item in data:
        getEmbedding(item)

    embedding_df = pd.DataFrame(embeddings)
    embedding_df.to_csv('nonphishing_embeddings.csv', index=False)

    labels_df = pd.DataFrame(labels, columns=['label'])
    labels_df.to_csv('nonphishing_labels.csv', index=False)