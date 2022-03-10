# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b13_test_multi_process.py
@Time: 2022-03-10 15:23
@Last_update: 2022-03-10 15:23
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import time
from concurrent.futures import ProcessPoolExecutor


def test(num):
    print(f'here, {num}')
    time.sleep(num)
    print(f'done, {num}')
    return num


if __name__ == '__main__':
    with ProcessPoolExecutor(4) as executor:
        rst = executor.map(test, [1,2,3,4])

    rst = list(rst)

    print(rst)
