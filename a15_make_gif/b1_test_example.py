#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b1_test_example.py
@Time: 2020-03-18 11:32
@Last_update: 2020-03-18 11:32
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
import imageio


image_list = 'data/1.jpg'

gif_name = 'data/1.gif'

duration = 1
target_size = 720

image = cv2.imread(image_list)

x,y,c = image.shape
print(image.shape)

if (x >= target_size) or (y >= target_size):
    if x >= y:
        new_x = target_size
        new_y = int((y * new_x) / x)
    else:
        new_y = target_size
        new_x = int((x * new_y) / y)
    image = cv2.resize(image, (new_y, new_x), interpolation=cv2.INTER_LINEAR)
    print(image.shape)

img_gray = cv2.cvtColor(image,cv2.COLOR_RGB2GRAY)
frames = [img_gray]
b,g,r = cv2.split(image)
image = cv2.merge([r,g,b])
for i in range(5):
    frames.append(image)

imageio.mimsave(gif_name, frames, 'GIF', duration=duration)