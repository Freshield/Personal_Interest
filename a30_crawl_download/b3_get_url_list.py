# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b3_get_url_list.py
@Time: 2023-01-25 21:18
@Last_update: 2023-01-25 21:18
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
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



if __name__ == '__main__':
    cookie_path = 'data/cookie.json'
    with open(cookie_path, 'r') as f:
        cookie_list = json.loads(f.read())
    country_path = 'data/contry_code.json'
    with open(country_path, 'r') as f:
        country_code_list = json.loads(f.read())
    chrome_options = Options()
    chrome_options.add_argument('--proxy-server=http://127.0.0.1:7890')

    driver = Chrome(options=chrome_options)
    url = 'https://www.documentchecker.com/rdo.dll/getdoc?doctype=KDI_THUMBNAILS&username=Demo Slope.User&cookieID=&language=1033&countrycode=ALB&IDTypeTabIndex=0'
    driver.get(url)

    for country_code in country_code_list:
        url = f'https://www.documentchecker.com/rdo.dll/getdoc?doctype=KDI_THUMBNAILS&username=Demo Slope.User&cookieID=&language=1033&countrycode={country_code}&IDTypeTabIndex=0#tabsmain-2'
        print(url)

        for cookie_dict in cookie_list:
            driver.add_cookie(cookie_dict)
        driver.get(url)
        time.sleep(3)
        html = driver.page_source
        with open('data/test.html', 'w') as f:
            f.write(html)

        exit()

        # driver.find_element("link_text", "Passports").click()
        # time.sleep(2)

    # for request in driver.requests:
    #     req_url = request.url
    #     if 'rdo.dll/getpict' in req_url:
    #         img = request.response.body
    #         with open('data/test2.jpg', 'wb') as f:
    #             f.write(img)

    driver.close()


