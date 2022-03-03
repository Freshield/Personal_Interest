# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b9_test_discord.py
@Time: 2022-03-03 11:54
@Last_update: 2022-03-03 11:54
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
from config import discord_token, channel_id_dict


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True, db=8)
        # start the task to run in the background
        self.my_background_task.start()

    async def on_ready(self):
        with redis.Redis(connection_pool=self.pool) as r:
            for i in range(r.llen('new_info')):
                info = r.lpop('new_info')
                print(info)
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        channel = client.get_channel(channel_id_dict['二次元社区'])
        await channel.send('begin')
        print('------')

    @tasks.loop(seconds=2)
    async def my_background_task(self):
        with redis.Redis(connection_pool=self.pool) as r:
            for i in range(r.llen('new_info')):
                info = r.lpop('new_info')
                print(info)
                for key, channel_id in channel_id_dict.items():
                    channel = client.get_channel(channel_id)
                    await channel.send(info)

    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()# wait until the bot logs in

print('begin server')
client = MyClient()
client.run(discord_token)
