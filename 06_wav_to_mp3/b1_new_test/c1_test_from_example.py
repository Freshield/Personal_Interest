#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: c1_test_from_example.py
@Time: 18-8-10 10:53
@Last_update: 18-8-10 10:53
@Desc: None
"""
import os

def wav_to_mp3(file_path, save_path):
    os.system('ffmpeg -i %s %s'%(file_path,save_path))

wav_to_mp3('test.wav','test4.mp3')