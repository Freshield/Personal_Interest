# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b2_test_account.py
@Time: 2023-03-25 00:39
@Last_update: 2023-03-25 00:39
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
import statistics
from eth_account import Account
from eth_account.signers.local import LocalAccount
import web3
from web3 import Web3, HTTPProvider
from web3.middleware import construct_sign_and_send_raw_middleware

if __name__ == '__main__':
    api_key = os.environ.get('INFURA_API_KEY')
    main_url = f'https://mainnet.infura.io/v3/{api_key}'
    test_url = f'https://goerli.infura.io/v3/{api_key}'
    w3 = Web3(Web3.HTTPProvider(test_url))

    with open('data/secret_data/used_test_file.txt', 'r') as f:
        info_list = f.readlines()
    private_key = info_list[0].strip().split('----')[1]
    print(info_list[0])

    assert private_key.startswith("0x"), "Private key must start with 0x hex prefix"

    account: LocalAccount = Account.from_key(private_key)
    w3.middleware_onion.add(construct_sign_and_send_raw_middleware(account))

    print(f"Your hot wallet address is {account.address}")
    balance_in_wei = w3.eth.get_balance(account.address)
    balance_in_eth = w3.from_wei(balance_in_wei, 'ether')

    print(f"账户 {account.address} 的余额为 {balance_in_eth} ETH")

    print(f'raw {w3.eth.gas_price}')

    print(w3.eth.estimate_gas({
        'to': account.address, 'from': account.address, 'value': 0}))

    res = w3.eth.send_transaction({
        'to': account.address,
        'from': account.address,
        'value': w3.to_wei(1, 'ether'),
    })
    print(res.hex())
