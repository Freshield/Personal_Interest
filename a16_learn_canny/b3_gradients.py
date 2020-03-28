#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b3_gradients.py
@Time: 2020-03-30 10:00
@Last_update: 2020-03-30 10:00
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


def gradients(img_data, eps=1e-8, return_int=True):
    """使用sobel算子得到梯度图"""
    W, H = img_data.shape
    dx = np.zeros((W-2, H-2))
    dy = np.zeros((W-2, H-2))
    M = np.zeros((W-2, H-2))
    theta = np.zeros((W-2, H-2))

    # 定义sobel算子
    x_sobel = np.array([-1,0,1,-2,0,2,-1,0,1]).reshape((3,3))
    y_sobel = np.array([1,2,1,0,0,0,-1,-2,-1]).reshape((3,3))

    # 卷积计算
    for i in range(W-2):
        for j in range(H-2):
            dx[i, j] = np.sum(img_data[i:i+3, j:j+3] * x_sobel)
            dy[i, j] = np.sum(img_data[i:i+3, j:j+3] * y_sobel)

            M[i, j] = np.sqrt(np.square(dx[i, j]) + np.square(dy[i, j]))

            theta[i, j] = math.atan(dx[i, j] / (dy[i, j] + eps))

    if return_int:
        dx = dx.astype(np.uint8)
        dy = dy.astype(np.uint8)
        M = M.astype(np.uint8)

    return dx, dy, M, theta


if __name__ == '__main__':
    import cv2
    from b0_get_img_data import get_img_data
    from b1_gray import gray
    from b2_smooth import smooth

    img_path = 'data/test.jpg'
    img_data = get_img_data(img_path)
    img_data = gray(img_data)
    img_data = smooth(img_data)
    dx, dy, M, theta = gradients(img_data)

    # print(img_data.shape)
    # print(dx.shape)
    # print(np.sum(dx[:,-20:]))
    # exit()

    # img_data = img_data.astype(np.uint8)
    cv2.imshow('test', img_data)
    cv2.imshow('dx', dx)
    cv2.imshow('dy', dy)
    cv2.imshow('M', M)
    cv2.waitKey()