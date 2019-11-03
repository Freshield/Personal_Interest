#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b3_block_store.py
@Time: 2019-11-02 16:29
@Last_update: 2019-11-02 16:29
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

with h5py.File('data/b3.h5', 'w') as f:
    dset = f.create_dataset('Images', shape=(100, 480, 640), dtype=np.uint8, chunks=(1, 64, 64))

    print(dset.chunks)

    image = dset[0, :, :]
    print(image.shape)

    tile = dset[0, 0:64, 0:64]
    print(tile.shape)