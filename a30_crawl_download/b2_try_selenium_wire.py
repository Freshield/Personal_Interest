# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b2_try_selenium_wire.py
@Time: 2023-01-25 20:51
@Last_update: 2023-01-25 20:51
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
import json
from selenium.webdriver.chrome.options import Options
from seleniumwire.webdriver import Chrome


def response_interceptor(request, response):
    # 这个过程是同步的，实际应用中建议通过进程/线程处理这部分逻辑
    t = response.headers['Content-Type']
    if 'rdo.dll/getpict' in request.url and t and 'image' in t:
        img = request.response.body
        with open('data/test3.jpg', 'wb') as f:
            f.write(img)


if __name__ == '__main__':
    cookie_path = 'data/cookie.json'
    with open(cookie_path, 'r') as f:
        cookie_list = json.loads(f.read())

    url = 'https://www.documentchecker.com/rdo.dll/getpict?username=Demo%20Slope.User&cookieid=&Pictname=Paspoorten/A/ALB/ALB_P4/JPG/ALB_P4_Datapage'
    url = 'https://www.documentchecker.com/rdo.dll/getpict?username=demo slope.user&cookieid=&pictname=paspoorten/a/afg/afg_p8/jpg/afg_p8_datapage'
    chrome_options = Options()
    chrome_options.add_argument('--proxy-server=http://127.0.0.1:7890')

    driver = Chrome(options=chrome_options)
    driver.response_interceptor = response_interceptor
    driver.get(url)
    for cookie_dict in cookie_list:
        driver.add_cookie(cookie_dict)
    driver.get(url)
    time.sleep(3)

    # for request in driver.requests:
    #     req_url = request.url
    #     if 'rdo.dll/getpict' in req_url:
    #         img = request.response.body
    #         with open('data/test2.jpg', 'wb') as f:
    #             f.write(img)

    driver.close()