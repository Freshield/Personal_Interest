# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b4_hello_world.py
@Time: 2023-03-03 19:21
@Last_update: 2023-03-03 19:21
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import gradio as gr

def image_classifier(inp, request: gr.Request):
    print(request)
    return {'cat': 0.3, 'dog': 0.7}

demo = gr.Interface(fn=image_classifier, inputs="text", outputs="label")
demo.launch()
