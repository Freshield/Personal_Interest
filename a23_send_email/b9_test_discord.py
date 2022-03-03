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
from config import discord_token, channel_id


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True, db=8)
        # start the task to run in the background
        self.my_background_task.start()

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    @tasks.loop(seconds=2)
    async def my_background_task(self):
        channel = client.get_channel(channel_id)
        with redis.Redis(connection_pool=self.pool) as r:
            for i in range(r.llen('new_info')):
                info = r.lpop('new_info')
                print(info)
                await channel.send(info)

    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()# wait until the bot logs in


client = MyClient()
client.run(discord_token)
