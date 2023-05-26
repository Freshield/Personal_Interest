# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: get_driver_img_url.py
@Time: 2023-01-26 18:15
@Last_update: 2023-01-26 18:15
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


def get_driver_img_url(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')
    thumb_list = soup.find_all('img', class_='zoom-thumb')
    driver_img_url_list = []
    for thumb in thumb_list:
        url = thumb.attrs['src'].lower()
        driver_img_url_list.append(url)

    return driver_img_url_list
