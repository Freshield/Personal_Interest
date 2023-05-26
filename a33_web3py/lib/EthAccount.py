# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: Account.py
@Time: 2023-03-25 18:52
@Last_update: 2023-03-25 18:52
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from eth_account import Account
from eth_account.signers.local import LocalAccount
from web3 import Web3, HTTPProvider
from web3.middleware import construct_sign_and_send_raw_middleware
from config import MAIN_URL, TEST_URL


class EthAccount(object):
    """
    账户类
    """
    def __init__(self, private_key, w3=None, is_test_net=True):
        """
        初始化
        """
        # 私钥
        self.private_key = private_key
        assert private_key.startswith("0x"), "Private key must start with 0x hex prefix"
        # web3类
        if w3 is None:
            w3 = Web3(HTTPProvider(TEST_URL if is_test_net else MAIN_URL))
        self.w3 = w3
        # 创建账户类
        account: LocalAccount = Account.from_key(private_key)
        w3.middleware_onion.add(construct_sign_and_send_raw_middleware(account))
        self.acc = account

    def get_balance(self, eth_format=True, ret_float=True):
        """
        获取余额
        """
        balance = self.w3.eth.get_balance(self.acc.address)
        if eth_format:
            balance = self.w3.from_wei(balance, 'ether')

        return float(balance) if ret_float else balance

    def send_transaction(
            self, to_address, value, gas_price=None, gas=None):
        """
        发送交易
        """
        res = self.w3.eth.send_transaction({
            'to': to_address,
            'from': self.acc.address,
            'value': self.w3.to_wei(value, 'ether'),
            'gas': gas,
            'gasPrice': gas_price
        })
        return res.hex()

    def send_all_value(self, to_address):
        """
        发送所有余额
        """
        # 获取账户余额和 gas 价格
        balance = self.get_balance(eth_format=False, ret_float=False)
        gas_price = self.w3.eth.gas_price

        # 计算 gas 消耗和总金额
        gas = self.w3.eth.estimate_gas({
            'from': self.acc.address, 'to': to_address, 'value': balance})
        total_amount = balance - gas * gas_price

        # 发送全部余额
        res = self.w3.eth.send_transaction({
            'to': to_address,
            'from': self.acc.address,
            'value': total_amount,
            'gas': gas,
            'gasPrice': gas_price
        })

        return res.hex()


if __name__ == '__main__':
    with open('../data/secret_data/used_test_file.txt', 'r') as f:
        info_list = f.readlines()
    private_key = info_list[0].strip().split('----')[1]
    account = EthAccount(private_key)
    print(account.acc.address)
    print(account.get_balance())
    print(account.send_all_value(account.acc.address))
