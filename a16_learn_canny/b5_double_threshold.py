#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b5_double_threshold.py
@Time: 2020-03-28 13:38
@Last_update: 2020-03-28 13:38
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import numpy as np


def double_threshold(img_data, return_int=True):
    W, H = img_data.shape
    DT = np.zeros((W, H))

    TL = 0.1 * np.max(img_data)
    TH = 0.3 * np.max(img_data)


    for i in range(1, W-1):
        for j in range(1, H-1):
            if img_data[i, j] < TL:
                DT[i, j] = 0
            elif img_data[i, j] > TH:
                DT[i, j] = 255
            # elif (img_data[i-1, j-1:j+1]<TH).any() or (img_data[i+1, j-1:j+1].any()) or (img_data[i, [j-1, j+1]]<TH).any():
            #     DT[i, j] = 255
            elif (img_data[i-1:i+2, j-1:j+2] > TH).any():
                DT[i, j] = 255

    if return_int:
        DT = DT.astype(np.uint8)

    print(np.unique(DT))

    return DT
                

if __name__ == '__main__':
    import cv2
    from b0_get_img_data import get_img_data
    from b1_gray import gray
    from b2_smooth import smooth
    from b3_gradients import gradients
    from b4_nms import nms

    img_path = 'data/test1.png'
    img_data = get_img_data(img_path)
    img_data = gray(img_data)
    # img_data = smooth(img_data, return_int=False)
    # dx, dy, M, theta = gradients(img_data, return_int=False)
    # nms = nms(M, dx, dy, return_int=True)
    # img_data = double_threshold(nms)
    # img_data = cv2.GaussianBlur(img_data, (3,3), 0)
    # canny = cv2.Canny(img_data, 50, 100)

    # print(img_data.shape)
    # print(dx.shape)
    # print(np.sum(dx[:,-20:]))
    # exit()

    # M = M.astype(np.uint8)
    # cv2.imshow('M', M)
    # cv2.imshow('nms', nms)
    cv2.imshow('test', img_data)
    # cv2.imshow('canny', canny)
    # cv2.imshow('dx', dx)
    # cv2.imshow('dy', dy)
    # cv2.imshow('M', M)
    cv2.waitKey()
