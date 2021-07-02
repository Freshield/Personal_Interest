# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b2_myflaskapp.py
@Time: 2021-07-02 19:07
@Last_update: 2021-07-02 19:07
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<span style='color:red'>I am app 1</span>"


if __name__ == '__main__':
    port = 9999
    app.run(host="0.0.0.0", port=port, threaded=True)
