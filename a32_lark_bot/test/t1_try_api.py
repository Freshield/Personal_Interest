# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: t1_try_api.py
@Time: 2023-03-07 21:26
@Last_update: 2023-03-07 21:26
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""

import json
import requests

json_data = {
    'encrypt': 'ds3da3sj32421lkkld4s5ao',
}
# json_data = json.dumps(json_data)
response = requests.post('http://127.0.0.1:9876/challenge', json=json_data)
# response = requests.post('http://8.210.212.195:9876/challenge', json=json_data)


print(response)
print(response.text)

