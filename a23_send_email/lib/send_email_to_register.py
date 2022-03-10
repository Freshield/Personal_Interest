# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: send_email_to_register.py
@Time: 2022-03-10 22:22
@Last_update: 2022-03-10 22:22
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from lib.send_email import send_email
from lib.get_html_mail_content import get_html_mail_content
from config import mail_register_dict, mail_sender, mail_license


def send_email_to_register(info_dict):
    """把邮件传到相应已经注册的用户手中"""
    # 生成相应的信息
    project_name = info_dict['project_name']
    info_type = info_dict['type']
    url = f'https://opensea.io/collection/{project_name}?search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW'
    if info_type == 'price':
        last_price = info_dict['last_price']
        new_price = info_dict['new_price']
        title = f'project {project_name}: floor price changed， {last_price} -> {new_price}'
        send_text = get_html_mail_content(
            f'The project {project_name} has new floor price, check it， {last_price} -> {new_price}', url)
    else:
        item_list = info_dict['item_list']
        title = f'project {project_name}: there have new list, {item_list}'
        send_text = get_html_mail_content(
            f'The project {project_name} has new list, {item_list}, check it', url)

    # 发送到相应的注册者手中
    for receiver_address, project_names in mail_register_dict.items():
        if project_name in project_names:
            send_email(mail_sender, mail_license, title, send_text, receiver_address)
