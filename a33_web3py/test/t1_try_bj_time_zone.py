# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: t1_try_bj_time_zone.py
@Time: 2023-03-28 21:54
@Last_update: 2023-03-28 21:54
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

# 协调世界时
utc_now = datetime.utcnow().replace(tzinfo=timezone.utc)
print("UTC:")
print(utc_now, utc_now.time())
print(utc_now.date(), utc_now.tzname())

# 北京时间
beijing_now = utc_now.astimezone(SHA_TZ)
print("Beijing:")
print(beijing_now.strftime('%H_%M_%S'))
print(beijing_now, beijing_now.time())
print(beijing_now.date(), beijing_now.tzname())

# 系统默认时区
local_now = utc_now.astimezone()
print("Default:")
print(local_now, local_now.time())
print(local_now.date(), local_now.tzname())