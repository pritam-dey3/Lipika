import importlib
import inspect
import logging
import pkgutil
from typing import Iterator, NoReturn

log = logging.getLogger(__name__)


def unqualify(name: str) -> str:
    """Return an unqualified name given a qualified module/package `name`."""
    return name.rsplit(".", maxsplit=1)[-1]


exts_all: dict[str, str] = {}
exts_tools: set[str] = set()
def walk_extensions() -> Iterator[str]:
    """Yield extension names from the bot.exts subpackage."""

    def on_error(name: str) -> NoReturn:
        raise ImportError(name=name)  # pragma: no cover

    for module in pkgutil.walk_packages(__path__, f"{__name__}.", onerror=on_error):
        if unqualify(module.name).startswith("_"):
            # Ignore module/package names starting with an underscore.
            continue

        if module.ispkg:
            imported = importlib.import_module(module.name)
            if not inspect.isfunction(getattr(imported, "setup", None)):
                # If it lacks a setup function, it's not an extension.
                continue

        # update global dictionary of extensions
        exts_all[unqualify(module.name)] = module.name
        if "tools" in module.name:
            exts_tools.add(unqualify(module.name))

        yield module.name

