# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b6_zksync2.py
@Time: 2023-04-06 11:43
@Last_update: 2023-04-06 11:43
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from zksync2.module.module_builder import ZkSyncBuilder
from zksync2.core.types import EthBlockParams

zksync_web3 = ZkSyncBuilder.build("https://mainnet.era.zksync.io")
print(zksync_web3.from_wei(zksync_web3.zksync.gas_price, 'gwei'))
zk_balance = zksync_web3.eth.get_balance(
    '0xEd443Bb6bC3f2889418eCF8D627CCBeDc7e2F920', EthBlockParams.LATEST.value)
print(zksync_web3.from_wei(zk_balance, 'ether'))

