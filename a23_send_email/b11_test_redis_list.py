# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b11_test_redis_list.py
@Time: 2022-03-03 14:18
@Last_update: 2022-03-03 14:18
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import redis

# with redis.Redis(host='localhost', port=6379, decode_responses=True, db=8) as r:
#     print(r.llen('test'))
#     for i in range(r.llen('test')):
#         print(r.lpop('test'))

with redis.Redis(host='localhost', port=6379, decode_responses=True, db=8) as r:
    receivers = r.smembers('receivers_set')
    print(receivers)
    print(type(receivers))