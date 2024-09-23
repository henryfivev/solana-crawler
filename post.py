import time
import json
import requests

url = 'https://api.mainnet-beta.solana.com'
file_path = './data/response'

# 标签数据有误，需要大小写敏感
phishing_address = [
    "DadEgL8xv3jB48UqEbC5y34zyMGBi8sH7r1oRn5oKukJ",
    "13qESscnJbEZjsUi4fv47nvxMcHjp4VNRapSuog1wYus",
    "CzXA1gwnbEByQfvNN5DbYZRLxxdDUGUgqCjTJrEBys1x",
    "48mpgkYNJuJhuFt6uk3N7erEVn2GXpFtStAhSK49Rx71",
    "HQwqACbdUqrcbUmbv53B72HJKuQZ6XeSG1zb9H1rbzn3",
    "CpXF4pfESN44aiHVUC37ypNcRvNpKqwd1aEyvRSU5axW",
    "fh2djPUyG3B8bv4jA3TUGtQnsEKRMy5iLaKh6bEQvie",
    "73EEefkLgw9beP6YNqtqwk2T8UuBCW7QKEDfjQi7A3Q7",
    "3WZSjw8CTn7KTDEKsWRv3E6ysACriGcntGtdph5ern9c",
    "8zY6jjLRxGJgE4yKxFNigdXCbibTPLXMmuCkUqFS32Nq"
]

nft_airdrop_address = [
    "EpUuGSj4Qp46fzedkq8ForC5vfRb8nudp2u17H2tWGPb",
    "DqFeG96sa5S7GvHiSk3rjw6xNzpyfK75yzq85RvZXXDA",
    "FbyJGnaGKod83GeGgugRxLApfxpUA1bg1su4rqKxqyjr",
    "2AWYu12aM1cr5V4Lsn5mMPJpoSTaajt1JfWmA5LJ8Ltz", 
    "J1oUdSi2QPqJdJouV6WvP9q3hN2tTrk8hRD1sUSBxZxp",
    "Fwo934dpJBJd13fFEtvyeD56kcTNoLf4vLY3PqxX5DNz",
    "22QHmhd8AtuaDYyRQmmHAbLGghciMKBiGGSxe5Qd9XAE",
    "4Kcm1GHZryfGcDhYLf2u9kLPM3JXPLkTzJJAHYYVZAoR",
    "HbtSzZgPZJabqWgXV9t7S4n6RwkmFuUDze1tQYX22oAP",
    "9p6adsm5fEy2Gm6peD6JPNi3UQ7Bd3Yj4xnTCf51RQTW"
]

def getSigForAddr(addr):
    headers = {
        'Content-Type': 'application/json',
        # 'Authorization': ''
    }
    data = {
        'jsonrpc': '2.0',
        'id': 1,
        'method': "getSignaturesForAddress",
        "params": [
            addr,
            {
                "limit": 10
            }
        ]
    }
    response = requests.post(url, json=data, headers=headers)

    # print(response.status_code)
    # print(response.json())
    return response.json()

def getSolTransaction(signature):
    headers = {
        'Content-Type': 'application/json',
        # 'Authorization': ''
    }
    data = {
        'jsonrpc': '2.0',
        'id': 1,
        'method': "getTransaction",
        "params": [
            signature,
            {
                "encoding": "jsonParsed",
                "maxSupportedTransactionVersion": 0
            }
        ]
    }

    response = requests.post(url, json=data, headers=headers)
    time.sleep(5) # api接口限制，每10秒

    return response.json()

if __name__ == "__main__":
    file_path = file_path+str(int(time.time()))+'.txt'

    for address in phishing_address:
        with open(file_path, 'a') as file:
            file.write('\n## '+ address +'\n')
        sig_response_json = getSigForAddr(address)
        signatures = [entry['signature'] for entry in sig_response_json['result']]
        
        for signature in signatures:
            trans_response_json = getSolTransaction(signature)
            print(trans_response_json)

            with open(file_path, 'a') as file:
                file.write(json.dumps(trans_response_json, indent=4)+'\n')
