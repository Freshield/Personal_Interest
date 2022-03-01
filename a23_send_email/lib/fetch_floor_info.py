# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: fetch_floor_price.py
@Time: 2022-03-01 13:31
@Last_update: 2022-03-01 13:31
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
import random
import logging
from config import mail_sender, mail_license, mail_receivers
from lib.get_items_info import get_items_info
from lib.send_email import send_email
from lib.get_html_mail_content import get_html_mail_content


def fetch_floor_info(browser, project_name, index, last_item_dict):
    """
    访问一次地板信息
    整体流程：
    1. 得到网页的信息
    2. 分析floor price
    3. 分析上架的item
    """
    # 1. 得到网页的信息
    url = f'https://opensea.io/collection/{project_name}?search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW'
    last_price = last_item_dict['last_price']
    floor_price, item_list = get_items_info(browser, url)
    if index % 50 == 0:
        logging.info(f'project {project_name}: floor price: {last_price}')

    # 2. 分析floor price
    # 如果不同则发邮件
    if floor_price != last_price:
        title = f'project {project_name}: floor price changed， {last_price} -> {floor_price}'
        send_text = get_html_mail_content(
            f'The project {project_name} has new floor price, check it', url)
        send_email(mail_sender, mail_license, mail_receivers, title, send_text)
        logging.info(title)
        # 更新
        last_item_dict['last_price'] = floor_price

    # 3. 分析上架的item
    # 判断是否有新的list
    new_item_list = []
    for item in item_list:
        if item not in last_item_dict:
            new_item_list.append(item)
    if len(new_item_list) != 0:
        title = f'project {project_name}: there have new list, {new_item_list}'
        send_text = get_html_mail_content(
            f'The project {project_name} has new list, {new_item_list}, check it', url)
        send_email(mail_sender, mail_license, mail_receivers, title, send_text)
        logging.info(title)
        # 更新
        last_item_dict.update({key: True for key in item_list})

    time.sleep(2 + 2 * random.random())

    return last_item_dict
