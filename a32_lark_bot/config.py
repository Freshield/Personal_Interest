# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: config.py
@Time: 2023-03-07 21:28
@Last_update: 2023-03-07 21:28
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""

import os
import logging

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(ROOT_DIR, 'data')


############### Config Info ###############
config_info_text = '/h or /config: 查看当前配置信息\n' \
                   '/update_role: 更新角色信息，在/update_role之后加上你想设定的role信息\n' \
                   '/update_temperature: 更新温度信息，在/update_temperature之后加上你想设定的temperature，' \
                   '这是一个介于0到1的值，约接近1回答越发散，越接近0越稳定\n'

############### Number of log files ###############
LOGS_DIR_NAME = 'log_files'
LOGS_STREAM_LEVEL = logging.DEBUG
LOGS_FILE_LEVEL = logging.INFO
LOGS_NUM = os.getenv("logs_num", 0)
