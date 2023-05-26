# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b4_get_nft_img.py
@Time: 2023-03-25 23:36
@Last_update: 2023-03-25 23:36
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import requests


if __name__ == '__main__':
    index = 11079

    for i in range(100):
        print(i, index)
        url = f'https://ipfs.io/ipfs/QmTRuWHr7bpqscUWFmhXndzf5AdQqkekhqwgbyJCqKMHrL/{index}.png'
        response = requests.get(url)
        with open(f'data/nft_img/{index}.png', 'wb') as f:
            f.write(response.content)
        index += 1
