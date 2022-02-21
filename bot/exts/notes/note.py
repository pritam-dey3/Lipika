import asyncio
from collections import defaultdict

from bot.bot import Bot
from bot.database import Note as DbNote
from discord import Message
from discord.abc import User
from discord.ext.commands import Cog, Context, command  # type: ignore


class Note(Cog):
    def __init__(self, bot: Bot) -> None:
        super().__init__()
        self.bot = bot
        self.info: dict[User, dict[str, str]] = defaultdict(
            lambda: {"title": "", "body": ""}
        )

    @command(name="note", aliases=["n", "nt"])
    async def note_start(self, ctx: Context, title: str) -> None:
        """Command to start of a note."""
        note = DbNote(
            user=ctx.message.author.id,
            title="",
            body="",
            channel_id=ctx.message.channel.id,
        )
        if title:
            note.title = title
        while True:
            try:
                msg: Message = await self.bot.wait_for("message", timeout=6)
            except asyncio.TimeoutError:
                break
            ctx2: Context = await self.bot.get_context(msg)
            if ctx2.valid:
                break
            else:
                note.body += msg.content + "\n"
        sess = self.bot.Sess()
        sess.add(note)
        sess.commit()
        await ctx.send(note.__repr__())

    @command(name="end_note", aliases=[".", "ent"])
    async def note_end(self, ctx: Context, *args: str) -> None:
        """Save note started by the author."""
        await ctx.send(self.info.__repr__())
        pass


def setup(bot: Bot) -> None:
    """Add Note cog to bot."""
    bot.add_cog(Note(bot))
