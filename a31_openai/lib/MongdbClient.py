# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: MongdbClient.py
@Time: 2023-03-03 20:25
@Last_update: 2023-03-03 20:25
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import pymongo
from hashlib import sha256


class MongodbClient(object):
    """Mongodb客户端"""
    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient["openai_bot"]
        self.user_info = self.mydb['user_info']
        self.user_history = self.mydb['user_history']

    def check_user_exist(self, username, password):
        """检测用户是否存在"""
        username = sha256(username.encode('utf8')).hexdigest()
        password = sha256(password.encode('utf8')).hexdigest()
        mydoc = self.user_info.find({'username': username, 'password': password}).limit(1)
        res = [x for x in mydoc]

        return len(res) >= 1

    def update_user_access_token(self, username, access_token):
        """更新数据库的access_token以便后续使用"""
        username = sha256(username.encode('utf8')).hexdigest()
        # 先看是否有这个用户
        mydoc = self.user_history.find({'username': username}).limit(1)
        res = [x for x in mydoc]
        # 如果没有则直接创建
        if len(res) < 1:
            mydict = {
                'username': username, 'access_token': access_token,
                'role': '你是ChatGPT，OpenAI训练的大规模语言模型，简明的回答用户的问题。', 'history': []}
            _ = self.user_history.insert_one(mydict)
        # 如果有则更新
        else:
            self.user_history.update_one({'username': username}, {'$set': {'access_token': access_token}})

    def get_user_chat_history(self, access_token):
        """获取用户的聊天历史"""
        mydoc = self.user_history.find({'access_token': access_token}).limit(1)
        res = [x for x in mydoc]
        history_str, history_list = '', []
        role = '你是ChatGPT，OpenAI训练的大规模语言模型，简明的回答用户的问题。'
        if len(res) >= 1:
            # 遍历加到history中
            history_list = res[0]['history']
            role = res[0]['role']
            for qus, ans in history_list[::-1]:
                history_str += f'Q: {qus}\nA: {ans}\n'

        return history_str, history_list, role

    def update_user_chat_history(self, access_token, qus, ans):
        """更新用户的聊天历史"""
        mydoc = self.user_history.find({'access_token': access_token}).limit(1)
        res = [x for x in mydoc]
        if len(res) >= 1:
            self.user_history.update_one({'access_token': access_token}, {'$push': {'history': (qus, ans)}})

    def delete_user_chat_history(self, access_token):
        """删除用户的聊天历史"""
        mydoc = self.user_history.find({'access_token': access_token}).limit(1)
        res = [x for x in mydoc]
        if len(res) >= 1:
            self.user_history.update_one({'access_token': access_token}, {'$set': {'history': []}})

    def update_role(self, access_token, role):
        """更新用户的聊天历史"""
        mydoc = self.user_history.find({'access_token': access_token}).limit(1)
        res = [x for x in mydoc]
        if len(res) >= 1:
            self.user_history.update_one({'access_token': access_token}, {'$set': {'role': role}})
