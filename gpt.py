import requests

api_key = ""
url = "https://api.gptapi.us/v1/chat/completions"

headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer sk-LuHfwSuzHWPMCTof100dC7543bE5405489F5C191E40c1d57'
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
