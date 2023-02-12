# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a1_opencv_resize.py
@Time: 2022-11-09 18:06
@Last_update: 2022-11-09 18:06
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

img = cv2.imread('data/QRcode_SP — 1.jpg', cv2.IMREAD_UNCHANGED)

print('Original Dimensions : ', img.shape)

scale_percent = 20  # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_NEAREST)

cv2.imwrite('data/result.jpg', resized)
print('Resized Dimensions : ', resized.shape)

# cv2.imshow("Resized image", resized)
# cv2.waitKey(0)
# cv2.destroyAllWindows()