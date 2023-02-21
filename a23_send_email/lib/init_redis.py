# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: set_redis.py
@Time: 2022-03-10 17:28
@Last_update: 2022-03-10 17:28
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
from config import mail_receivers, mail_register_dict, channel_id_dict, channel_register_dict


def init_redis():
    """
    初始化redis
    :return:
    """
    pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True, db=8)
    with redis.Redis(connection_pool=pool) as r:
        # 删除相关信息
        for receiver in r.smembers('receivers_set'):
            r.srem('receivers_set', receiver)
        for channel_id in r.smembers('channels_set'):
            print(channel_id)
            r.srem('channels_set', channel_id)
        # 增加信息
        for receiver in mail_receivers:
            r.sadd('receivers_set', receiver)
        for _, channel_id in channel_id_dict.items():
            r.sadd('channels_set', channel_id)


if __name__ == '__main__':
    init_redis()
