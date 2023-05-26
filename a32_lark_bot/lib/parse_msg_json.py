# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: parse_msg_json.py
@Time: 2023-03-08 11:38
@Last_update: 2023-03-08 11:38
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


def parse_msg_json(json_dict):
    """
    解析json_dict中的msg
    """
    event_type = json_dict['header']['event_type']
    chat_type = json_dict['event']['message']['chat_type']
    message_id = json_dict['event']['message']['message_id']
    user_open_id = json_dict['event']['sender']['sender_id']['open_id']
    content = json_dict['event']['message']['content']
    content = json.loads(content)['text']

    return {
        'event_type': event_type, 'chat_type': chat_type, 'message_id': message_id,
        'user_open_id': user_open_id, 'content': content}
