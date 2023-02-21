# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: get_html_mail_content.py
@Time: 2022-02-28 17:24
@Last_update: 2022-02-28 17:24
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""


def get_html_mail_content(text, url=None):
    """得到html格式的话"""
    text = f'<p>{text}</p>'
    if url is not None:
        text += f'<p><a href="{url}">link here</a></p>'

    return text
