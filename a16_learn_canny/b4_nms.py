#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b4_nms.py
@Time: 2020-03-30 11:04
@Last_update: 2020-03-30 11:04
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


def nms(M, dx, dy, return_int=True):
    d = np.copy(M)
    W, H = M.shape
    NMS = np.copy(d)
    NMS[0, :] = NMS[-1, :] = NMS[:, 0] = NMS[:, -1] = 0

    for i in range(1, W-1):
        for j in range(1, H-1):
            # 梯度为0，不是边缘
            if M[i, j] == 0:
                NMS[i, j] = 0
            else:
                gradX = dx[i, j]
                gradY = dy[i, j]
                gradTemp = d[i, j]

                # 如果y方向梯度大
                if np.abs(gradY) > np.abs(gradX):
                    weight = np.abs(gradX) / np.abs(gradY)
                    grad2 = d[i, j-1]
                    grad4 = d[i, j+1]


                    # 如果x，y符号一致
                    # g1 g2
                    #    c
                    #    g4 g3
                    if gradX * gradY > 0:
                        grad1 = d[i-1, j-1]
                        grad3 = d[i+1, j+1]

                    # 如果x，y符号相反
                    #    g2 g1
                    #    c
                    # g3 g4
                    else:
                        grad1 = d[i+1, j-1]
                        grad3 = d[i-1, j+1]

                # 如果x方向梯度大
                else:
                    weight = np.abs(gradY) / np.abs(gradX)
                    grad2 = d[i-1, j]
                    grad4 = d[i+1, j]

                    # 如果x，y方向一致
                    #      g3
                    # g2 c g4
                    # g1
                    if gradX * gradY > 0:
                        grad1 = d[i-1, j+1]
                        grad3 = d[i+1, j-1]

                    # 如果x，y方向相反
                    # g1
                    # g2 c g4
                    #      g3
                    else:
                        grad1 = d[i-1, j-1]
                        grad3 = d[i+1, j+1]

                gradTemp1 = weight * grad1 + (1 - weight) * grad2
                gradTemp2 = weight * grad3 + (1 - weight) * grad4

                if (gradTemp > gradTemp1) and (gradTemp > gradTemp2):
                    NMS[i, j] = gradTemp
                else:
                    NMS[i, j] = 0

    if return_int:
        NMS = NMS.astype(np.uint8)

    return NMS


if __name__ == '__main__':
    import cv2
    from b0_get_img_data import get_img_data
    from b1_gray import gray
    from b2_smooth import smooth
    from b3_gradients import gradients

    img_path = 'data/test.jpg'
    img_data = get_img_data(img_path)
    img_data = gray(img_data)
    img_data = smooth(img_data, return_int=False)
    dx, dy, M, theta = gradients(img_data, return_int=False)
    img_data = nms(M, dx, dy)

    # print(img_data.shape)
    # print(dx.shape)
    # print(np.sum(dx[:,-20:]))
    # exit()

    M = M.astype(np.uint8)
    cv2.imshow('M', M)
    cv2.imshow('test', img_data)
    # cv2.imshow('dx', dx)
    # cv2.imshow('dy', dy)
    # cv2.imshow('M', M)
    cv2.waitKey()
