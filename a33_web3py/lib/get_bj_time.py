# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: get_bj_time.py
@Time: 2023-03-28 21:55
@Last_update: 2023-03-28 21:55
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from datetime import datetime
from datetime import timedelta
from datetime import timezone


SHA_TZ = timezone(
    timedelta(hours=8),
    name='Asia/Shanghai',
)


def get_bj_time():
    # 协调世界时
    utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
    # 北京时间
    beijing_now = utc_now.astimezone(SHA_TZ)

    return beijing_now
