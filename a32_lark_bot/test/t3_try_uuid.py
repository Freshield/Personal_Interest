# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: t3_try_uuid.py
@Time: 2023-03-08 10:32
@Last_update: 2023-03-08 10:32
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import uuid


if __name__ == '__main__':
    uuid = str(uuid.uuid1())
    print(uuid)
    print(type(uuid))
    text = '@123_123 123 123123234_sadf wer '
    text = ' '.join(text.split(' ')[1:]).strip()
    print(text)

