# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b1_foobar.py
@Time: 2021-07-02 18:07
@Last_update: 2021-07-02 18:07
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b"Hello World"]
