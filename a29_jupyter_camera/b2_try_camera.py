# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b2_try_camera.py
@Time: 2023-01-18 22:05
@Last_update: 2023-01-18 22:05
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import cv2

video = cv2.VideoCapture(0)

try:
    while True:
        _, frame = video.read()
        frame = cv2.flip(frame, 1)
        cv2.imshow('test', frame)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
except Exception as e:
    pass
finally:
    video.release()
