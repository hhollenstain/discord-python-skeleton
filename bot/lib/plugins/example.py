import discord
import logging
import random
from discord.ext import commands
from bot.lib import utils

LOG = logging.getLogger(__name__)

class Example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='8ball',
                    description="Answers a yes/no question.",
                    brief="Answers from the beyond.",
                    aliases=['eight_ball', 'eightball', '8-ball'],
                    pass_context=True)
    @utils.block_check()
    async def eight_ball(self, ctx):
        possible_responses = [
            'That is a resounding no',
            'It is not looking likely',
            'Too hard to tell',
            'It is quite possible',
            'Definitely',
        ]
        await ctx.send('{}, {}'.format(random.choice(possible_responses),
                                       ctx.message.author.mention))

    @commands.command(pass_context=True)
    async def hello(self, ctx):
        await ctx.send('Hello {}'.format(ctx.message.author.mention))

    async def on_message(self, message):
        if message.author == self.bot.user:
            return

    
    @commands.command()
    @utils.block_check()
    async def ping(self, ctx):
        await ctx.send('Pong')

def setup(bot):
   bot.add_cog(Example(bot))
