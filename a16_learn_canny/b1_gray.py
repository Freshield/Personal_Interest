# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b1_gray.py
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
import numpy as np


def gray(img_data):
    img_data = cv2.cvtColor(img_data, cv2.COLOR_BGR2RGB)
    img_data = np.dot(img_data[...,:3], [0.299, 0.587, 0.114])
    img_data = img_data.astype(np.uint8)
    # img_data = np.stack([img_data,img_data,img_data], axis=2)
    # img_data = img_data[...,0]
    # img_data = cv2.cvtColor(img_data, cv2.COLOR_BGR2GRAY)
    # print(img_data.shape)
    # print(img_data[50, 50:60])
    # exit()

    return img_data


if __name__ == '__main__':
    from b0_get_img_data import get_img_data
    img_path = 'data/test.jpg'
    img_data = get_img_data(img_path)
    img_data = gray(img_data)
    cv2.imshow('test', img_data)
    cv2.waitKey()