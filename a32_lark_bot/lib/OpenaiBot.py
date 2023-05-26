# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: OpenaiBot.py
@Time: 2023-03-08 11:27
@Last_update: 2023-03-08 11:27
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
import os
import aiohttp
import requests
from lib.logs import LOGGER


class OpenaiBot(object):
    """调用openai的机器人"""
    def __init__(self, temperature=0.5):
        self.api_key = os.environ.get('OPENAI_API_KEY')
        self.model_engine = "gpt-3.5-turbo"
        self.temperature = temperature
        self.default_role = '你是ChatGPT，OpenAI训练的大规模语言模型，简明的回答用户的问题。'
        self.get_engine_list()

    def construct_message(self, role, new_msg, history_list, keep_history=3):
        """
        构造message，这里history_list是一个list，每个元素是一个tuple
        """
        msg_list = [{"role": "system", "content": role}]
        history_list = history_list[-keep_history:]
        for user, assistant in history_list:
            msg_list.append({"role": "user", "content": user})
            msg_list.append({"role": "assistant", "content": assistant})
        msg_list.append({"role": "user", "content": new_msg})

        return msg_list

    def get_engine_list(self):
        url = 'https://api.openai.com/v1/engines'
        header = {"Authorization": f'Bearer {self.api_key}'}
        response = requests.get(url, headers=header).json()

    async def get_response(self, role, new_msg, history_list, temperature=None, keep_history=3):
        """
        通过openai获取回复
        """
        url = 'https://api.openai.com/v1/chat/completions'
        header = {"Authorization": f'Bearer {self.api_key}', "Content-Type": "application/json; charset=utf-8"}
        msg_list = self.construct_message(role, new_msg, history_list, keep_history)
        temp = self.temperature if temperature is None else temperature
        req_dict = {
            'model': self.model_engine, 'temperature': float(temp), 'messages': msg_list}
        LOGGER.info(req_dict)
        req_dict = json.dumps(req_dict)

        async with aiohttp.ClientSession() as session:
            async with session.post(url, data=req_dict, headers=header) as res:
                response = await res.json()
                LOGGER.info(response)
                content = response['choices'][0]['message']['content']

                return content


if __name__ == '__main__':
    openai_bot = OpenaiBot()
    # openai_bot.get_response(openai_bot.default_role, '你好', [])

