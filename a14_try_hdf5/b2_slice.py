#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b2_slice.py
@Time: 2019-10-29 16:19
@Last_update: 2019-10-29 16:19
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
import h5py

with h5py.File('data/b2.h5', 'w') as f:
    f['data1'] = np.random.rand(100, 1000) - 0.5
    dset = f['data1']
    print(dset)
    out = dset[0:10, 20:70]
    print(out.shape)
    dset[0:10, 20:70] = out * 2

