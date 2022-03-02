# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b6_test_redis.py
@Time: 2022-03-01 12:31
@Last_update: 2022-03-01 12:31
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import redis    # 导入redis 模块

# pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True, db=8)
# with redis.Redis(connection_pool=pool) as r:
with redis.Redis(host='localhost', port=6379, decode_responses=True, db=8) as r:
    r.set('exit', 0)  # 设置 name 对应的值
    print(r.get('exit'))  # 取出键 name 对应的值
    print('here')
    r.sadd('receivers_set', 'yangyufresh@163.com')
    print(r.smembers('receivers_set'))
    r.sadd('receivers_set', 'test@163.com')
    test = r.smembers('receivers_set')
    print(''.join([f"<{item}>" for item in test]))
    print(r.smembers('receivers_set'))
    r.srem('receivers_set', 'test@163.com')
    print(type(test))
