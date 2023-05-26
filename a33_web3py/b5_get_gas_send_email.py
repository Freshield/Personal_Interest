# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b5_get_gas_send_email.py
@Time: 2023-03-28 21:17
@Last_update: 2023-03-28 21:17
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
from web3 import Web3, HTTPProvider

from config import MAIN_URL, TEST_URL
from lib.send_email import send_email
from lib.get_bj_time import get_bj_time

if __name__ == '__main__':
    main_w3 = Web3(HTTPProvider(MAIN_URL))
    test_w3 = Web3(HTTPProvider(TEST_URL))
    main_gas_threshold = 30
    test_gas_threshold = 100
    main_last_send_time = 0.
    test_last_send_time = 0.
    wait_time = 1.5 * 60
    main_send_wait_time = 5 * 60
    test_send_wait_time = 10 * 60
    monitor_test = False

    while True:
        try:
            bj_hour = int(get_bj_time().strftime("%-H"))
            main_gas = main_w3.from_wei(main_w3.eth.gas_price, 'gwei')
            print(f'bj hour is {bj_hour}')
            print(f'Main Gas Price is {main_gas:.2f}, threshold is {main_gas_threshold}')
            # 对于主网，如果小于阈值，且距离上次发送时间大于5分钟，且在白天，则发送邮件
            if (main_gas < main_gas_threshold) and ((bj_hour > 9) and (bj_hour < 23)) and (
                    (time.time() - main_last_send_time) > main_send_wait_time):
                text = f'!!!!!!Main Gas {main_gas:.2f}, threshold {main_gas_threshold} bj hour {bj_hour}'
                send_email(text, text)
                main_last_send_time = time.time()
                print('Done send the email')
            # 对于测试网，如果小于阈值，且距离上次发送时间大于5分钟，且在白天，则发送邮件
            if monitor_test:
                test_gas = test_w3.from_wei(test_w3.eth.gas_price, 'gwei')
                print(f'Test Gas Price is {test_gas:.2f}, threshold is {test_gas_threshold}')
                if (test_gas < test_gas_threshold) and (
                            (bj_hour > 9) and (bj_hour < 23)) and (
                            (time.time() - test_last_send_time) > test_send_wait_time):
                    text = f'Test Gas Price is {test_gas:.2f}, threshold {test_gas} bj hour is {bj_hour}'
                    send_email(text, text)
                    test_last_send_time = time.time()
                    print('Done send the email')
        except Exception as e:
            print(e)

        # 每3分钟获取一次gas
        time.sleep(wait_time)
