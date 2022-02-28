# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b3_check_list_items.py
@Time: 2022-02-28 14:03
@Last_update: 2022-02-28 14:03
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def get_item_list(text, title):
    """得到当前地板的信息列表"""
    text_lines = text.split(title)
    text_lines = [sub_line.split('\n')[0] for sub_line in text_lines if ('Price' in sub_line) and ('timelapse' in sub_line)]
    items_list = []
    for line in text_lines:
        id, price = line.split('Price')
        id = id.split(' ')[-1]
        price = price.split(' timelapse')[0]
        items_list.append(f'{id}_{price}')

    return items_list


if __name__ == '__main__':
    import random
    for i in range(30):
        print(2 + 2*random.random())

    a = {key: True for key in range(10)}
    print(a)
    a.update({key: True for key in range(20)})
    print(a)
