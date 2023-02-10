# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: t2_try_bs4.py
@Time: 2023-01-25 22:10
@Last_update: 2023-01-25 22:10
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import json
from bs4 import BeautifulSoup


if __name__ == '__main__':
    elements_path = '../data/elements.txt'
    with open(elements_path, 'r') as f:
        text_str = f.read()
    elements_list = []
    for line in text_str.split('\n'):
        if '<img' in line:
            elements_list.append(line)

    url_list = []
    for line in elements_list:
        soup = BeautifulSoup(line, 'html.parser')

        src = soup.find('img').attrs['src'].lower()
        url_list.append(src)

    with open('../data/url_list.json', 'w') as f:
        f.write(json.dumps(url_list, indent=4))
