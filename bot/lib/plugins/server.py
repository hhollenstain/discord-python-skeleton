import discord
import logging
import random
from discord import Game
from discord.ext import commands
""" AC imports """ 
from bot import VERSION
from bot.lib import utils

LOG = logging.getLogger(__name__)

class Server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        LOG.info('Logged in as {}'.format(self.bot.user.name))
        await self.bot.change_presence(status=discord.Status.online, activity=Game('Waking up, making coffee...'))
        self.bot.loop.create_task(utils.change_status(self.bot))
        self.bot.loop.create_task(utils.list_servers(self.bot))
        self.bot.loop.create_task(utils.list_users(self.bot))

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            LOG.error(error)
            msg = '{} Error running the command'.format(ctx.message.author.mention)
        if isinstance(error, commands.CommandNotFound):
            msg = '{} the command you ran does not exist please use !help for assistance'.format(ctx.message.author.mention)
        if isinstance(error, commands.CheckFailure):
            msg = ':octagonal_sign: you do not have permission to run this command, {}'.format(ctx.message.author.mention)
        if isinstance(error, commands.MissingRequiredArgument):
            msg = 'Missing required argument: ```{}```'.format(error)

        if not msg:
            msg = 'Oh no, I have no idea what I am doing! {}'.format(error)


        await ctx.send('{}'.format(msg))

    @commands.command(aliases=['bot'])
    async def info(self, ctx):
        """
        Information about what makes the bot run!
        """
        embed = discord.Embed(
            description = 'Bot information',
            colour = discord.Colour.green()
        )
        
        """Link to your bots avatar"""
        #avatar = ""
        embed.set_author(name='Bot')
        #embed.set_thumbnail(url=avatar)
        embed.add_field(name='description', value=f'Skeleton bot please update for your own use', inline=True)
        # embed.add_field(name='Source Code', value=f'Want to see what makes me run? [Source Code Here!](https://github.com/hhollenstain/discord-python-bot)', inline=True)
        embed.add_field(name='Version', value=VERSION, inline=True)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Server(bot))
