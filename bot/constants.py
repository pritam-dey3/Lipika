"""This file contains all required constants."""

import os
from dataclasses import dataclass
from typing import NamedTuple

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    """Configuration settings."""

    name: str = "Lipika"
    guild: int = int(os.getenv("BOT_GUILD", 267624335836053506))
    prefix: str = os.getenv("PREFIX", ".")
    token: str = os.getenv("BOT_TOKEN")


class Roles(NamedTuple):
    """Available roles in the guild."""

    owners: int = 267627879762755584
    moderation_team: int = 267629731250176001
    friends: int = 587606783669829632
    everyone: int = Config.guild


MODERATION_ROLES = {Roles.moderation_team, Roles.owners}


@dataclass
class Emojis:
    """Emojis to reuse in different cogs and extensions."""

    cross_mark = "\u274C"
    star = "\u2B50"
    christmas_tree = "\U0001F384"
    check = "\u2611"
    envelope = "\U0001F4E8"
    trashcan = "trash"
    ok_hand = ":ok_hand:"
    hand_raised = "\U0001F64B"

    # These icons are from Github's repo https://github.com/primer/octicons/
    # issue_open = "<:IssueOpen:852596024777506817>"
    # issue_closed = "<:IssueClosed:852596024739758081>"
    # # Not currently used by Github, but here for future.
    # issue_draft = "<:IssueDraft:852596025147523102>"
    # pull_request_open = "<:PROpen:852596471505223781>"
    # pull_request_closed = "<:PRClosed:852596024732286976>"
    # pull_request_draft = "<:PRDraft:852596025045680218>"
    # pull_request_merged = "<:PRMerged:852596100301193227>"

    number_emojis = {
        1: "\u0031\ufe0f\u20e3",
        2: "\u0032\ufe0f\u20e3",
        3: "\u0033\ufe0f\u20e3",
        4: "\u0034\ufe0f\u20e3",
        5: "\u0035\ufe0f\u20e3",
        6: "\u0036\ufe0f\u20e3",
        7: "\u0037\ufe0f\u20e3",
        8: "\u0038\ufe0f\u20e3",
        9: "\u0039\ufe0f\u20e3",
    }

    confirmation = "\u2705"
    decline = "\u274c"
    incident_unactioned = "incident_unactioned_emj"

    x = "<:cross_err:946786944329859072>"
    o = "\U0001f1f4"
    check = "<:check:946786323933593660>"

    x_square = "x_square"
    o_square = "o_square"

    status_online = "online"
    status_idle = "idle"
    status_dnd = "dnd"
    status_offline = "offline"

    stackoverflow_tag = "stov_tag"
    stackoverflow_views = "stov_view"

    hyperpleased = "<:8210_kirbyblob:921796114380894258>"
    pensive = ":pensive:"
