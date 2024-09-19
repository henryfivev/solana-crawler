1. 选择一个url
2. 参考接口文档

## response

### getSignatureForAddress

{'jsonrpc': '2.0', 

'result': [
    {'blockTime': 1725257067, 'confirmationStatus': 'finalized', 'err': None, 'memo': None, 'signature': '5ZEYtBqjM1G8pHrrH5oq7eZcLN3bJUyxRLe3ZBFp1KB525NjCkegTaYGeVf6Ci2AgPJa8sfvFRkUXVgGdDcuPk2y', 'slot': 287298056},
    {'blockTime': 1725217527, 'confirmationStatus': 'finalized', 'err': None, 'memo': None, 'signature': 'gjFD43FVqjVZsCtg1hXEdK6gRUeMYFT3uxshQkMFtczCQRe256Svsu3JCb5iTnMpxASBWKd1eRKifDRaqmJN6Jb', 'slot': 287206042}, 
    {'blockTime': 1725217522, 'confirmationStatus': 'finalized', 'err': None, 'memo': None, 'signature': '2vCxWF2CmnfgzY4yXNSnoXCahvrVajoZ3J9vxRCpHbaVshm8XesGum9hjkaKG3udLeJUyuyrGUskNo7GXwxS4uuA', 'slot': 287206029}, 
    {'blockTime': 1725217479, 'confirmationStatus': 'finalized', 'err': None, 'memo': None, 'signature': 'mvH49EjuKR3jX2zRHa6okKptPNgRETxAmcBtrew2cGr2xCRFCfN9syTMMjZ1gdS5bh964TJua7rb9ow1DjK3swS', 'slot': 287205925}, 
    {'blockTime': 1725121411, 'confirmationStatus': 'finalized', 'err': None, 'memo': None, 'signature': 'QdEB3Abcoxg1eXJXXQD6k3gGpT5bRVPho3AKsECo9moAyppg67ejaczPF45VUFaiBDCEXKch8NSVDXY2WY7PSCJ', 'slot': 286979212}, 
    {'blockTime': 1725121393, 'confirmationStatus': 'finalized', 'err': None, 'memo': None, 'signature': '4RzpqJk8Z16agmT5MybBPoH1MjmKHvGquxxToNd1ieZkVm3yQ5igw3Y7h1qfoHa7KgX5dtvfYMbxxoVpszc7mZvX', 'slot': 286979170}, 
    {'blockTime': 1725121383, 'confirmationStatus': 'finalized', 'err': None, 'memo': None, 'signature': '2jCQDYSpgnmK9He4gwemd3L4vAeBLvq4cgSS3KKw64wDp6q1MDHHAzKkZBydvEEVvWLmhipj448HdzFC9VuekseV', 'slot': 286979146}
    ], 'id': 1}

### getTransaction

{'jsonrpc': '2.0', 
'result': {
    'blockTime': 1725257067, 
    'meta': {'computeUnitsConsumed': 450, 
        'err': None, 
        'fee': 15000, 
        'innerInstructions': [], 
        'loadedAddresses': {'readonly': [], 'writable': []}, 
        'logMessages': ['Program ComputeBudget111111111111111111111111111111 invoke [1]', 'Program ComputeBudget111111111111111111111111111111 success', 'Program ComputeBudget111111111111111111111111111111 invoke [1]', 'Program ComputeBudget111111111111111111111111111111 success', 'Program 11111111111111111111111111111111 invoke [1]', 'Program 11111111111111111111111111111111 success'], 
        'postBalances': [0, 103044145243, 1, 1], 
        'postTokenBalances': [], 
        'preBalances': [13633831981, 89410328262, 1, 1], 
        'preTokenBalances': [], 
        'rewards': [], 
        'status': {'Ok': None}}, 
    'slot': 287298056, 
    'transaction': {
        'message': {
            'accountKeys': ['DadEgL8xv3jB48UqEbC5y34zyMGBi8sH7r1oRn5oKukJ', '7RHDN1S2vEeAVYspqBuHjRw9jtVGzD6hm63uLb38BmY8', '11111111111111111111111111111111', 'ComputeBudget111111111111111111111111111111'], 
            'header': {'numReadonlySignedAccounts': 0, 'numReadonlyUnsignedAccounts': 2, 'numRequiredSignatures': 1}, 
            'instructions': [
                {'accounts': [], 'data': '3DVGviTXKAPH', 'programIdIndex': 3, 'stackHeight': None}, 
                {'accounts': [], 'data': 'LKoyXd', 'programIdIndex': 3, 'stackHeight': None}, 
                {'accounts': [0, 1], 'data': '3Bxs4RsMzdreNCto', 'programIdIndex': 2, 'stackHeight': None}], 
            'recentBlockhash': 'HxKDu9kRJBaq2y1yvXrbiTFF7muYyP1rY2EtSMKKkF21'}, 
        'signatures': ['5ZEYtBqjM1G8pHrrH5oq7eZcLN3bJUyxRLe3ZBFp1KB525NjCkegTaYGeVf6Ci2AgPJa8sfvFRkUXVgGdDcuPk2y']}}, 
'id': 1} 

