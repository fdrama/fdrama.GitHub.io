# -*- coding: utf-8 -*-
# /usr/bin/python3
import os
import requests

cookie_file = '/home/admin/cookie'
cookie = open(cookie_file).read().strip()
headers = {'cookie': cookie, 'content-type': 'application/json;charset=UTF-8', 'User-Agent': 'Mozilla/5.0  (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163   Safari/537.36'}
data = '{"token": "glados.one"}'
response = requests.post('https://glados.rocks/api/user/checkin', headers=headers, data=data)
message = response.json()['message']

response = requests.get('https://glados.rocks/api/user/status', headers=headers)
left_days = response.json()['leftDays']

feishu_webhook_url = 'https://open.feishu.cn/open-apis/bot/v2/hook/8799894d-144e-46b9-a283-9ea52606b447'
data = {'msg_type': 'text', 'content': {'text': f'{message} {left_days}'}}
response = requests.post(feishu_webhook_url, json=data)
