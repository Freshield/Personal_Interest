# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b5_try_pymongo.py
@Time: 2023-03-03 19:59
@Last_update: 2023-03-03 19:59
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import random
import pymongo
from hashlib import sha256


if __name__ == '__main__':
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["openai_bot"]
    mycol = mydb['user_info']


    username_list = ['ada']

    for username in username_list:
        password = ''.join([str(random.randint(0, 9)) for _ in range(8)])
        print(f'{username} {password}')
    exit()

    user_pass_str = 'ranran 30067983\nxixi 63598444\nheihei 60248174\nada 07515389'
    user_pass_list = user_pass_str.split('\n')
    for user_pass in user_pass_list:
        username, password = user_pass.split(' ')
        print(f'{username} {password}')
        username = sha256(username.encode('utf8')).hexdigest()
        password = sha256(password.encode('utf8')).hexdigest()
        mydict = {'username': username, 'password': password}
        x = mycol.insert_one(mydict)
        print(x.inserted_id)
    exit()

    # mydoc = mycol.find({'username': username, 'password': password}).limit(1)
    # res = [x for x in mydoc]
    # print(res)
    # print(len(res))

    username = 'freshield'
    mycol = mydb['user_history']
    mydict = {'username': username, 'access-token': '', 'history': [('a', 'b'), ('c', 'd')]}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)
    mydoc = mycol.find({'username': username}).limit(1)
    res = [x for x in mydoc]
    print(res)
    print(len(res))
    res = res[0]
    # res['history'].append('d')
    # mycol.update_one({'username': username}, {'$set': {'history': res['history']}})
    mycol.update_one({'username': username}, {'$push': {'history': ('e', 'f')}})
    mydoc = mycol.find({'username': username}).limit(1)
    res = [x for x in mydoc]
    print(res)
    print(len(res))
