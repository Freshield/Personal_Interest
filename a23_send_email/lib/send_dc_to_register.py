# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: send_dc_to_register.py
@Time: 2022-03-10 22:31
@Last_update: 2022-03-10 22:31
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
from lib.get_price_embed import get_price_embed
from lib.get_items_embed import get_item_embed
from config import channel_register_dict, channel_id_dict


async def send_dc_to_register(client, info_dict):
    """向注册的dc频道发送信息"""
    # 生成相应的信息
    embed = get_price_embed(info_dict) \
        if info_dict['type'] == 'price' else get_item_embed(info_dict)

    # 发送到相应的频道
    project_name = info_dict['project_name']
    for channel_name, project_names in channel_register_dict.items():
        if project_name in project_names:
            channel = client.get_channel(channel_id_dict[channel_name])
            await channel.send(embed=embed)