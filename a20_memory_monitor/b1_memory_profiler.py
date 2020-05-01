# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b1_memory_profiler.py
@Time: 2020-05-11 21:22
@Last_update: 2020-05-11 21:22
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import numpy as np
from memory_profiler import profile

@profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    x = np.array(range(10 ** 7))
    y = np.array(np.random.uniform(0, 100, size=(10 ** 8)))
    return a

for i in range(20):
    my_func()