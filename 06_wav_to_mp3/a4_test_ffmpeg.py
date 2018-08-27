#coding=utf-8
"""
@Author: Freshield
@License: (C) Copyright 2018, BEIJING LINKING MEDICAL TECHNOLOGY CO., LTD.
@Contact: yangyufresh@163.com
@File: a4_test_ffmpeg.py
@Time: 18-8-24 14:04
@Last_update: 18-8-24 14:04
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



def convert_wav_to_mp3(wav_file, mp3_file):
    yy.io.judge_del_file('',mp3_file)
    cmd = 'ffmpeg -i %s -codec:a libmp3lame -qscale:a 4 %s'
    os.system(cmd%(wav_file,mp3_file))


