"""This cog simulates a coin-flip. The user can also predict the flipped side."""

import random

from bot.bot import Bot
from bot.constants import Emojis
from discord.ext import commands  # type: ignore


class CoinSide(commands.Converter):
    """Class used to convert the `side` parameter of coinflip command."""

    HEADS = ("h", "head", "heads")
    TAILS = ("t", "tail", "tails")

    async def convert(self, ctx: commands.Context, side: str) -> str:
        """Convert the provided `side` into the corresponding string."""
        side = side.lower()
        if side in self.HEADS:
            return "Heads"

        if side in self.TAILS:
            return "Tails"

        raise commands.BadArgument(f"{side!r} is not a valid coin side.")


class CoinFlip(commands.Cog):
    """Cog for the CoinFlip command."""

    @commands.command(name="coinflip", aliases=("flip", "coin", "cf"))
    async def coinflip_command(
        self, ctx: commands.Context, side: CoinSide = None
    ) -> None:
        """Flip a coin.

        If `side` is provided will state whether you guessed the side correctly.
        """
        flipped_side = random.choice(["Heads", "Tails"])

        message = f"{ctx.author.mention} flipped **{flipped_side}**. "
        if not side:
            await ctx.send(message)
            return

        if side == flipped_side:
            message += f"You guessed correctly! {Emojis.hyperpleased}"
        else:
            message += f"You guessed incorrectly. {Emojis.pensive}"
        await ctx.send(message)


def setup(bot: Bot) -> None:
    """Load the coinflip cog."""
    bot.add_cog(CoinFlip())
