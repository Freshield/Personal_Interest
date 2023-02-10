# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: t8_try_file_move.py
@Time: 2023-01-27 14:16
@Last_update: 2023-01-27 14:16
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
import shutil


if __name__ == '__main__':
    src_path = '../data/url_list.json'
    dst_path = '../data/url_list_test.json'
    shutil.move(src_path, dst_path)
