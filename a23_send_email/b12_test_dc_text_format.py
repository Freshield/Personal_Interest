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


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        project_name = "doodles-official"
        url = f'https://opensea.io/collection/{project_name}?search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW'

        embed = discord.Embed(
            title=project_name,
            url=url,
            description="nd the different components",
            color=0xFF5733)
        embed.set_author(
            name="Opensea Floor Monitor",
            url="https://twitter.com/freshield2")
        channel = client.get_channel(channel_id_dict['二次元社区'])
        await channel.send(embed=embed)
        print('------')
        exit()

print('begin test server')
client = MyClient()
client.run(discord_test_token)
