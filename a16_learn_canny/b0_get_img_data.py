# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b0_get_img_data.py
@Time: 2020-03-29 22:52
@Last_update: 2020-03-29 22:52
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import cv2


def get_img_data(img_path):
    return cv2.imread(img_path)


if __name__ == '__main__':
    import numpy as np
    img_path = 'data/test.jpg'
    img_data = get_img_data(img_path)
    img_data = np.zeros((100,100,3))
    img_data[...,0] = 1
    cv2.imshow('test', img_data)
    cv2.waitKey()