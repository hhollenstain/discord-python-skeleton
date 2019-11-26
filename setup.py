"""``discord-python-skeleton`` lives on
https://github.com/hhollenstain/discord-python-skeleton
"""
from setuptools import setup, find_packages
import bot

INSTALL_REQUIREMENTS = [
    'asyncio',
    'coloredlogs',
    'discord.py==1.2.5',
    'pip==18.0',
]

TEST_REQUIREMENTS = {
    'test':[
        'pytest',
        'pylint',
        'sure',
        ]
    }

setup(
    name='discord-python-skeleton',
    version=bot.VERSION,
    description='Python Discord Bot skeleton',
    url='https://github.com/hhollenstain/discord-python-skeleton',
    packages=find_packages(),
    include_package_data=True,
    install_requires=INSTALL_REQUIREMENTS,
    extras_require=TEST_REQUIREMENTS,
    entry_points={
        'console_scripts':  [
            'bot = bot.bot:main',
        ],
    },
    )
