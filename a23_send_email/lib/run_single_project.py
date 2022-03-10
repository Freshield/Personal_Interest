# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: run_single_project.py
@Time: 2022-03-10 16:44
@Last_update: 2022-03-10 16:44
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
from config import threshold, cool_down_time, logging_info_time, mail_receivers, mail_sender, mail_license
from lib.set_chrome_options import set_chrome_options
from lib.init_items_info import init_items_info
from lib.fetch_floor_info import fetch_floor_info
from lib.send_email import send_email


def run_single_project(project_name, proxy=False, driver_path='./chromedriver'):
    """
    运行单一的项目
    1. 初始化
    2. 进行数据的获取
    """
    with webdriver.Chrome(driver_path, chrome_options=set_chrome_options(proxy)) as browser:
        browser.set_window_size(2500, 1200)
        # 1. 初始化
        last_item_dict = init_items_info(browser, project_name)
        logging.info(f'project {project_name}: Begin floor price: {last_item_dict["last_price"]}')

        begin_time = time.time()
        try:
            while True:
                # 项目获取信息
                # 2. 进行数据的获取
                last_item_dict = fetch_floor_info(
                    browser, project_name, last_item_dict, threshold, cool_down_time)
                # 如果大于打log的时间则显示
                if (time.time() - begin_time) >= logging_info_time:
                    logging.info(
                        f'project {project_name}: floor price: {last_item_dict["last_price"]}')
                    begin_time = time.time()
        except Exception as e:
            logging.info(traceback.format_exc())
            send_email(
                mail_sender, mail_license,
                'The program meet bug', traceback.format_exc(), [mail_receivers[0]])


if __name__ == '__main__':
    from lib.set_logger import set_logger
    set_logger()
    run_single_project('3landers', True, '../chromedriver')
