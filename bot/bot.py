from discord.ext import commands  # type: ignore
from bot.database import Session

bot_description = """\
Lipika is a personal assistant bot created by Pritam Dey to automate some \
day to day tasks.
"""


class Bot(commands.Bot):
    def __init__(self, **kwargs: dict) -> None:
        super().__init__(**kwargs)
        self.command_prefix = "."
        self.description = bot_description
        self.Sess = Session
