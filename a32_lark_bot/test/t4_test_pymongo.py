# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: t4_test_pymongo.py
@Time: 2023-03-08 12:45
@Last_update: 2023-03-08 12:45
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import time
import random
import pymongo
import datetime
from hashlib import sha256


if __name__ == '__main__':
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["lark_bot"]
    mycol = mydb['msg_id']

    mydict = {'id': '2', 'datetime': datetime.datetime.utcnow()}
    x = mycol.insert_one(mydict)
    print(x.inserted_id)
    mydoc = mycol.find({'id': '2'}).limit(1)
    res = [x for x in mydoc]
    print(res)
    print(len(res))
    res = res[0]
    time.sleep(61)
    mydoc = mycol.find({'id': '2'}).limit(1)
    res = [x for x in mydoc]
    print(res)
    print(len(res))
    res = res[0]
