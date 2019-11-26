#!/usr/bin/env python3
"""
BOT LIVES!
"""
# import asyncio
# import random
import os
import discord
# import importlib
import logging
import coloredlogs
# import sys
# from discord import Game
# from discord.ext import commands
from discord.ext.commands import Bot
"""bot Imports"""
from bot.lib import plugin, utils
from bot.skeleton import SkeletonBot

EXTENSIONS = [  
    'server',
    'example',
    ]

LOG = logging.getLogger(__name__)

APP_ID = os.getenv('APP_ID') or 'fakeid'
BOT_PREFIX = ("?", "!")
SHARD = os.getenv('SHARD') or 0
SHARD_COUNT = os.getenv('SHARD_COUNT') or 1
TOKEN = os.getenv('TOKEN')

def main():
    """Entrypoint if called as an executable."""
    args = utils.parse_arguments()
    logging.basicConfig(level=logging.INFO)
    coloredlogs.install(level=0,
                        fmt="[%(asctime)s][%(levelname)s] [%(name)s.%(funcName)s:%(lineno)d] %(message)s",
                        isatty=True)
    if args.debug:
        l_level = logging.DEBUG
    else:
        l_level = logging.INFO

    logging.getLogger(__package__).setLevel(l_level)
    logging.getLogger('discord').setLevel(l_level)
    logging.getLogger('websockets.protocol').setLevel(l_level)
    logging.getLogger('urllib3').setLevel(l_level)

    LOG.info("Bot brewing coffee. Just a moment")
    bot = SkeletonBot(shard_id=int(SHARD), shard_count=int(SHARD_COUNT), 
                      command_prefix=BOT_PREFIX, app_id=APP_ID)

    for extension in EXTENSIONS:
        plugin.load('bot.lib.plugins.{}'.format(extension), bot)
    bot.run(TOKEN)
   


if __name__ == '__main__':
    main()
