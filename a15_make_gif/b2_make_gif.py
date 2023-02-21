#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b2_make_gif.py
@Time: 2020-03-18 12:06
@Last_update: 2020-03-18 12:06
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


def make_sample_image(image_shape, hard_path):
    sample = cv2.imread(hard_path)
    x,y,c = image_shape
    target_size = min(x, y)
    sample = cv2.resize(sample, (target_size, target_size), interpolation=cv2.INTER_LINEAR)
    b, g, r = cv2.split(sample)
    sample = cv2.merge([r, g, b])

    rst_image = np.zeros((x,y,c), dtype=sample.dtype)
    rst_image[int(x/2-target_size/2):int(x/2+target_size/2), int(y/2-target_size/2):int(y/2+target_size/2), :] = sample

    return sample


def make_one_gif(image_path, save_name, target_size=720, duration=1, hard_sample_path=None):
    image = cv2.imread(image_path)

    x, y, c = image.shape
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

    img_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    if hard_image_path is not None:
        sample = make_sample_image(image.shape, hard_sample_path)
        frames = [sample, sample, img_gray]
    else:
        frames = [img_gray]
    b, g, r = cv2.split(image)
    image = cv2.merge([r, g, b])
    for i in range(5):
        frames.append(image)

    if hard_sample_path is not None:
        frames.extend([img_gray, sample, sample])

    imageio.mimsave(save_name, frames, 'GIF', duration=duration)


if __name__ == '__main__':
    import os

    a = np.zeros((100,100,3))
    a[...,2] = 1
    a[...,[0,1,2]] = a[...,[2,0,1]]
    print(a.shape)
    print(a[0,0])
    exit()

    # data_dir = 'data/raw'
    # save_dir = 'data/gif'
    # image_path_list = [os.path.join(data_dir, data_name) for data_name in os.listdir(data_dir)]
    # save_path_list = [data_path.replace(data_dir, save_dir) for data_path in image_path_list]
    # save_path_list = [os.path.splitext(data_path)[0]+'.gif' for data_path in save_path_list]
    #
    # for i in range(len(image_path_list)):
    #     make_one_gif(image_path_list[i], save_path_list[i])

    hard_image_path = 'data/raw/3.jpg'
    hard_sample_path = 'data/sample.jpg'
    hard_save_path = 'data/gif/3.gif'
    make_one_gif(hard_image_path, hard_save_path, hard_sample_path=hard_sample_path)