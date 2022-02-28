# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b3_options.py
@Time: 2022-02-10 16:16
@Last_update: 2022-02-10 16:16
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from tornado.web import RequestHandler, Application
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
import tornado.options

tornado.options.define('port', default=8000, type=int, help='this is the port for application')

class IndexHandler(RequestHandler):
    def get(self):
        self.write('options')


if __name__ == '__main__':
    app = Application([(r'/', IndexHandler)])
    tornado.options.parse_command_line()

    http_server = HTTPServer(app)
    http_server.bind(tornado.options.options.port)
    http_server.start(1)

    IOLoop.current().start()
