爬取逻辑

1. 选择一个url
2. 参考接口文档写请求

chainabuse上this is the scammer标记是什么意思？

## todo

1. 分析response字段
2. try-exception处理error
3. apikey更换

## response字段

`getTransaction` 是 Solana 的一个 RPC 方法，用于获取特定交易的详细信息。以下是一些主要字段：

1. **slot**: 交易处理的槽位。
2. **transaction**: 交易对象，可以是 JSON 格式或编码的二进制数据，具体取决于编码参数。
3. **blockTime**: 交易处理的估计时间（Unix 时间戳）。
4. **meta**: 交易状态元数据对象，包括以下子字段：
   - **err**: 如果交易失败，包含错误信息；如果交易成功，则为 null。
   - **fee**: 交易费用。
   - **preBalances**: 交易前的账户余额数组。
   - **postBalances**: 交易后的账户余额数组。
   - **innerInstructions**: 内部指令列表，如果未启用内部指令记录，则为 null。
   - **preTokenBalances**: 交易前的代币余额列表。
   - **postTokenBalances**: 交易后的代币余额列表。
   - **logMessages**: 日志消息数组，如果未启用日志消息记录，则为 null。
   - **rewards**: 交易级别的奖励信息数组。

你在使用 `getTransaction` 方法时遇到什么问题了吗？

源: 与 Copilot 的对话， 2024/9/23
(1) getTransaction RPC Method - Solana. https://solana.com/docs/rpc/http/gettransaction.
(2) getTransaction RPC Method | Solana. https://drpc.org/docs/solana-api/transactionsinfo/getTransaction.
(3) getTransaction | Solana - Chainstack Developer Portal. https://docs.chainstack.com/reference/gettransaction.
(4) getTransactionCount RPC Method - Solana. https://solana.com/docs/rpc/http/gettransactioncount.
(5) undefined. https://api.devnet.solana.com-X.
(6) undefined. https://solana.drpc.org.

## error未处理

