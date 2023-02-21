#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b2_file_logging.py
@Time: 2020-03-09 10:52
@Last_update: 2020-03-09 10:52
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


logging.basicConfig(filename='data/test.log', filemode='w', format='%(asctime)s %(name)s:%(levelname)s:%(message)s',
                    datefmt='%d-%M-%Y %H:%M:%S', level=logging.DEBUG)
logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')