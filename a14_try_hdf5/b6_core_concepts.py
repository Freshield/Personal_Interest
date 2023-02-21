#coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b6_core_concepts.py
@Time: 2019-11-02 17:12
@Last_update: 2019-11-02 17:12
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
import shutil
import h5py
import numpy as np

os.remove('data/mytestfile.hdf5')

with h5py.File('data/mytestfile.hdf5', 'a') as f:
    print(list(f.keys()))

    dset = f.create_dataset('mydataset', (100,), dtype='i')

    print(dset.shape)
    print(dset.dtype)

    dset[...] = np.arange(100)
    print(dset[0])
    print(dset[10])
    print(dset[0:100:10])

    print(dset.name)
    print(f.name)

    grp = f.create_group('subgroup')
    dset2 = grp.create_dataset('another_dataset', (50, ), dtype='f')
    print(dset2.name)
    print(dset2.dtype)

    dset3 = f.create_dataset('subgroup2/dataset_three', (10, ), dtype='i')
    print(dset3.name)
    print(dset3.dtype)

    dataset3 = f['subgroup2/dataset_three']
    print(dataset3.shape)
    print()
    for name in f:
        print(name)
    print()

    def printname(name, obj):
        print(name)
        print(obj)
        print()

    f.visititems(printname)

    dset.attrs['temperature'] = 99.5
    print(dict(dset.attrs))
