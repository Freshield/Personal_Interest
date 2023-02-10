# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: t1_get_contry_code.py
@Time: 2023-01-25 21:47
@Last_update: 2023-01-25 21:47
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import json


if __name__ == '__main__':
    with open('../data/contry_code.txt', 'r') as f:
        text_list = f.read().strip().split('\n')

    code_list = []
    for text in text_list:
        code = text.split('value="')[-1].split('">')[0]
        code_list.append(code)

    print(json.dumps(code_list, indent=4))
    with open('../data/contry_code.json', 'w') as f:
        f.write(json.dumps(code_list, indent=4))
