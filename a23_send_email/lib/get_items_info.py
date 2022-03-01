# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: get_items_info.py
@Time: 2022-02-28 15:07
@Last_update: 2022-02-28 15:07
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
from lib.get_floor_price import get_floor_price
from lib.get_item_list import get_item_list


def get_items_info(browser, url):
    """得到地板价和item信息"""
    # 初始化访问
    browser.get(url)
    time.sleep(3)
    browser.execute_script('window.scrollTo(0,600)')
    time.sleep(3)

    floor_price = get_floor_price(browser)
    item_list = get_item_list(browser)

    return floor_price, item_list
