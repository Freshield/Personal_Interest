# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: get_layer0_gas_image.py
@Time: 2023-04-10 20:39
@Last_update: 2023-04-10 20:39
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
import cv2
import numpy as np
from playwright.sync_api import Playwright, sync_playwright, expect


def get_layer0_gas_image():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context(
            viewport={'height': 1000, 'width': 1000},
            user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36')
        page = context.new_page()
        page.goto("https://stargate.finance/transfer")
        page.get_by_text("Check Transfer Gas Estimator").click()
        time.sleep(2)

        element = page.wait_for_selector(
            'body > div.MuiDialog-root > div.MuiDialog-container.jss68.MuiDialog-scrollPaper > div > div.MuiDialogContent-root.jss73.jss74 > section > div > table > tbody > tr:nth-child(4) > td:nth-child(4) > div',
            timeout=10000)
        for i in range(25):
            time.sleep(0.5)
            if 'MATIC' in element.inner_text():
                break

        time.sleep(1)
        image_data = page.screenshot()

        page.close()
        context.close()
        browser.close()

    return image_data


if __name__ == '__main__':
    image_data = get_layer0_gas_image()
    image_data = np.frombuffer(image_data, np.uint8)
    image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)
    cv2.imshow('image', image)
    cv2.waitKey(0)
