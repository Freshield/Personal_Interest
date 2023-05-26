# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: t6_try_post_gas_api.py
@Time: 2023-04-10 21:12
@Last_update: 2023-04-10 21:12
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import cv2
import numpy as np
import requests
from config import PORT_NUM, VERIFY_CODE, CHAIN_NAMES


if __name__ == '__main__':
    url = f'http://127.0.0.1:{PORT_NUM}'
    # get image
    response = requests.post(url=f'{url}/get_image', json={'veirfy_code': VERIFY_CODE}, timeout=20)
    image_data = response.content
    image_data = np.fromstring(image_data, np.uint8)
    image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)
    print(image.shape)
    cv2.imshow('image', image)
    cv2.waitKey(0)
    # get gas
    for chain in CHAIN_NAMES:
        print(chain)
        response = requests.post(
            url=f'{url}/get_gas', json={'veirfy_code': VERIFY_CODE, 'chain': chain}, timeout=20)
        print(response.json())

