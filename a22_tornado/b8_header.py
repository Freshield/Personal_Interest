# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b8_header.py
@Time: 2022-02-11 17:15
@Last_update: 2022-02-11 17:15
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
    def set_default_headers(self) -> None:
        print('set header')
        self.set_header('Content-type', 'application/json: charset=utf-8')
        self.set_header('js', 'zj')

    def get(self):
        print('get')
        self.write("{'jianshu':'zhiji'}")
        self.set_header('jianshu', 'zhijiheader')


if __name__ == '__main__':
    app = Application([(r'/', IndexHandler)])

    app.listen(8000)

    IOLoop.current().start()
