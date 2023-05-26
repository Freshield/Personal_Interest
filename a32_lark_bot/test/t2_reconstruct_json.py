# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: t2_reconstruct_json.py
@Time: 2023-03-07 22:15
@Last_update: 2023-03-07 22:15
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
from data.test.user_direct import user_direct_dict
from data.test.group_msg import group_msg

# message_id = user_direct_dict['event']['message']['message_id']
# content = user_direct_dict['event']['message']['content']
# print(content)
# print(type(content))
# content = json.loads(content)['text']
# print(content)
# print(type(content))

data_dict = user_direct_dict
data_dict = group_msg
with open('../data/test/group_msg.txt', 'w') as f:
    f.write(json.dumps(data_dict, indent=4, ensure_ascii=False))
