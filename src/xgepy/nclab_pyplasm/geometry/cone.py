"""
Cone Geometry Module
"""

__all__ = [
    "cone",
    "CONE",
    # Language variants
    "KUZEL",  # Czech
    "STOZEK",  # Polish
    "KEGEL",  # German
    "CONO",  # Spanish
    "CONO",  # Italian
    "CONE",  # French
]

from nclab.tools import ExceptionWT
from ..utils.common import ISNUMBER
from ..geometry.base import BASEOBJ
from ...fenvs import PLASM_CONE


def cone(*args):
    raise ExceptionWT("Command cone() is undefined. Try CONE() instead?")


def CONE(r, h, division=48):
    if not ISNUMBER(r):
        raise ExceptionWT("Radius r in CONE(r, h) must be a number!")
    if not ISNUMBER(h):
        raise ExceptionWT("Height h in CONE(r, h) must be a number!")
    if r <= 0:
        raise ExceptionWT("Radius r in CONE(r, h) must be positive!")
    if h <= 0:
        raise ExceptionWT("Height h in CONE(r, h) must be positive!")
    if division < 3:
        raise ExceptionWT("Number of sides n in CONE(r, h, n) must be at least 3!")
    return BASEOBJ(PLASM_CONE([r, h])(division))


# Czech:
KUZEL = CONE  # cone

# Polish:
STOZEK = CONE  # cone

# German:
KEGEL = CONE  # cone

# Spanish:
CONO = CONE  # cone

# Italian:
CONO = CONE  # same as Spanish

# French:
CONE = CONE  # same as English
