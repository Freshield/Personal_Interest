# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b3_transfer_all_test_eth.py
@Time: 2023-03-25 20:19
@Last_update: 2023-03-25 20:19
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
import pandas as pd
from web3 import Web3, HTTPProvider
from concurrent.futures import ThreadPoolExecutor

from config import TEST_URL
from lib.logs import LOGGER
from lib.EthAccount import EthAccount


if __name__ == '__main__':
    w3 = Web3(HTTPProvider(TEST_URL))
    # 获取所有要转的地址
    file_path = 'data/secret_data/racknerd.xlsx'
    data_dict_list = pd.read_excel(file_path).to_dict('records')
    to_transfer_address_list = [data_dict['address'] for data_dict in data_dict_list]
    # 多线程获取地址的余额，保证是0
    with ThreadPoolExecutor(max_workers=20) as executor:
        res_list = executor.map(lambda address: (address, w3.eth.get_balance(address)), to_transfer_address_list)
    for addr, balance in list(res_list):
        if balance != 0:
            LOGGER.warn(addr, balance)
            LOGGER.info(list(res_list))
            exit()
    # 获取所有的私钥地址
    file_path = 'data/secret_data/private_key_info.txt'
    with open(file_path, 'r') as f:
        info_list = f.readlines()
    private_key_list = [info.strip().split('\t')[2] for info in info_list]
    private_account_list = [EthAccount(private_key, w3) for private_key in private_key_list]
    # 保证所有地址都有余额
    with ThreadPoolExecutor(max_workers=20) as executor:
        res_list = executor.map(lambda account: (account.acc.address, account.get_balance()), private_account_list)
    for private_key, balance in list(res_list):
        print(private_key, balance)
        if balance < 0.9:
            LOGGER.warn(private_key, balance)
            LOGGER.info(list(res_list))
            exit()
    # 保证长度一致
    assert len(to_transfer_address_list) == len(private_account_list), '长度不一致'

    # 开始转账
    index = 1
    for to_address, account in zip(to_transfer_address_list, private_account_list):
        tx = account.send_all_value(to_address)
        LOGGER.info(f'index {index} {account.acc.address} send all value to {to_address}, tx {tx}')
        time.sleep(int(60 * (4 + 2 * random.random())))
        index += 1



