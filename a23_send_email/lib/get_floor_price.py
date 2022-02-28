# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: get_floor_price.py
@Time: 2022-02-28 14:57
@Last_update: 2022-02-28 14:57
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
from lib.get_page_text import get_page_text


def get_floor_price(browser):
    """得到地板价格"""
    text = get_page_text(browser)
    # 尝试2次 如果都没有则退出
    if ('owners' not in text) or ('floor price' not in text):
        time.sleep(3)
        text = get_page_text(browser)
    if ('owners' not in text) or ('floor price' not in text):
        return None
    floor_price = float(text.split('owners')[-1].split('floor price')[0])

    return floor_price
