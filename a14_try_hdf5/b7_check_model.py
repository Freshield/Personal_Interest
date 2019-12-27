#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b7_check_model.py
@Time: 2019-11-05 17:40
@Last_update: 2019-11-05 17:40
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
import h5py
import numpy as np

os.remove('data/small_model.h5')

f = h5py.File('data/model.h5', 'r')
print(dict(f.attrs))

f1 = h5py.File('data/small_model.h5', 'w')

for key, attr in f.attrs.items():
    f1.attrs[key] = attr

# for key, value in f.items():
#     print(key)
#     print(value)
#     print(value.name)
#     print()


def get_hdf5_data_list(input_item):
    rst_list = []
    if type(input_item) == h5py.File:
        for key, value in input_item.items():
            rst_list += get_hdf5_data_list(value)
    elif type(input_item) == h5py.Group:
        if len(input_item) == 0:
            rst_list.append((input_item.name, None))
        else:
            for key, value in input_item.items():
                rst_list += get_hdf5_data_list(value)
    elif type(input_item) == h5py.Dataset:
        a = input_item[:]
        rst_list.append((input_item.name, a.copy()))
    else:
        print(type(input_item))

    return rst_list



rst_list = get_hdf5_data_list(f)

print(rst_list)

for i in range(100):
    if rst_list[i][1] is None:
        f1.create_group(rst_list[i][0])
    else:
        f1[rst_list[i][0]] = rst_list[i][1]

f.close()
f1.close()