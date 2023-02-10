# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b1_download_img.py
@Time: 2023-01-25 19:45
@Last_update: 2023-01-25 19:45
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
import time
import json
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import requests

if __name__ == '__main__':
    cookie_path = 'data/cookie.json'
    with open(cookie_path, 'r') as f:
        cookie_list = json.loads(f.read())

    url = 'https://www.documentchecker.com/rdo.dll/getpict?username=Demo%20Slope.User&cookieid=&Pictname=Paspoorten/A/ALB/ALB_P4/JPG/ALB_P4_Datapage'
    url = 'https://www.documentchecker.com/rdo.dll/incstatcount?username=Demo Slope.User&cookieid=&producttype=ID&action=Select&countrycode=ALB'
    url = 'https://www.documentchecker.com/rdo.dll/getdoc?doctype=KDI_THUMBNAILS&username=Demo Slope.User&cookieID=&language=1033&countrycode=ALB&IDTypeTabIndex=0'
    url = 'https://www.documentchecker.com/rdo.dll/getdoc?docname=KDI_SHOWDOC&username=Demo Slope.User&cookieid=&language=1033&CountryCode=DZA&SerieNr=P3&IDType=P'
    url = 'https://www.documentchecker.com/rdo.dll/getdoc?docname=KDI_SHOWDOC&username=Demo Slope.User&cookieid=&language=1033&CountryCode=AFG&SerieNr=P8&IDType=P'
    url = 'https://www.documentchecker.com/rdo.dll/getpict?username=demo slope.user&cookieid=&pictname=paspoorten/a/afg/afg_p8/jpg/afg_p8_datapage'
    url = 'https://www.documentchecker.com/rdo.dll/getdoc?docname=NAD_Thumbnails&Username=Demo Slope.User&CookieID=&language=1033&StateCode=AL&CardSeries='
    chrome_options = Options()
    chrome_options.add_argument('--proxy-server=http://127.0.0.1:7890')

    driver = Chrome(options=chrome_options)

    driver.get(url)
    for cookie_dict in cookie_list:
        driver.add_cookie(cookie_dict)
    driver.get(url)
    time.sleep(3)
    # html_str = driver.page_source
    # with open('data/test1.html', 'w') as f:
    #     f.write(html_str)

    for request in driver.requests:
        img = request.response.body

    # driver.save_screenshot('data/test.png')
    driver.close()


