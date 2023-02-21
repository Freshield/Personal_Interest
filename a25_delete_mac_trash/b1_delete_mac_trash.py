# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b1_delete_mac_trash.py
@Time: 2022-06-02 13:51
@Last_update: 2022-06-02 13:51
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

mac_trash_path_list = []
for root, dirs, files in os.walk('/media/freshield/DATA_2T'):
    for file in files:
        if file == '.DS_Store':
            file_path = os.path.join(root, file)
            mac_trash_path_list.append(file_path)

print(mac_trash_path_list)
print(len(mac_trash_path_list))

for path in mac_trash_path_list:
    os.remove(path)
