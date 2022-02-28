# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b6_para.py
@Time: 2022-02-11 16:53
@Last_update: 2022-02-11 16:53
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
from tornado.httpserver import HTTPServer
from tornado.options import options, define

define('port', default=8000, type=int)


class IndexHandler(RequestHandler):
    def get(self):
        username = self.get_query_argument('username')
        usernames = self.get_query_arguments('username')

        print(username)
        print(usernames)


if __name__ == '__main__':
    app = Application([(r'/', IndexHandler)])

    app.listen(8000)

    IOLoop.current().start()
