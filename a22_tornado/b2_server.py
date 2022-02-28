# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b2_server.py
@Time: 2022-02-10 16:08
@Last_update: 2022-02-10 16:08
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

class IndexHandler(RequestHandler):
    def get(self):
        self.write('hello world')


if __name__ == '__main__':
    app = Application([(r'/', IndexHandler)])
    http_server = HTTPServer(app)

    http_server.bind(8888)
    http_server.start(0)

    IOLoop.current().start()
