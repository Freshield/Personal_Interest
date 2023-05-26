# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: MongdbClient.py
@Time: 2023-03-08 13:05
@Last_update: 2023-03-08 13:05
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
import datetime
from lib.logs import LOGGER


class MongodbClient(object):
    """Mongodb客户端"""
    def __init__(self):
        self.myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        self.mydb = self.myclient["lark_bot"]
        self.msg_id = self.mydb['msg_id']
        self.user_history = self.mydb['user_history']

    def check_msg_id_exist(self, msg_id):
        """检测msg_id是否存在"""
        mydoc = self.msg_id.find({'id': msg_id}).limit(1)
        res = [x for x in mydoc]

        return len(res) >= 1

    def insert_msg_id(self, msg_id):
        """插入msg_id"""
        mydict = {'id': msg_id, 'datetime': datetime.datetime.utcnow()}
        _ = self.msg_id.insert_one(mydict)

    def create_user(self, open_id, history=None, role=None, temperature=0.5):
        """创建用户"""
        role = '你是ChatGPT，OpenAI训练的大规模语言模型，简明的回答用户的问题。' if role is None else role
        history = history if history is not None else []
        self.user_history.insert_one({
            'open_id': open_id, 'history': history, 'role': role, 'temperature': temperature})

        return role, temperature, history

    def get_user_chat_history(self, open_id):
        """获取用户的聊天历史"""
        mydoc = self.user_history.find({'open_id': open_id}).limit(1)
        res = [x for x in mydoc]
        LOGGER.info(f'get user chat history {res}')
        # 如果已经创建则update
        if len(res) >= 1:
            history = res[0]['history']
            role = res[0]['role']
            temperature = res[0]['temperature']
        # 没有则创建
        else:
            role, temperature, history = self.create_user(open_id)

        return role, temperature, history

    def update_user_chat_history(self, open_id, qus, ans):
        """更新用户的聊天历史"""
        mydoc = self.user_history.find({'open_id': open_id}).limit(1)
        res = [x for x in mydoc]
        LOGGER.info(f'update user chat history {res}')
        # 如果有则创建
        if len(res) >= 1:
            self.user_history.update_one({'open_id': open_id}, {'$push': {'history': (qus, ans)}})
        # 没有则创建
        else:
            self.create_user(open_id, [(qus, ans)])

    def delete_user_chat_history(self, open_id, keep_num=9):
        """删除用户的聊天历史"""
        mydoc = self.user_history.find({'open_id': open_id}).limit(1)
        res = [x for x in mydoc]
        if len(res) >= keep_num:
            history_list = res[0]['history']
            self.user_history.update_one({
                'open_id': open_id}, {'$set': {'history': history_list[-keep_num:]}})

    def update_role(self, open_id, role):
        """更新用户的role"""
        mydoc = self.user_history.find({'open_id': open_id}).limit(1)
        res = [x for x in mydoc]
        if len(res) >= 1:
            self.user_history.update_one({'open_id': open_id}, {'$set': {'role': role}})
        else:
            self.create_user(open_id, role=role)

    def update_temperature(self, open_id, temperature):
        """更新用户的temperature"""
        mydoc = self.user_history.find({'open_id': open_id}).limit(1)
        res = [x for x in mydoc]
        if len(res) >= 1:
            self.user_history.update_one({'open_id': open_id}, {'$set': {'temperature': temperature}})
        else:
            self.create_user(open_id, temperature=temperature)

    def get_user_config(self, open_id):
        """获取用户的配置"""
        mydoc = self.user_history.find({'open_id': open_id}).limit(1)
        res = [x for x in mydoc]
        role = '你是ChatGPT，OpenAI训练的大规模语言模型，简明的回答用户的问题。'
        if len(res) >= 1:
            return res[0]['role'], res[0]['temperature']
        else:
            self.create_user(open_id)

        return role, 0.5


