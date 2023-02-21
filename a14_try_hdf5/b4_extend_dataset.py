#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b4_extend_dataset.py
@Time: 2019-11-03 16:37
@Last_update: 2019-11-03 16:37
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

with h5py.File('data/b4.h5', 'w') as f:
    dset = f.create_dataset('chunck', shape=(100, 480), dtype=np.uint8,
                            maxshape=(None, 480), chunks=(1, 480))
    print(dset.chunks)