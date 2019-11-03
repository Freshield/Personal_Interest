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
    cmd = 'ffmpeg -i %s -codec:a libmp3lame -qscale:a 6 %s'
    os.system(cmd%(wav_file,mp3_file))

def del_ending_files_in_dir(file_dir,ending):
    for file_name in os.listdir(file_dir):
        temp_ending = file_name.split('.')[-1]
        if temp_ending == ending:
            yy.io.del_file(file_dir, file_name)
            print('Done del %s'%file_name)

def convert_all_wav_to_mp3_in_dir(file_dir, is_del:False):
    for file_name in os.listdir(file_dir):
        temp_ending = file_name.split('.')[-1]
        if temp_ending == 'wav':
            file_title = '.'.join(file_name.split('.')[:-1])
            print(file_title)
            wav_path = yy.io.join(file_dir,file_name)
            mp3_path = yy.io.join(file_dir,file_title+'.mp3')
            print(wav_path)
            print(mp3_path)
            if is_del:
                convert_del_wav(wav_path, mp3_path)
            else:
                convert_wav_to_mp3(wav_path, mp3_path)
            print('Done convert %s'%file_name)

def convert_del_wav(wav_file, mp3_file):
    convert_wav_to_mp3(wav_file, mp3_file)
    yy.io.del_file('', wav_file)

def convert_del_all_wav_in_dir(file_dir):
    convert_all_wav_to_mp3_in_dir(file_dir, is_del=True)
    del_ending_files_in_dir(file_dir,'wav')

if __name__ == "__main__":
    file_dir = '/media/freshield/YYSPACE/VOICE'
    convert_del_all_wav_in_dir(file_dir)