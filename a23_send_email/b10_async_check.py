# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b10_async_check.py
@Time: 2022-03-03 13:50
@Last_update: 2022-03-03 13:50
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
from config import mail_sender, mail_license, mail_receivers
from discord.ext import tasks
import discord
import time


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # an attribute we can access from our task
        self.index = 0

        self.project_names = ['azuki', 'doodles-official']
        self.threshold = 0.05

        set_logger()
        self.pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True, db=8)
        with redis.Redis(connection_pool=self.pool) as r:
            r.set('exit', 'False')
            for receiver in mail_receivers:
                r.sadd('receivers_set', receiver)
        logging.info('begin the bot')

        self.browser = webdriver.Chrome('./chromedriver', chrome_options=set_chrome_options())


        # start the task to run in the background
        self.my_background_task.start()

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def test(self):
        with self.browser as browser:
            browser.set_window_size(2500, 1200)

            logging.info('Init the items info')
            project_info_dicts = dict()
            for project_name in self.project_names:
                last_item_dict = init_items_info(browser, project_name)
                logging.info(f'project {project_name}: Begin floor price: {last_item_dict["last_price"]}')
                project_info_dicts[project_name] = last_item_dict

            try:
                self.index += 1
                # 检查是否要退出
                with redis.Redis(connection_pool=self.pool) as r:
                    exit = r.get('exit')
                    if exit == 'True':
                        raise ValueError('Time to exit')
                # 遍历项目获取信息
                for project_name, last_item_dict in project_info_dicts.items():
                    last_item_dict = fetch_floor_info(
                        browser, project_name, self.index, last_item_dict, self.threshold)
                    project_info_dicts[project_name] = last_item_dict
                if self.index % 39 == 0:
                    self.index = 0
            except Exception as e:
                logging.info(traceback.format_exc())
                send_email(
                    mail_sender, mail_license, ['yangyufresh@163.com'],
                    'The program meet bug', traceback.format_exc())
            finally:
                browser.quit()

    @tasks.loop(seconds=10) # task runs every 60 seconds
    async def my_background_task(self):
        print(time.strftime('%Y%m%d%H%M', time.localtime(time.time())))
        channel = self.get_channel(948784040746549278) # channel ID goes here
        await self.test()
        await channel.send(self.index)


    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready() # wait until the bot logs in

client = MyClient()
client.run('')