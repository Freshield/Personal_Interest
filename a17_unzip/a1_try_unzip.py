#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: a1_try_unzip.py
@Time: 2020-04-03 17:27
@Last_update: 2020-04-03 17:27
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
import time
from concurrent.futures import ProcessPoolExecutor


def unzip_file(filepath):
    filedir = filepath.split('.zip')[0]
    cmd = 'unzip -d %s %s' % (filedir, filepath)
    os.system(cmd)
    cmd = 'rm %s' % filepath
    os.system(cmd)



def get_all_zip_files(fileroot):
    rst_list = []
    for root, dirs, files in os.walk(fileroot):
        for file in files:
            if '.zip' in file:
                rst_list.append(os.path.join(root, file))

    return rst_list


def unzip_all(fileroot):
    data_path_list = get_all_zip_files(fileroot)

    begin = time.time()
    # with ProcessPoolExecutor(max_workers=8) as executor:
    #     executor.map(unzip_file, data_path_list)
    for filepath in data_path_list:
        unzip_file(filepath)

    end = time.time() - begin

    print('use %.2f minutes' % (end - begin)/60)



if __name__ == '__main__':
    filepath = '/media/freshield/SSD2_120/NCP备份_20200403/'
    unzip_all(filepath)