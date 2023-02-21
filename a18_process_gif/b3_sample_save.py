#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b3_sample_save.py
@Time: 2020-04-07 13:25
@Last_update: 2020-04-07 13:25
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
import imageio


def create_gif(image_list, gif_name):
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    # Save them as frames into a gif
    imageio.mimsave(gif_name, frames, 'GIF', duration=0.03)

    return


def main():
    save_dir = 'data/goal'
    # image_list = [os.path.join(save_dir, file) for file in os.listdir(save_dir) if 'test1-' in file]
    image_list = [os.path.join(save_dir, 'test1-%d.png' % i) for i in range(63, 121)]
    image_list.sort(key=lambda x: int(x.split('.png')[0].split('test1-')[-1]))
    image_list1 = image_list.copy()
    image_list1.sort(key=lambda x: int(x.split('.png')[0].split('test1-')[-1]), reverse=True)
    gif_name = os.path.join(save_dir, 'created_gif1.gif')
    image_list += image_list1
    create_gif(image_list, gif_name)


if __name__ == "__main__":
    main()
