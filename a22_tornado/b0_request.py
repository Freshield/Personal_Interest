# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b0_request.py
@Time: 2022-02-11 17:07
@Last_update: 2022-02-11 17:07
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import requests


if __name__ == '__main__':

    requests.post('http://127.0.0.1:8000', data={'user': 'admin'})
