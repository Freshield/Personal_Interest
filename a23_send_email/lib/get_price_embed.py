# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: get_price_embed.py
@Time: 2022-03-03 22:05
@Last_update: 2022-03-03 22:05
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
import discord
from config import project_thumbnail_dict


def get_price_embed(info_dict):
    """得到价格更改的embed卡片格式"""
    project_name = info_dict['project_name']
    last_price = info_dict['last_price']
    new_price= info_dict['new_price']
    url = f'https://opensea.io/collection/{project_name}?search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW'
    embed = discord.Embed(
        title=project_name,
        url=url,
        description=f"The project {project_name} price is changed",
        color=discord.Color.red())
    embed.set_author(
        name="Opensea Floor Monitor - New Price",
        url="https://twitter.com/freshield2")
    embed.set_thumbnail(url=project_thumbnail_dict[project_name])
    embed.add_field(name="Last price", value=last_price, inline=True)
    embed.add_field(name="New price", value=new_price, inline=True)
    embed.add_field(name="Time", value=f"<t:{int(time.time())}>", inline=False)
    embed.set_footer(text="Created by freshield.eth")

    return embed
