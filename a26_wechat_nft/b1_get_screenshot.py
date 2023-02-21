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


url = 'https://freshield.medium.com/00049-20221111-83a8a64eab10'
chrome_options = Options()
# 启动无头模式，实际上是用命令行来对Google浏览器进行限制
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--proxy-server=http://127.0.0.1:7890')
# chrome_options.binary_location = '/Users/yang.yu/Downloads/Google Chrome.app/Contents/MacOS/Google Chrome'

driver = Chrome(os.path.abspath('./chromedriver'), options=chrome_options)
driver.set_window_size(2200, 3500)

driver.get(url)
time.sleep(4)
driver.save_screenshot('data/test.png')
driver.close()
