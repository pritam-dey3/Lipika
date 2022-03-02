import asyncio
from collections import defaultdict

from bot.bot import Bot
from bot.database import Note as DbNote
from discord import Embed, Message
from discord.abc import User
from discord.ext.commands import Cog, Context, command, is_owner  # type: ignore
from discord.ext.pages import Paginator  # type: ignore
from sqlalchemy import delete, desc


class Note(Cog):
    def __init__(self, bot: Bot) -> None:
        super().__init__()
        self.bot = bot
        self.info: dict[User, dict[str, str]] = defaultdict(
            lambda: {"title": "", "body": ""}
        )

    @command(name="note", aliases=["n", "nt"])
    async def note_start(self, ctx: Context, *title_: str) -> None:
        """Command to start of a note."""
        note = DbNote(
            user=ctx.message.author.id,
            title="",
            body="",
            channel_id=ctx.message.channel.id,
        )
        if title_:
            title = " ".join(title_)
            note.title = title
        while True:
            try:
                msg: Message = await self.bot.wait_for("message", timeout=60)
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

    @command(name="end_note", aliases=[".", "ent"])
    async def note_end(self, ctx: Context, *args: str) -> None:
        """Save note started by the author."""
        pass

    @command(name="see_all_notes", aliases=["nalll"])
    @is_owner()
    async def see_all(self, ctx: Context, *args: str) -> None:
        """Command to view all the notes."""
        with self.bot.Sess() as sess:
            notes = sess.query(DbNote).order_by(desc(DbNote.date_time)).all()
        paginator = self.annotate_notes(notes, add_user=True)
        await paginator.send(ctx)

    @command(name="see_all_user_notes", aliases=["nall"])
    async def see_all_user(self, ctx: Context, *args: str) -> None:
        """Command to view all the notes."""
        with self.bot.Sess() as sess:
            notes = (
                sess.query(DbNote)
                .order_by(desc(DbNote.date_time))
                .where(DbNote.user == ctx.message.author.id)
            )
        paginator = self.annotate_notes(notes)
        await paginator.send(ctx)

    def annotate_notes(self, notes: list[DbNote], add_user: bool = False) -> Paginator:
        """Annotate a list of notes and return Paginator for all of them."""
        n = 0
        pages = []
        txt = ""
        for note in notes:
            n += 1
            txt += (
                f"{note.id}."
                f"**{note.title}**"
                f"\t`{note.date_time.strftime('%d %b, %Y - %H:%m')}`"
            )
            if add_user:
                txt += f"\t::{note.user}"
            txt += f"\n{note.body}\n"
            if n % 4 == 0:
                emb = Embed(title="All notes", description=txt)
                pages.append(emb)
                txt = ""
        emb = Embed(title="All notes", description=txt)
        pages.append(emb)
        paginator = Paginator(pages)
        return paginator

    @command(name="note_delete", aliases=["ndel"])
    async def note_delete(self, ctx: Context, nid: int) -> None:
        """Delete a note by id."""
        with self.bot.Sess() as sess:
            stmt = delete(DbNote).where(DbNote.id == nid)
            sess.execute(stmt)
            sess.commit()


def setup(bot: Bot) -> None:
    """Add Note cog to bot."""
    bot.add_cog(Note(bot))
