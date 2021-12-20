import logging
from os import path
import random

import discord
from discord.ext import commands  # type: ignore

logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename=".logs/discord.log", encoding="utf-8", mode="w")
handler.setFormatter(
    logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
)
logger.addHandler(handler)

bot_description = """\
Lipika is a personal assistant bot created by Pritam Dey to automate some \
day to day tasks.
"""


class Bot(commands.Bot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.command_prefix = "."
        self.description = bot_description
