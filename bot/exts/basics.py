"""Some basic simple commands."""

import random

from bot.bot import Bot
from discord.ext.commands import Cog, Context, command  # type: ignore


class BasicCommands(Cog):
    """Some simple commands."""

    @command()
    async def add(self, ctx: Context, left: int, right: int) -> None:
        """Add two numbers together."""
        await ctx.send(left + right)

    @command()
    async def roll(self, ctx: Context, dice: str) -> None:
        """Roll a dice in NdN format."""
        try:
            rolls, limit = map(int, dice.split("d"))
        except Exception:
            await ctx.send("Format has to be in NdN!")
            return None

        result = ", ".join(str(random.randint(1, limit)) for r in range(rolls))
        await ctx.send(result)

    @command()
    async def choose(self, ctx: Context, *choices: str) -> None:
        """Chooses between multiple choices."""
        await ctx.send(random.choice(choices))

    # @user_command(
    #     guild_ids=[Client.guild]
    # )  # create a user command for the supplied guilds
    # async def mention(ctx: Context, member: Member): # user commands return the member
    #     await ctx.respond(f"{ctx.author.name} just mentioned {member.mention}!")


def setup(bot: Bot) -> None:
    """Add extension to bot."""
    bot.add_cog(BasicCommands())
