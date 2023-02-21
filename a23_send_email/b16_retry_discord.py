# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b16_retry_discord.py
@Time: 2022-08-23 17:18
@Last_update: 2022-08-23 17:18
@Desc: None
@==============================================@
@      _____             _   _     _   _       @
@     |   __|___ ___ ___| |_|_|___| |_| |      @
@     |   __|  _| -_|_ -|   | | -_| | . |      @
@     |__|  |_| |___|___|_|_|_|___|_|___|      @
@                                    Freshield @
@==============================================@
"""
import time
import traceback
import discord
from discord.ext import tasks
from config import discord_token
from b17_try_embed import get_embed


class DCClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True, db=8)
        # start the task to run in the background
        # self.my_background_task.start()
        self.channel = None

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        channel = client.get_channel(1011566599045652510)
        self.channel = channel

        embed = get_embed('lonnnnnnnnnnnnnnnnnnnnnnnng loooooooooooooooooooooooog', is_normal=True)
        await channel.send(embed=embed)
        embed = get_embed('warnnnnnnnnnnnnnnnnnnnnning messssssssssssssssssssssage', is_normal=False)
        await channel.send(embed=embed)
        print('------')
        self.my_background_task.start()

    @tasks.loop(seconds=2)
    async def my_background_task(self):
        try:
            # with redis.Redis(connection_pool=self.pool) as r:
            #     for i in range(r.llen('new_info')):
            #         info = r.lpop('new_info')
            #         print(info)
            #         info_dict = json.loads(info)
            #         # email
            #         send_email_to_register(info_dict)
            #         # dc
            #         await send_dc_to_register(client, info_dict)
            #         print(info_dict)
            embed = get_embed('here', is_normal=True)
            await self.channel.send(embed=embed)
            print('here')
        except Exception as e:
            print(traceback.format_exc())

    # @my_background_task.before_loop
    # async def before_my_task(self):
    #     await self.wait_until_ready()# wait until the bot logs in


if __name__ == '__main__':
    print('begin server')
    client = DCClient(intents=discord.Intents.default())
    client.run(discord_token)
