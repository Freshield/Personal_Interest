# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: test.py
@Time: 2022-02-28 13:30
@Last_update: 2022-02-28 13:30
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
with open('./test.txt', 'r') as f:
    text = f.read()
print(text)
print('\n'.join(text.split('FishyFam')))
