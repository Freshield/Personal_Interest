# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b1_head_first.py
@Time: 2022-02-10 15:29
@Last_update: 2022-02-10 15:29
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import tornado.web
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    """处理get请求"""
    def get(self):
        self.write('hello world')


if __name__ == '__main__':
    app = tornado.web.Application([(r'/', IndexHandler)])
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
