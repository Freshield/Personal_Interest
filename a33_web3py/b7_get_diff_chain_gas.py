# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b7_get_diff_chain_gas.py
@Time: 2023-04-08 21:01
@Last_update: 2023-04-08 21:01
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import json
import requests


import time
from web3 import Web3, HTTPProvider
from config import MAIN_URL
from lib.get_chain_gas import get_chain_gas


if __name__ == '__main__':
    with open('data/secret_data/owlracle_keys.json', 'r') as f:
        owlracle_keys = json.load(f)
    main_w3 = Web3(HTTPProvider(MAIN_URL))
    main_gas = main_w3.from_wei(main_w3.eth.gas_price, 'gwei')
    print(main_gas)

    for chain in owlracle_keys:
        gas, fee = get_chain_gas(chain)
        print(f'{chain} gas: {gas}, fee: {fee}')
        print()
