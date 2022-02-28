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
import time
import random
import traceback
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import ChromeOptions
from config import mail_sender, mail_license, mail_receiver
from lib.init_items_info import init_items_info
from lib.get_items_info import get_items_info
from lib.send_email import send_email


if __name__ == '__main__':
    project_name = 'fishyfam'
    url = f'https://opensea.io/collection/{project_name}?search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW'

    # 设置options参数，以开发者模式运行
    option = ChromeOptions()
    # 解决报错，设置无界面运行
    option.add_argument('--no-sandbox')
    option.add_argument('--disable-dev-shm-usage')
    option.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    option.add_argument('--headless')
    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
    option.add_argument('user-agent={0}'.format(user_agent))

    # with webdriver.Chrome('./chromedriver', chrome_options=option) as browser:

    with webdriver.Remote(
            command_executor="http://127.0.0.1:4444/wd/hub",
            desired_capabilities=DesiredCapabilities.CHROME,
            options=option) as browser:

        browser.set_window_size(2500, 1200)

        print('Init the items info')
        last_price, last_item_dict = init_items_info(browser, url)
        print(f'project {project_name}: Begin floor price: {last_price}')
        try:
            while True:
                floor_price, item_list = get_items_info(browser, url)
                time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                print(f'{time_str}: project {project_name}: last {last_price}, now {floor_price}')
                # 如果小则发邮件
                if floor_price < last_price:
                    title = f'project {project_name}: floor price {last_price} -> {floor_price}'
                    send_text = f'The project {project_name} has new floor price, check it\n{url}'
                    send_email(mail_sender, mail_license, mail_receiver, title, send_text)
                    # 更新
                    last_price = floor_price

                # 判断是否有新的list
                new_item_list = []
                for item in item_list:
                    if item not in last_item_dict:
                        new_item_list.append(item)
                if len(new_item_list) != 0:
                    title = f'project {project_name}: there have new list, {new_item_list}'
                    send_text = f'The project {project_name} has new list, {new_item_list}, check it\n{url}'
                    send_email(mail_sender, mail_license, mail_receiver, title, send_text)
                    # 更新
                    last_item_dict.update({key: True for key in item_list})

                time.sleep(2 + 2*random.random())
        except Exception as e:
            print(traceback.format_exc())
        finally:
            browser.close()
