# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: get_page_text.py
@Time: 2022-02-28 15:02
@Last_update: 2022-02-28 15:02
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


def get_page_text(browser):
    """得到页面的字符串"""
    html = browser.page_source
    soup = BeautifulSoup(html, features='lxml')
    text = soup.text

    return text
