# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: get_items_embed.py
@Time: 2022-03-03 22:23
@Last_update: 2022-03-03 22:23
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


def get_item_embed(info_dict):
    """得到价格更改的embed卡片格式"""
    project_name = info_dict['project_name']
    item_list = info_dict['item_list']
    url = f'https://opensea.io/collection/{project_name}?search[sortAscending]=true&search[sortBy]=PRICE&search[toggles][0]=BUY_NOW'
    embed = discord.Embed(
        title=project_name,
        url=url,
        description=f"The project {project_name} new item list",
        color=discord.Color.blue())
    embed.set_author(
        name="Opensea Floor Monitor - New Items",
        url="https://twitter.com/freshield2")
    for item_line in item_list:
        item_id, item_price = item_line.split("_")
        embed.add_field(name="Item id", value=item_id, inline=True)
        embed.add_field(name="Item price", value=item_price, inline=True)
    embed.add_field(name="Time", value=f"<t:{int(time.time())}>", inline=False)
    embed.set_footer(text="Created by freshield.eth")

    return embed