# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b8_gas_server.py
@Time: 2023-04-10 20:58
@Last_update: 2023-04-10 20:58
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
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from pydantic import BaseModel
from typing import Optional

from config import VERSION, VERIFY_CODE, PORT_NUM
from lib.logs import LOGGER
from lib.get_layer0_gas_image import get_layer0_gas_image
from lib.get_chain_gas import get_chain_gas

app = FastAPI()
# 跨域
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount('/static', StaticFiles(directory='./static'), name='static')


class PostData(BaseModel):
    """上传的数据"""
    veirfy_code: str
    chain: Optional[str] = None


@app.get('/')
def main():
    return 'server running'


@app.post('/get_image')
def get_image(post_data: PostData):
    """获取图片"""
    if post_data.veirfy_code != VERIFY_CODE:
        return 'Wrong verify code!'
    return Response(get_layer0_gas_image(), media_type='image/png')


@app.post('/get_gas')
def get_gas(post_data: PostData):
    """获取gas信息"""
    res_dict = dict()
    try:
        if post_data.veirfy_code != VERIFY_CODE:
            raise ValueError('Wrong verify code!')
        chain = post_data.chain
        if chain is None:
            return 'Please input chain!'
        gas, fee = get_chain_gas(chain)
        res_dict = {'gas': gas, 'fee': fee, 'chain': chain, 'status': 'success'}
    except Exception as e:
        res_dict = {'status': 'fail', 'error': str(e)}

    return res_dict


if __name__ == '__main__':
    LOGGER.info(f'Run the server with version {VERSION}')
    uvicorn.run(app, host='0.0.0.0', port=PORT_NUM)
