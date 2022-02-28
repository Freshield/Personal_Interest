# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b4_application.py
@Time: 2022-02-10 16:24
@Last_update: 2022-02-10 16:24
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
from tornado.options import define, options

define('port', default=8000, type=int)

class IndexHandler(RequestHandler):
    def get(self):
        self.write('the index')

class ArticleHandler(RequestHandler):
    def initialize(self, title):
        print('initialize')
        self.title = title

    def get(self):
        self.write(f'you are looking for, {self.title}')


if __name__ == '__main__':
    options.parse_command_line()

    app = Application([
        (r'/', IndexHandler), (r'/article', ArticleHandler, {'title': 'the article'})], debug=True)

    http_server = HTTPServer(app)
    http_server.bind(options.port)
    http_server.start(1)

    IOLoop.current().start()


