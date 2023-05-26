# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: get_id_card_url.py
@Time: 2023-01-26 20:30
@Last_update: 2023-01-26 20:30
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from bs4 import BeautifulSoup


def get_id_card_url(html_str):
    soup = BeautifulSoup(html_str, 'html.parser')
    div = soup.find('div', id='tabsmain-3')
    containers = div.find_all('div', class_='thumbcontainer')
    url_list = []
    for container in containers:
        info = container.find('div', class_='info')
        a = info.find('a')
        info_tuple = eval(a.attrs['href'].split('onClickThumbnail(')[-1].split(');')[0])
        country_code, serie_number, id_type = info_tuple
        target_url = f'https://www.documentchecker.com/rdo.dll/getdoc?docname=KDI_SHOWDOC&username=Demo Slope.User&cookieid=&language=1033&CountryCode={country_code}&SerieNr={serie_number}&IDType={id_type}'
        url_list.append(target_url)

    return url_list