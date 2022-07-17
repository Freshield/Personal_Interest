# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b15_test_get_opensea_twitter.py
@Time: 2022-06-13 21:03
@Last_update: 2022-06-13 21:03
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
import logging
import traceback
from selenium import webdriver
from lib.set_chrome_options import set_chrome_options


def get_opensea_twitter(times, index=0, proxy=True, driver_path='./chromedriver'):
    """
    运行单一的项目
    1. 初始化
    2. 进行数据的获取
    """
    time.sleep(index)
    chrome_options = set_chrome_options(proxy)
    browser = webdriver.Chrome(driver_path, options=chrome_options)
    # 1. 初始化
    url = 'https://opensea.io/0xdecade69'

    try:
        for i in range(times):
            browser.get(url)
            time.sleep(4)
            page_source = browser.page_source
            while 'DDoS protection by' in browser.page_source:
                print('meet cloudflare')
                print('reset driver')
                # handle = browser.window_handles[-1]
                # time.sleep(1)
                # browser.service.stop()
                # time.sleep(6)
                # browser = webdriver.Chrome(driver_path, options=chrome_options)
                # time.sleep(1)
                # browser.switch_to.window(handle)
                time.sleep(6)

            if 'href="https://twitter.com/' in browser.page_source:
                logging.info(f'has twitter')
                print('has twitter')
            else:
                logging.info(f'not has twitter')
                print('not has twitter')
    except Exception as e:
        logging.info(traceback.format_exc())


if __name__ == '__main__':
    from lib.set_logger import set_logger
    set_logger()
    from concurrent.futures import ProcessPoolExecutor
    with ProcessPoolExecutor(max_workers=5) as executor:
        executor.map(get_opensea_twitter, [10] * 5, range(5))
