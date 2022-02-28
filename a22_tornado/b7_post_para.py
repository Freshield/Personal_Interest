# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b7_post_para.py
@Time: 2022-02-11 17:00
@Last_update: 2022-02-11 17:00
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from tornado.options import options, define

define('port', default=8000, type=int)


class IndexHandler(RequestHandler):
    def get(self):
        user = self.get_argument('user')
        print(f'get the {user}')

    def post(self):
        user = self.get_argument('user')
        print(f'post the {user}')


if __name__ == '__main__':
    app = Application([(r'/', IndexHandler)])
    app.listen(8000)
    IOLoop.current().start()
