# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: get_chain_gas.py
@Time: 2023-04-10 20:28
@Last_update: 2023-04-10 20:28
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
import json
import requests
from config import OWLRACLE_PATH

with open('data/secret_data/owlracle_keys.json', 'r') as f:
    _owlracle_keys = json.load(f)


def get_chain_gas(chain):
    """获取链的gas"""
    sub_dict = _owlracle_keys[chain]
    res = requests.get(f'https://api.owlracle.info/v4/{chain}/gas?apikey={sub_dict["api_key"]}').json()
    print(res)
    gas, fee = res['speeds'][1][sub_dict['gas_key']], res['speeds'][1][sub_dict['fee_key']]

    return gas, fee
