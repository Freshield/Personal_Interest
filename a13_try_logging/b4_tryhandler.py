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

logger = logging.getLogger()

handler1 = logging.StreamHandler()
handler2 = logging.FileHandler(filename='data/test.log', mode='w', encoding='utf-8')

logger.setLevel(logging.DEBUG)
handler1.setLevel(logging.WARNING)
handler2.setLevel(logging.DEBUG)

formater = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')
handler1.setFormatter(formater)
handler2.setFormatter(formater)

logger.addHandler(handler1)
logger.addHandler(handler2)

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')