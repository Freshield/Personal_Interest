# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b5_reverse.py
@Time: 2022-02-10 16:35
@Last_update: 2022-02-10 16:35
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from tornado.web import Application, RequestHandler, url
from tornado.ioloop import IOLoop
from tornado.httpserver import HTTPServer
from tornado.options import options, define

define('port', default=8000, type=int)


class IndexHandler(RequestHandler):
    def get(self):
        self.write(f"<a href='{self.reverse_url('login')}'>用户登录</a>")


class RegistHandler(RequestHandler):
    def initialize(self, title):
        self.title = title

    def get(self):
        self.write(f'register {self.title}')


class LoginHandler(RequestHandler):
    def get(self):
        self.write('login show')

    def post(self):
        self.write('login process')


if __name__ == '__main__':
    app = Application([
        (r'/', IndexHandler),
        (r'/regist', RegistHandler, {'title': 'rigister'}),
        url(r'/login', LoginHandler, name='login')
    ])

    http_server = HTTPServer(app)
    http_server.listen(8000)

    IOLoop.current().start()



