# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: config.py
@Time: 2023-03-25 18:58
@Last_update: 2023-03-25 18:58
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

# 初始化最初的服务
VERSION = '0.0.1'

PORT_NUM = 9888
VERIFY_CODE = '!GetGasInfoHere@'
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
API_KEY = os.environ.get('INFURA_API_KEY')
MAIL_PASS = os.getenv('MAIL_PASS')
MAIN_URL = f'https://mainnet.infura.io/v3/{API_KEY}'
TEST_URL = f'https://goerli.infura.io/v3/{API_KEY}'

############### gas related ###############
OWLRACLE_PATH = os.path.join(BASE_DIR, 'data/secret_data/owlracle_keys.json')
CHAIN_NAMES = ('eth', 'goerli', 'opt', 'arb', 'poly', 'avax', 'ftm')

############### Number of log files ###############
LOGS_DIR_PATH = os.path.join(BASE_DIR, 'log_files')
LOGS_STREAM_LEVEL = logging.INFO
LOGS_FILE_LEVEL = logging.INFO
LOGS_NUM = os.getenv("logs_num", 0)

os.makedirs(BASE_DIR, exist_ok=True)
os.makedirs(LOGS_DIR_PATH, exist_ok=True)