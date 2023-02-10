# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: get_driver_url_list.py
@Time: 2023-01-26 18:05
@Last_update: 2023-01-26 18:05
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


def get_driver_url_list(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')
    td_list = soup.find_all('td', class_='thumbnail')
    driver_url_list = []
    for td in td_list:
        driver_url = td.find('a').attrs['href'].lower()
        driver_url_list.append(driver_url)

    return driver_url_list
