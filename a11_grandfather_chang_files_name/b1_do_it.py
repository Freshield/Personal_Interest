#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: b1_do_it.py
@Time: 2019-03-05 11:22
@Last_update: 2019-03-05 11:22
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
import yy_lib as yy

data_dir = '/media/freshield/Data_2T/1993包青天'

sub_dir_list = [path for path in os.listdir(data_dir)]
sub_dir_list.sort()
# count = 61
# for num,sub_dir in enumerate(sub_dir_list):
#     num += 1
#     if num < 13:
#         continue
#
#     sub_dir_path = os.path.join(data_dir, sub_dir)
#     for file_name in os.listdir(sub_dir_path):
#         if count < 100:
#             new_file_name = '0%d%s' % (count, file_name)
#         else:
#             new_file_name = '%d%s' % (count, file_name)
#
#         yy.io.rename_file(sub_dir_path, file_name, new_file_name)
#
#         count += 1

for num, sub_dir in enumerate(sub_dir_list):
    sub_dir_path = os.path.join(data_dir, sub_dir)
    for file_name in os.listdir(sub_dir_path):
        file_path = os.path.join(sub_dir_path, file_name)
        yy.io.move_dir_or_file(sub_dir_path, file_name, data_dir, file_name)