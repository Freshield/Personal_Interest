#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b4_tryhandler.py
@Time: 2019-10-27 11:01
@Last_update: 2019-10-27 11:01
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import logging
import logging.handlers
from queue import Queue

logger = logging.getLogger()

test = Queue(1000)

handler1 = logging.StreamHandler()
handler2 = logging.FileHandler(filename='data/test.log', mode='w', encoding='utf-8',)
handler3 = logging.handlers.QueueHandler(test)

logger.setLevel(logging.DEBUG)
handler1.setLevel(logging.WARNING)
handler2.setLevel(logging.DEBUG)
handler3.setLevel(logging.DEBUG)

formater = logging.Formatter('{asctime}-{filename}-{funcName}-{lineno}-{levelname}-{message}', style='{')
handler1.setFormatter(formater)
handler2.setFormatter(formater)
handler3.setFormatter(formater)

logger.addHandler(handler1)
logger.addHandler(handler2)
logger.addHandler(handler3)

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')

a = 1
b = 0

try:
    c = a / b
except Exception as e:
    a = logging.exception('exception')
    print(a)

print(test.qsize())
last = test.get()
print(last.name)
print(last.asctime)
print(test.qsize())
print(formater.format(last))