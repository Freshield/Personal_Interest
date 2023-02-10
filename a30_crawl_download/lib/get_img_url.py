# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: get_img_url.py
@Time: 2023-01-26 17:05
@Last_update: 2023-01-26 17:05
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


def get_img_url(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')
    rst_list = []
    img_list = soup.find_all('img', id='MainImage')
    for img in img_list:
        src = img.attrs['src'].lower()
        rst_list.append(src)
    img_list = soup.find_all('img', id='BackImage')
    for img in img_list:
        src = img.attrs['src'].lower()
        rst_list.append(src)

    return rst_list
