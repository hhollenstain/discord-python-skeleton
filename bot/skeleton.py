import discord
import logging
import os
import asyncio
import aiohttp
import json
from discord.ext.commands import Bot

log = logging.getLogger('discord')

class SkeletonBot(discord.ext.commands.Bot):
    """A modified discord.Client class

    This mod dispatches most events to the different plugins.

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app_id = kwargs.get('app_id')