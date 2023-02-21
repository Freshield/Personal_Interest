#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b2_resize.py
@Time: 2020-04-07 13:20
@Last_update: 2020-04-07 13:20
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
import cv2

data_dir = 'data'
save_dir = 'data/goal'


for file in os.listdir(data_dir):
    if 'test1-' in file:
        file_path = os.path.join(data_dir, file)
        image_data = cv2.imread(file_path)
        image_data = cv2.resize(image_data, (224, 168))
        cv2.imwrite(os.path.join(save_dir, file), image_data)