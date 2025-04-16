"""
Torus Geometry Module
"""

from nclab.tools import ExceptionWT
from ..utils.common import ISNUMBER
from ..geometry.base import BASEOBJ
from ...fenvs import PLASM_TORUS, PLASM_SOLIDTORUS

__all__ = [
    "TORUS_SURFACE",
    "torus",
    "TORUS",
    "DONUT",
    # Language variants
    "TORUS",  # Czech
    "TORUS",  # Polish
    "TORUS",  # German
    "TORO",  # Spanish
    "TORO",  # Italian
    "TORE",  # French
]


def TORUS_SURFACE(r1, r2, divisions=[32, 16]):
    if r1 <= 0:
        raise ExceptionWT("Inner radius r1 in TORUS_SURFACE(r1, r2) must be positive!")
    if r2 <= 0:
        raise ExceptionWT("Outer radius r2 in TORUS_SURFACE(r1, r2) must be positive!")
    if r2 <= r1:
        raise ExceptionWT(
            "Inner radius r1 must be smaller than outer radius r2 in TORUS_SURFACE(r1, r2)!"
        )
    return BASEOBJ(PLASM_TORUS([r1, r2])(divisions))


def torus(*args):
    raise ExceptionWT("Command torus() is undefined. Try TORUS() instead?")


def TORUS(r1, r2, divisions=[32, 16]):
    if not ISNUMBER(r1):
        raise ExceptionWT("Inner radius r1 in TORUS(r1, r2) must be a number!")
    if not ISNUMBER(r2):
        raise ExceptionWT("Outer radius r2 in TORUS(r1, r2) must be a number!")
    if r1 <= 0:
        raise ExceptionWT("Inner radius r1 in TORUS(r1, r2) must be positive!")
    if r2 <= 0:
        raise ExceptionWT("Outer radius r2 in TORUS(r1, r2) must be positive!")
    if r2 <= r1:
        raise ExceptionWT(
            "Inner radius r1 must be smaller than outer radius r2 in TORUS(r1, r2)!"
        )
    divisionslist = divisions
    if not isinstance(divisions, list):
        if divisions / 2 <= 0:
            raise ExceptionWT("Bad division in the TORUS command!")
        divisionslist = [divisions, int(divisions / 2)]
    return BASEOBJ(PLASM_SOLIDTORUS([r1, r2])([divisionslist[0], divisionslist[1], 1]))


# English:
DONUT = TORUS  # colloquial term

# Czech:
TORUS = TORUS  # same as English

# Polish:
TORUS = TORUS  # same as English

# German:
TORUS = TORUS  # same as English

# Spanish:
TORO = TORUS  # torus

# Italian:
TORO = TORUS  # same as Spanish

# French:
TORE = TORUS  # torus
