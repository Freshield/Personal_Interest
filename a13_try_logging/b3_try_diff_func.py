#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b3_try_diff_func.py
@Time: 2020-03-09 10:56
@Last_update: 2020-03-09 10:56
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
from func_a import func_a
from func_b import func_b


logging.basicConfig(filename='data/test.log', filemode='w', format='%(asctime)s %(name)s:%(levelname)s:%(message)s',
                    datefmt='%d-%M-%Y %H:%M:%S', level=logging.DEBUG)

func_a()
func_b()