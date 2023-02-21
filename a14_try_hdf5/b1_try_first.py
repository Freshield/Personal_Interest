#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b1_try_first.py
@Time: 2020-03-09 16:12
@Last_update: 2020-03-09 16:12
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import h5py
import numpy as np

imgData = np.zeros((30, 3, 128, 256))
f = h5py.File('data/b1.h5', 'w')
f['data'] = imgData
f['labels'] = range(100)
f.close()

f = h5py.File('data/b1.h5', 'r')
print(f.keys())
a = f['data'][:]
print(a.shape)
print(f['labels'][:])
f.close()