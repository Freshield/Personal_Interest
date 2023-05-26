# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: OpenaiBot.py
@Time: 2023-03-03 17:47
@Last_update: 2023-03-03 17:47
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import os
import openai


class OpenaiBot(object):
    """调用openai的机器人"""
    def __init__(self, temperature=0.5):
        openai.api_key = os.environ.get('OPENAI_API_KEY')
        self.model_engine = "gpt-3.5-turbo"
        self.temperature = temperature
        # try to call api
        openai.Engine.list()

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

    def get_response(self, role, new_msg, history_list, keep_history=3):
        """
        通过openai获取回复
        """
        msg_list = self.construct_message(role, new_msg, history_list, keep_history)
        response = openai.ChatCompletion.create(
            model=self.model_engine, messages=msg_list,
            temperature=self.temperature
        )
        content = response['choices'][0]['message']['content']

        return content


if __name__ == '__main__':
    openai_bot = OpenaiBot()
