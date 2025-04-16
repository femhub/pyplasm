"""
Pyramid Geometry Module
"""

from nclab.tools import ExceptionWT
from ..utils.common import ISNUMBER
from ..geometry.base import BASEOBJ
from ...fenvs import PLASM_CONE

__all__ = [
    "pyramid",
    "PYRAMID",
    # Language variants
    "PYRAMIDA",
    "JEHLAN",  # Czech
    "PIRAMIDA",
    "OSTROSZUP",  # Polish
    "PYRAMIDE",
    "KEGEL",  # German
    "PIRAMIDE",
    "CONO",  # Spanish
    "PIRAMIDE",
    "CONO",  # Italian
    "PYRAMIDE",
    "CONE",  # French
]


def pyramid(*args):
    raise ExceptionWT("Command pyramid() is undefined. Try PYRAMID() instead?")


def PYRAMID(r, h, n=4):
    if not ISNUMBER(r):
        raise ExceptionWT("Radius r in PYRAMID(r, h, n) must be a number!")
    if not ISNUMBER(h):
        raise ExceptionWT("Height h in PYRAMID(r, h, n) must be a number!")
    if not ISNUMBER(n):
        raise ExceptionWT("Number of sides n in PYRAMID(r, h, n) must be a number!")
    if r <= 0:
        raise ExceptionWT("Radius r in PYRAMID(r, h, n) must be positive!")
    if h <= 0:
        raise ExceptionWT("Height h in PYRAMID(r, h, n) must be positive!")
    if n < 3:
        raise ExceptionWT("Number of sides n in PYRAMID(r, h, n) must be at least 3!")
    return BASEOBJ(PLASM_CONE([r, h])(n))


# Czech:
PYRAMIDA = PYRAMID  # pyramid
JEHLAN = PYRAMID  # pyramid

# Polish:
PIRAMIDA = PYRAMID  # pyramid
OSTROSZUP = PYRAMID  # pyramid

# German:
PYRAMIDE = PYRAMID  # pyramid
KEGEL = PYRAMID  # cone

# Spanish:
PIRAMIDE = PYRAMID  # pyramid
CONO = PYRAMID  # cone

# Italian:
PIRAMIDE = PYRAMID  # pyramid
CONO = PYRAMID  # cone

# French:
PYRAMIDE = PYRAMID  # pyramid
CONE = PYRAMID  # cone
