# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: server.py
@Time: 2023-03-07 21:10
@Last_update: 2023-03-07 21:10
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import json
import os
import random
import requests
import uvicorn
import traceback
from typing import Optional
from fastapi import FastAPI, File, UploadFile
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from pydantic import BaseModel

from lib.logs import LOGGER
from lib.AESCipher import AESCipher
from lib.LarkBot import LarkBot
from lib.parse_msg_json import parse_msg_json

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


class CheckData(BaseModel):
    """Lark测试数据"""
    encrypt: str


cipher = AESCipher(os.environ.get('LARK_ENCRYPT_KEY'))
lark_bot = LarkBot(os.environ.get('LARK_APPID'), os.environ.get('LARK_APPSECRET'))


@app.post('/')
async def bot_reply(check_data: CheckData):
    """对用户的问题进行回复"""
    res_dict = {'code': -1, 'msg': 'nothing'}
    try:
        LOGGER.info(f'Successfully get check data!')
        encrypt = check_data.encrypt
        json_dict = json.loads(cipher.decrypt_string(encrypt))
        LOGGER.info(f'input json{json_dict}')
        # 如果是challenge则返回challenge
        if json_dict.get('type', None) == 'url_verification':
            return {'challenge': json_dict['challenge']}
        json_dict = parse_msg_json(json_dict)
        # 保证是正确的聊天event
        if json_dict['event_type'] != 'im.message.receive_v1':
            return {'code': -1, 'msg': 'invalid event type'}

        # 区分不同的聊天类型
        if json_dict['chat_type'] == 'group':
            response = await lark_bot.reply_group_msg(json_dict)
        elif json_dict['chat_type'] == 'p2p':
            response = await lark_bot.reply_p2p_msg(json_dict)

        res_dict = res_dict if response is None else response
        LOGGER.info(f'res dict, {res_dict}')

        return {'code': res_dict['code'], 'msg': res_dict['msg']}
    except Exception as e:
        error_info = traceback.format_exc()
        LOGGER.error(error_info)

        res_dict = await lark_bot.reply_error_msg(json_dict, '对不起，服务器出现了错误，请稍后再试！')
        LOGGER.info(f'error res dict, {res_dict}')

        return {'code': res_dict['code'], 'msg': res_dict['msg']}


if __name__ == '__main__':
    uvicorn.run(app=app, host='0.0.0.0', port=9876)
