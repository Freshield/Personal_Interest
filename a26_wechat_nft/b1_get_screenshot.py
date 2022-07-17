# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b1_get_screenshot.py
@Time: 2022-06-07 17:51
@Last_update: 2022-06-07 17:51
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import os.path
import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


url = 'https://mirror.xyz/freshield.eth/R0M1Aa-E5bJ3Y4KATgF8L9Kg3D1p_e7Zoy-llpYQ1OI'
chrome_options = Options()
# 启动无头模式，实际上是用命令行来对Google浏览器进行限制
chrome_options.add_argument('--headless')
# chrome_options.add_argument('--proxy-server=http://127.0.0.1:7890')

driver = Chrome(os.path.abspath('./chromedriver'), options=chrome_options)
driver.set_window_size(1200, 1800)

driver.get(url)
time.sleep(2)
driver.save_screenshot('data/test.png')
driver.close()
