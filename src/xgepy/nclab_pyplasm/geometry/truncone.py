"""
Truncated Cone Geometry Module
"""

from nclab.tools import ExceptionWT
from ..utils.common import ISNUMBER
from ..geometry.base import BASEOBJ
from ...fenvs import PLASM_JOIN, PLASM_TRUNCONE

__all__ = [
    "tcone",
    "truncone",
    "TCONE",
    "TRUNCONE",
    # Language variants
    "KOMOLYKUZEL",
    "KKUZEL",  # Czech
    "SCIETYSTOZEK",
    "SSTOZEK",  # Polish
    "KEGELSTUMPF",
    "KSTUMPF",  # German
    "CONOTRUNCADO",
    "TRUNCONO",
    "TCONO",  # Spanish
    "TRONCONO",
    "TCONO",  # Italian
    "TRONCONE",  # French
]


def tcone(*args):
    raise ExceptionWT("Command tcone() is undefined. Try TCONE() instead?")


def truncone(*args):
    raise ExceptionWT("Command truncone() is undefined. Try TRUNCONE() instead?")


def TCONE(r1, r2, h, divisions=48):
    if not ISNUMBER(r1):
        raise ExceptionWT("Bottom radius r1 in TCONE(r1, r2, h) must be a number!")
    if not ISNUMBER(r2):
        raise ExceptionWT("Top radius r2 in TCONE(r1, r2, h) must be a number!")
    if not ISNUMBER(h):
        raise ExceptionWT("Height h in TCONE(r1, r2, h) must be a number!")
    if not ISNUMBER(h):
        raise ExceptionWT("Height h in CYLINDER(r, h) must be a number!")
    if r1 <= 0:
        raise ExceptionWT("Bottom radius r1 in TCONE(r1, r2, h) must be positive!")
    if r2 <= 0:
        raise ExceptionWT("Top radius r2 in TCONE(r1, r2, h) must be positive!")
    if h <= 0:
        raise ExceptionWT("Height h in TCONE(r1, r2, h) must be positive!")
    if divisions < 3:
        raise ExceptionWT(
            "Number of sides n in TCONE(r1, r2, h, n) must be at least 3!"
        )
    # Changing to a solid:
    return BASEOBJ(PLASM_JOIN(PLASM_TRUNCONE([r1, r2, h])(divisions)))


# English:
TRUNCONE = TCONE  # truncated cone

# Czech:
KOMOLYKUZEL = TRUNCONE  # truncated cone
KKUZEL = TRUNCONE  # short form

# Polish:
SCIETYSTOZEK = TRUNCONE  # truncated cone
SSTOZEK = TRUNCONE  # short form

# German:
KEGELSTUMPF = TRUNCONE  # truncated cone
KSTUMPF = TRUNCONE  # short form

# Spanish:
CONOTRUNCADO = TRUNCONE  # truncated cone
TRUNCONO = TRUNCONE  # truncated cone
TCONO = TRUNCONE  # short form

# Italian:
TRONCONO = TRUNCONE  # truncated cone
TCONO = TRUNCONE  # short form

# French:
TRONCONE = TCONE  # truncated cone
