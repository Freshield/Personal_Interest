# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b12_test_dc_text_format.py
@Time: 2022-03-03 20:49
@Last_update: 2022-03-03 20:49
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""

import redis
import discord
from discord.ext import tasks
from config import discord_test_token, channel_id_dict
from lib.get_price_embed import get_price_embed
from lib.get_items_embed import get_item_embed


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        channel = client.get_channel(channel_id_dict['二次元社区'])

        project_name = "doodles-official"
        info_dict = {
            'project_name': project_name, 'last_price': 11.1,
            'new_price': 10.0
        }
        embed = get_price_embed(info_dict)
        await channel.send(embed=embed)

        info_dict = {
            'project_name': project_name, 'item_list': ['1111_11.0', '2222_10.1']
        }
        embed = get_item_embed(info_dict)
        await channel.send(embed=embed)

        print('------')
        exit()

print('begin test server')
client = MyClient()
client.run(discord_test_token)
