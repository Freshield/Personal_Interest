#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b2_smooth.py
@Time: 2019-12-27 09:38
@Last_update: 2019-12-27 09:38
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import math
import numpy as np


def smooth(img_data, sigma=1.4, return_int=True):
    """
    生成一个(2k+1)x(2k+1)的高斯滤波器
    H[i, j] = (1/(2*pi*sigma**2))*exp((-1/(2*sigma**2)*((i-k-1)**2+(j-k-1)**2)
    """
    gau_sum = 0
    gaussian = np.zeros((5, 5))
    for i in range(5):
        for j in range(5):
            left = 1 / (2 * math.pi * sigma**2)
            right = math.exp((-1/(2*sigma**2)) * ((i-3-1)**2+(j-3-1)**2))
            gaussian[i, j] = left * right
            gau_sum += gaussian[i, j]

    gaussian = gaussian / gau_sum

    # 滤波
    W, H = img_data.shape
    new_gray = np.zeros((W-5, H-5))

    for i in range(W-5):
        for j in range(H-5):
            new_gray[i, j] = np.sum(img_data[i:i+5, j:j+5] * gaussian)

    if return_int:
        new_gray = new_gray.astype(np.uint8)

    return new_gray


if __name__ == '__main__':
    import cv2
    from b0_get_img_data import get_img_data
    from b1_gray import gray

    img_path = 'data/test.jpg'
    img_data = get_img_data(img_path)
    img_data = gray(img_data)
    img_data = smooth(img_data)

    img_data = img_data.astype(np.uint8)
    cv2.imshow('test', img_data)
    cv2.waitKey()