# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: init_items_info.py
@Time: 2022-02-28 14:59
@Last_update: 2022-02-28 14:59
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
from lib.get_item_list import get_item_list
from lib.get_items_info import get_items_info


def init_items_info(browser, url):
    """初始化地板价和item信息"""
    # 初始化访问
    floor_price, item_list = get_items_info(browser, url)

    browser.execute_script('window.scrollTo(600,1200)')
    time.sleep(4)
    item_list += get_item_list(browser)

    browser.execute_script('window.scrollTo(1200,1800)')
    time.sleep(4)
    item_list += get_item_list(browser)

    item_dict = {key: True for key in item_list}

    return floor_price, item_dict