{'jsonrpc': '2.0', 'result': {'blockTime': 1725217527, 'meta': {'computeUnitsConsumed': 1950, 'err': None, 'fee': 5024, 'innerInstructions': [], 'loadedAddresses': {'readonly': [], 'writable': []}, 'logMessages': ['Program ComputeBudget111111111111111111111111111111 invoke [1]', 'Program ComputeBudget111111111111111111111111111111 success', 'Program ComputeBudget111111111111111111111111111111 invoke [1]', 'Program ComputeBudget111111111111111111111111111111 success', 'Program 11111111111111111111111111111111 invoke [1]', 'Program 11111111111111111111111111111111 success', 'Program 11111111111111111111111111111111 invoke [1]', 'Program 11111111111111111111111111111111 success', 'Program 11111111111111111111111111111111 invoke [1]', 'Program 11111111111111111111111111111111 success', 'Program 11111111111111111111111111111111 invoke [1]', 'Program 11111111111111111111111111111111 success', 'Program 11111111111111111111111111111111 invoke [1]', 'Program 11111111111111111111111111111111 success', 'Program 11111111111111111111111111111111 invoke [1]', 'Program 11111111111111111111111111111111 success', 'Program 11111111111111111111111111111111 invoke [1]', 'Program 11111111111111111111111111111111 success', 'Program 11111111111111111111111111111111 invoke [1]', 'Program 11111111111111111111111111111111 success', 'Program 11111111111111111111111111111111 invoke [1]', 'Program 11111111111111111111111111111111 success', 'Program 11111111111111111111111111111111 invoke [1]', 'Program 11111111111111111111111111111111 success', 'Program 11111111111111111111111111111111 invoke [1]', 'Program 11111111111111111111111111111111 success'], 'postBalances': [475727451, 1287215429, 1645733521, 3761950, 902080, 317667466, 2915920, 13633831981, 176505440, 161931953, 66201110, 15517880632, 1, 1], 'postTokenBalances': [], 'preBalances': [475733575, 1287215329, 1645733421, 3761850, 901980, 317667366, 2915820, 13633831881, 176505340, 161931853, 66201010, 15517880532, 1, 1], 'preTokenBalances': [], 'rewards': [], 'status': {'Ok': None}}, 'slot': 287206042, 'transaction': {'message': {'accountKeys': ['Habp5bncMSsBC3vkChyebepym5dcTNRYeg2LVG464E96', '1Zm1rDEAxfSCUcjcKANSNBReurcFUMhgGC3wWwxmWZi', '5sa8bSGg1Njiaw4rkPamDqscEuHWj2ygcQxeQL96ATFy', '6AEsiuJBARThTXiaJMjp5jGUTzACybCha7XK1TK5FE9H', '8R8wrwU4Ug3iNBXSH9JHJsE1UDKhhJ8f2dAnFtffrgLw', '94cQQ5uYUzndAxjTbqtdiSKgNc8oM466e2wGBmgYXwey', 'CX91zHmzhA4cnjUARQvMG6vfckWfmzmJgePcD7Y5CueR', 'DadEgL8xv3jB48UqEbC5y34zyMGBi8sH7r1oRn5oKukJ', 'EnqP8nKXVFV5prqVVLzAamBsEhQDYVkDjTtHhfo6GaGN', 'FL2v6qWb7sadwkp88jd7f6Xag4CVsXwX9t2HfXv1kHAW', 'FtcBAZTttxaCGUTyWmvMm5fvvDRrawo2GrN8wYCnZY1f', 'HpBT6QceinQDSjhPDr74AmRY2fQFMbgWCwYkvVu7hQg9', '11111111111111111111111111111111', 'ComputeBudget111111111111111111111111111111'], 'header': {'numReadonlySignedAccounts': 0, 'numReadonlyUnsignedAccounts': 2, 'numRequiredSignatures': 1}, 'instructions': [{'accounts': [], 'data': 'GZv9UT', 'programIdIndex': 13, 'stackHeight': None}, {'accounts': [], 'data': '3GL7Yb6Rijcb', 'programIdIndex': 13, 'stackHeight': None}, {'accounts': [0, 7], 'data': '3Bxs4HanWsHUZCbH', 'programIdIndex': 12, 'stackHeight': None}, {'accounts': [0, 4], 'data': '3Bxs4HanWsHUZCbH', 'programIdIndex': 12, 'stackHeight': None}, {'accounts': [0, 2], 'data': '3Bxs4HanWsHUZCbH', 'programIdIndex': 12, 'stackHeight': None}, {'accounts': [0, 10], 'data': '3Bxs4HanWsHUZCbH', 'programIdIndex': 12, 'stackHeight': None}, {'accounts': [0, 11], 'data': '3Bxs4HanWsHUZCbH', 'programIdIndex': 12, 'stackHeight': None}, {'accounts': [0, 1], 'data': '3Bxs4HanWsHUZCbH', 'programIdIndex': 12, 'stackHeight': None}, {'accounts': [0, 3], 'data': '3Bxs4HanWsHUZCbH', 'programIdIndex': 12, 'stackHeight': None}, {'accounts': [0, 9], 'data': '3Bxs4HanWsHUZCbH', 'programIdIndex': 12, 'stackHeight': None}, {'accounts': [0, 8], 'data': '3Bxs4HanWsHUZCbH', 'programIdIndex': 12, 'stackHeight': None}, {'accounts': [0, 5], 'data': '3Bxs4HanWsHUZCbH', 'programIdIndex': 12, 'stackHeight': None}, {'accounts': [0, 6], 'data': '3Bxs4HanWsHUZCbH', 'programIdIndex': 12, 'stackHeight': None}], 'recentBlockhash': '7ExF1EV2v2UhWwJJSm9tWRG3cGrD9UpQgMNPWh4qQ7Fe'}, 'signatures': ['gjFD43FVqjVZsCtg1hXEdK6gRUeMYFT3uxshQkMFtczCQRe256Svsu3JCb5iTnMpxASBWKd1eRKifDRaqmJN6Jb']}}, 'id': 1}

出现以下response

{'jsonrpc': '2.0', 'error': {'code': 429, 'message': 'Too many requests for a specific RPC call'}, 'id': 1} 

### openai

{'id': 'chatcmpl-3DYu6ibW4mnjWEwhZH5WozWrRTq8U', 
'object': 'chat.completion', 
'created': 1726731159, 
'model': 'gpt-3.5-turbo', 
'choices': [{
    'index': 0, 
    'message': {
        'role': 'assistant', 
        'content': "Hello! I'm here to help you with a variety of tasks. Whether you need information, advice, assistance with a project, or just someone to talk to, feel free to let me know how I can assist you today!"}, 
    'logprobs': None, 
    'finish_reason': 'stop'}], 
'system_fingerprint': 'fp_ecb642f809', 
'usage': {
    'completion_tokens': 0, 
    'prompt_tokens': 0, 
    'total_tokens': 0}} 
