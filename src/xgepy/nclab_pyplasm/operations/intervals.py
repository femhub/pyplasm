"""
Intervals Operations Module
"""

from nclab.tools import ExceptionWT
from ..geometry.base import BASEOBJ
from ...fenvs import PLASM_INTERVALS

__all__ = [
    "intervals",
    "INTERVALS",
    "DIVISION",
    # Language variants
    "DELENI",
    "INTERVALY",  # Czech
    "DZIELENIE",
    "INTERWALY",  # Polish
    "INTERVALLE",
    "AUFTEILEN",
    "AUFSPALTEN",  # German
    "DIVISION",  # Spanish
    "DIVISION",
    "DIVISIONE",  # Italian
    "DIVISION",  # French
]


def intervals(*args):
    raise ExceptionWT("Command intervals() is undefined. Try INTERVALS() instead?")


def INTERVALS(a, n):
    return BASEOBJ(PLASM_INTERVALS(a)(n))


# English:
DIVISION = INTERVALS

# Czech:
DELENI = INTERVALS
INTERVALY = INTERVALS

# Polish:
DZIELENIE = INTERVALS
INTERWALY = INTERVALS

# German:
INTERVALLE = INTERVALS
AUFTEILEN = INTERVALS
AUFSPALTEN = INTERVALS

# Spanish:
DIVISION = INTERVALS

# Italian:
DIVISION = INTERVALS
DIVISIONE = INTERVALS

# French:
DIVISION = INTERVALS
