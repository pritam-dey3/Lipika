import logging
from typing import Callable

from bot.bot import Bot
from bot.exts import exts_all, exts_tools
from discord.ext.commands import Cog, Context, command, is_owner  # type: ignore

log = logging.getLogger(__name__)

exts = {ext: val for ext, val in exts_all.items() if ext not in exts_tools}


class ExtLoader(Cog):
    """Load, unload, reload any extensions (excluding tools)."""

    def __init__(self, bot: Bot) -> None:
        super().__init__()
        self.bot = bot

    def apply(self, module_name: str, func: Callable) -> None:
        """Apply `func` to the `module_name` extension.

        If module_name belongs to `tools/` then it is ignored

        Args:
            module_name (str): Name of the extension file.
            func (Callable): Function to be applied for the given `module_name`
        """
        try:
            module = exts[module_name]
            func(module)
        except KeyError:
            msg = f"{module_name} is not an extension"
            log.warning(msg)
            print(msg)
        except Exception as e:
            print(f"Unknown error occured while loading module: {module_name}")
            print(type(e).__name__, e)

    @command(name="load")
    @is_owner()
    async def load_command(self, ctx: Context, module_name: str) -> None:
        """Load `module_name` extension. If `module_name=*` then load all extensions.

        Ignote if `module_name` belongs to tools.
        """
        if module_name == "*":
            for ext in exts:
                self.apply(ext, self.bot.load_extension)
        else:
            self.apply(module_name, self.bot.load_extension)

    @command(name="unload")
    @is_owner()
    async def unload_command(self, ctx: Context, module_name: str) -> None:
        """Unload `module_name`.

        If `module_name=*` then unload all module except tools
        """
        if module_name == "*":
            for ext in exts:
                self.apply(ext, self.bot.unload_extension)
        else:
            self.apply(module_name, self.bot.unload_extension)

    @command(name="reload", aliases=["rl"])
    @is_owner()
    async def reload_command(self, ctx: Context, module_name: str) -> None:
        """Reload `module_name`."""
        if module_name == "*":
            for ext in exts:
                self.apply(ext, self.bot.reload_extension)
        else:
            self.apply(module_name, self.bot.reload_extension)


def setup(bot: Bot) -> None:
    """Add `ExtLoader` to bot."""
    bot.add_cog(ExtLoader(bot))
