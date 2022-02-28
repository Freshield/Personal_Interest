# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: get_item_list.py
@Time: 2022-02-28 14:58
@Last_update: 2022-02-28 14:58
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from bs4 import BeautifulSoup


def get_item_list(browser):
    """得到当前地板的信息列表"""
    html = browser.page_source
    soup = BeautifulSoup(html, features='lxml')
    text = soup.text
    title = soup.find('title').text.split('- Collection')[0].strip()
    text_lines = text.split(title)
    text_lines = [sub_line.split('\n')[0] for sub_line in text_lines if ('Price' in sub_line) and ('timelapse' in sub_line)]
    item_list = []
    for line in text_lines:
        id, price = line.split('Price')
        id = id.split(' ')[-1]
        price = price.split(' timelapse')[0]
        item_list.append(f'{id}_{price}')

    return item_list
