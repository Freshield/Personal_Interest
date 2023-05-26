# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: t5_fastapi_image.py
@Time: 2023-04-09 20:55
@Last_update: 2023-04-09 20:55
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import StreamingResponse, Response

from lib.get_layer0_gas_image import get_layer0_gas_image

app = FastAPI()

app.mount('/static', StaticFiles(directory='../static'), name='static')


@app.get('/')
def main():
    return 'server running'


@app.get('/image')
def get_image():

    return Response(get_layer0_gas_image(), media_type='image/png')


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
