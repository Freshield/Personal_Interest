# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b1_link_web3.py
@Time: 2023-03-25 00:19
@Last_update: 2023-03-25 00:19
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
from web3 import Web3


if __name__ == '__main__':
    api_key = os.environ.get('INFURA_API_KEY')
    main_url = f'https://mainnet.infura.io/v3/{api_key}'
    test_url = f'https://goerli.infura.io/v3/{api_key}'

    w3 = Web3(Web3.HTTPProvider(main_url))
    print(w3.eth.get_block('latest'))


