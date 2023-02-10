# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b7_get_id_card_imgs.py
@Time: 2023-01-26 20:10
@Last_update: 2023-01-26 20:10
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
from tqdm import tqdm
from selenium.webdriver.chrome.options import Options
from seleniumwire.webdriver import Chrome
from lib.get_id_card_url import get_id_card_url
from lib.get_img_url import get_img_url


def response_interceptor(request, response):
    # 这个过程是同步的，实际应用中建议通过进程/线程处理这部分逻辑
    t = response.headers['Content-Type']
    if 'rdo.dll/getpict' in request.url and t and 'image' in t:
        name = request.url.split('/')[-1]
        ending = t.split('/')[-1]
        img = response.body
        with open(f'data/test2/{name}.{ending}', 'wb') as f:
            f.write(img)


if __name__ == '__main__':
    # 准备cookie和country code以及driver
    cookie_path = 'data/cookie.json'
    with open(cookie_path, 'r') as f:
        cookie_list = json.loads(f.read())
    country_path = 'data/contry_code.json'
    with open(country_path, 'r') as f:
        country_code_list = json.loads(f.read())
    chrome_options = Options()
    chrome_options.add_argument('--proxy-server=http://127.0.0.1:7890')

    driver = Chrome(options=chrome_options)
    driver.response_interceptor = response_interceptor
    url = 'https://www.documentchecker.com/rdo.dll/getdoc?doctype=KDI_THUMBNAILS&username=Demo Slope.User&cookieID=&language=1033&countrycode=ALB&IDTypeTabIndex=0'
    driver.get(url)
    for cookie_dict in cookie_list:
        driver.add_cookie(cookie_dict)
    # 遍历country code
    country_code_list.sort()
    country_code_list = country_code_list[50:]
    for index, country_code in enumerate(country_code_list):
        url = f'https://www.documentchecker.com/rdo.dll/getdoc?doctype=KDI_THUMBNAILS&username=Demo Slope.User&cookieID=&language=1033&countrycode={country_code}&IDTypeTabIndex=0#tabsmain-3'
        print(f'{index}/{len(country_code_list)}, {url}')
        # 首先跳转到country页面
        driver.get(url)
        time.sleep(2)
        html_str = driver.page_source
        # 获取passport对应的url
        id_url_list = get_id_card_url(html_str)
        # 遍历每个passport url
        for id_url in id_url_list:
            driver.get(id_url)
            time.sleep(2)
            html_str = driver.page_source
            # 获取对应的主图的链接
            img_url_list = get_img_url(html_str)
            for img_url in img_url_list:
                # 进行访问下载
                driver.get(img_url)
                time.sleep(2)

    driver.close()
