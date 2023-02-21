# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b14_delete_inter_info.py
@Time: 2022-03-10 18:36
@Last_update: 2022-03-10 18:36
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

if __name__ == '__main__':
    # 删除中间存储的info信息
    with redis.Redis(host='localhost', port=6379, decode_responses=True, db=8) as r:
        for i in range(r.llen('new_info')):
            print(r.lpop('new_info'))
