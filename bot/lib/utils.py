import asyncio
import argparse
import discord
import logging
import os
from discord import Game
from discord.ext import commands
from itertools import cycle, islice
""" AC Imports """
from bot import VERSION

LOG = logging.getLogger(__name__)
BLOCKED_USERS = os.getenv('BLOCKED_USERS') or '123456'

def parse_arguments():
    """parsing arguments.

    """
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--debug', help='enable debug', action='store_true')
    parser.add_argument('--version', action='version',
                        version=format(VERSION),
                        help='show the version number and exit')

    return parser.parse_args()

def block_check():
    """[summary]
    
    Returns:
        [type] -- [description]
    """
    def predicate(ctx):
        if str(ctx.message.author.id) in BLOCKED_USERS:
            return False
        else:
            return True
    return commands.check(predicate)

async def change_status(client):
    """[summary]
    
    Arguments:
        client {[type]} -- [description]
    """
    await client.wait_until_ready()

    if os.environ.get('GAMES') is not None:
        GAMES = os.environ.get('GAMES').split(",")
        sts = cycle(GAMES)

        while not client.is_closed():
            current_status = next(sts)
            await client.change_presence(status=discord.Status.online, activity=Game(name=current_status))
            await asyncio.sleep(300)
    else:
        while not client.is_closed():
            guild_count = len(client.guilds)
            current_status = 'Serving {} Discord servers!'.format(guild_count)
            await client.change_presence(status=discord.Status.online, activity=Game(name=current_status))
            await asyncio.sleep(300)


async def list_servers(client):
    """[summary]
    
    Arguments:
        client {[type]} -- [description]
    """
    await client.wait_until_ready()
    while not client.is_closed():
        server_list = []
        for server in client.guilds:
            server_list.append(server.name)
        LOG.info(f'Current servers: {server_list}')
        await asyncio.sleep(600)

async def list_users(client):
    """[summary]
    
    Arguments:
        client {[type]} -- [description]
    """
    await client.wait_until_ready()
    while not client.is_closed():
        numb_of_clients = len(set(client.get_all_members()))
        LOG.info(f'Number Of clients: {numb_of_clients}')
        await asyncio.sleep(600)
