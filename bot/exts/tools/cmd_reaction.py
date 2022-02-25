from bot.bot import Bot
from bot.constants import Emojis
from discord.ext.commands import Cog, Context, command  # type: ignore


class CmdReact(Cog):
    """React emojis when a command is invoked showing success/failure of command."""

    @Cog.listener()
    async def on_command_completion(self, ctx: Context) -> None:
        """Add :check: if there are no errors during invokation of the command."""
        await ctx.message.add_reaction(Emojis.check)

    @Cog.listener()
    async def on_command_error(self, ctx: Context, error: Exception) -> None:
        """Add :check: if there are no errors during invokation of the command."""
        await ctx.message.add_reaction(Emojis.x)
        raise error

    @command(name="test_err")
    async def test_err(self, ctx: Context) -> None:
        """Simple command to raise an error."""
        raise Exception("test exception")


def setup(bot: Bot) -> None:
    """Add `ExtLoader` to bot."""
    bot.add_cog(CmdReact())