Traceback (most recent call last):
  File "/Users/henryfive/miniconda3/envs/crawler/lib/python3.8/site-packages/urllib3/connectionpool.py", line 775, in urlopen
    self._prepare_proxy(conn)
  File "/Users/henryfive/miniconda3/envs/crawler/lib/python3.8/site-packages/urllib3/connectionpool.py", line 1044, in _prepare_proxy
    conn.connect()
  File "/Users/henryfive/miniconda3/envs/crawler/lib/python3.8/site-packages/urllib3/connection.py", line 652, in connect
    sock_and_verified = _ssl_wrap_socket_and_match_hostname(
  File "/Users/henryfive/miniconda3/envs/crawler/lib/python3.8/site-packages/urllib3/connection.py", line 805, in _ssl_wrap_socket_and_match_hostname
    ssl_sock = ssl_wrap_socket(
  File "/Users/henryfive/miniconda3/envs/crawler/lib/python3.8/site-packages/urllib3/util/ssl_.py", line 465, in ssl_wrap_socket
    ssl_sock = _ssl_wrap_socket_impl(sock, context, tls_in_tls, server_hostname)
  File "/Users/henryfive/miniconda3/envs/crawler/lib/python3.8/site-packages/urllib3/util/ssl_.py", line 509, in _ssl_wrap_socket_impl
    return ssl_context.wrap_socket(sock, server_hostname=server_hostname)
  File "/Users/henryfive/miniconda3/envs/crawler/lib/python3.8/ssl.py", line 500, in wrap_socket
    return self.sslsocket_class._create(
  File "/Users/henryfive/miniconda3/envs/crawler/lib/python3.8/ssl.py", line 1073, in _create
    self.do_handshake()
  File "/Users/henryfive/miniconda3/envs/crawler/lib/python3.8/ssl.py", line 1342, in do_handshake
    self._sslobj.do_handshake()
ConnectionResetError: [Errno 54] Connection reset by peer

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/henryfive/miniconda3/envs/crawler/lib/python3.8/site-packages/requests/adapters.py", line 667, in send
    resp = conn.urlopen(
  File "/Users/henryfive/miniconda3/envs/crawler/lib/python3.8/site-packages/urllib3/connectionpool.py", line 843, in urlopen
    retries = retries.increment(
  File "/Users/henryfive/miniconda3/envs/crawler/lib/python3.8/site-packages/urllib3/util/retry.py", line 474, in increment
    raise reraise(type(error), error, _stacktrace)
  File "/Users/henryfive/miniconda3/envs/crawler/lib/python3.8/site-packages/urllib3/util/util.py", line 38, in reraise
    raise value.with_traceback(tb)
  File "/Users/henryfive/miniconda3/envs/crawler/lib/python3.8/site-packages/urllib3/connectionpool.py", line 775, in urlopen
    self._prepare_proxy(conn)
  File "/Users/henryfive/miniconda3/envs/crawler/lib/python3.8/site-packages/urllib3/connectionpool.py", line 1044, in _prepare_proxy
    conn.connect()
  File "/Users/henryfive/miniconda3/envs/crawler/lib/python3.8/site-packages/urllib3/connection.py", line 652, in connect
    sock_and_verified = _ssl_wrap_socket_and_match_hostname(
  File "/Users/henryfive/miniconda3/envs/crawler/lib/python3.8/site-packages/urllib3/connection.py", line 805, in _ssl_wrap_socket_and_match_hostname
    ssl_sock = ssl_wrap_socket(
  File "/Users/henryfive/miniconda3/envs/crawler/lib/python3.8/site-packages/urllib3/util/ssl_.py", line 465, in ssl_wrap_socket
    ssl_sock = _ssl_wrap_socket_impl(sock, context, tls_in_tls, server_hostname)
  File "/Users/henryfive/miniconda3/envs/crawler/lib/python3.8/site-packages/urllib3/util/ssl_.py", line 509, in _ssl_wrap_socket_impl
    return ssl_context.wrap_socket(sock, server_hostname=server_hostname)
  File "/Users/henryfive/miniconda3/envs/crawler/lib/python3.8/ssl.py", line 500, in wrap_socket
    return self.sslsocket_class._create(
  File "/Users/henryfive/miniconda3/envs/crawler/lib/python3.8/ssl.py", line 1073, in _create
    self.do_handshake()
  File "/Users/henryfive/miniconda3/envs/crawler/lib/python3.8/ssl.py", line 1342, in do_handshake
    self._sslobj.do_handshake()
urllib3.exceptions.ProtocolError: ('Connection aborted.', ConnectionResetError(54, 'Connection reset by peer'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "post.py", line 90, in <module>
    trans_response_json = getSolTransaction(signature)
  File "post.py", line 75, in getSolTransaction
    response = requests.post(url, json=data, headers=headers)
  File "/Users/henryfive/miniconda3/envs/crawler/lib/python3.8/site-packages/requests/api.py", line 115, in post
    return request("post", url, data=data, json=json, **kwargs)
  File "/Users/henryfive/miniconda3/envs/crawler/lib/python3.8/site-packages/requests/api.py", line 59, in request
    return session.request(method=method, url=url, **kwargs)
  File "/Users/henryfive/miniconda3/envs/crawler/lib/python3.8/site-packages/requests/sessions.py", line 589, in request
    resp = self.send(prep, **send_kwargs)
  File "/Users/henryfive/miniconda3/envs/crawler/lib/python3.8/site-packages/requests/sessions.py", line 703, in send
    r = adapter.send(request, **kwargs)
  File "/Users/henryfive/miniconda3/envs/crawler/lib/python3.8/site-packages/requests/adapters.py", line 682, in send
    raise ConnectionError(err, request=request)
requests.exceptions.ConnectionError: ('Connection aborted.', ConnectionResetError(54, 'Connection reset by peer'))

## response样例

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