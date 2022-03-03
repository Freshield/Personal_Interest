# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b2_analyse_opensea.py
@Time: 2022-02-28 11:56
@Last_update: 2022-02-28 11:56
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import redis
import logging
import traceback
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from lib.init_items_info import init_items_info
from lib.set_logger import set_logger
from lib.fetch_floor_info import fetch_floor_info
from lib.set_chrome_options import set_chrome_options
from lib.send_email import send_email
from config import mail_sender, mail_license, mail_receivers, project_names, threshold,cool_down_time


if __name__ == '__main__':
    set_logger()
    pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True, db=8)
    with redis.Redis(connection_pool=pool) as r:
        for receiver in mail_receivers:
            r.sadd('receivers_set', receiver)
    logging.info('begin the bot')

    with webdriver.Chrome('./chromedriver', chrome_options=set_chrome_options()) as browser:
    # with webdriver.Remote(
    #         command_executor="http://127.0.0.1:4444/wd/hub",
    #         desired_capabilities=DesiredCapabilities.CHROME,
    #         options=option) as browser:
        browser.set_window_size(2500, 1200)

        logging.info('Init the items info')
        project_info_dicts = dict()
        for project_name in project_names:
            last_item_dict = init_items_info(browser, project_name)
            logging.info(f'project {project_name}: Begin floor price: {last_item_dict["last_price"]}')
            project_info_dicts[project_name] = last_item_dict

        index = 0
        try:
            while True:
                index += 1
                # 遍历项目获取信息
                for project_name, last_item_dict in project_info_dicts.items():
                    last_item_dict = fetch_floor_info(
                        browser, project_name, index, last_item_dict, threshold, cool_down_time)
                    project_info_dicts[project_name] = last_item_dict
                if index % 39 == 0:
                    index = 0
        except Exception as e:
            logging.info(traceback.format_exc())
            send_email(
                mail_sender, mail_license,
                'The program meet bug', traceback.format_exc(), ['yangyufresh@163.com'])
        finally:
            browser.quit()
