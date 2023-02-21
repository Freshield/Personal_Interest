# coding=utf-8
"""
@Author: Freshield
@Contact: yangyufresh@163.com
@File: b17_try_embed.py
@Time: 2022-08-23 17:33
@Last_update: 2022-08-23 17:33
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


def get_embed(msg, is_normal=True):
    word = 'normal' if is_normal else 'warning'
    color = discord.Color.blue() if is_normal else discord.Color.red()
    embed = discord.Embed(
        title=f'There have a {word} log\n<t:{int(time.time())}>',
        color=color)
    embed.add_field(name="message", value=msg)
    embed.set_footer(text="Created by freshield.eth")
    return embed
