# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: set_chrome_options.py
@Time: 2022-03-01 13:44
@Last_update: 2022-03-01 13:44
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from selenium.webdriver import ChromeOptions


def set_chrome_options():
    """设置chrome的参数"""
    # 设置options参数，以开发者模式运行
    option = ChromeOptions()
    # 解决报错，设置无界面运行
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-dev-shm-usage')
    option.add_argument("--disable-setuid-sandbox")
    option.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    option.add_argument('--headless')
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    option.add_argument('user-agent={0}'.format(user_agent))

    return option
