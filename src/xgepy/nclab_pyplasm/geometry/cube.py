"""
Cube Creation Module

This module provides functions for creating cube objects with optional rounded corners.
The CUBE function creates a 3D cube with specified size and optional corner radius.
"""

from nclab.tools import ExceptionWT
from ..utils.common import ISNUMBER
from ..geometry.base import BASEOBJ
from ..geometry.brick import BRICK
from ...fenvs import CUBOID


def cube(*args):
    raise ExceptionWT("Command cube() is undefined. Try CUBE() instead?")


def CUBE(size, r=0):
    if not ISNUMBER(size):
        raise ExceptionWT("Size s in CUBE(s, r=0) must be a number!")
    if size <= 0:
        raise ExceptionWT("Size s in CUBE(s, r=0) must be positive!")
    if not ISNUMBER(r):
        raise ExceptionWT("Radius r in CUBE(s, r=0) must be a number!")
    if r < -1e-10:
        raise ExceptionWT("Radius r in CUBE(s, r=0) must be positive!")
    if r > 0.5 * size:
        raise ExceptionWT("Radius r in CUBE(s, r=0) must be less than or equal to s/2!")
    if abs(r) < 1e-10:
        return BASEOBJ(CUBOID([size, size, size]))
    else:
        return BRICK(size, size, size, r)


# English:
CUBE = CUBE
# Czech:
KRYCHLE = CUBE
KOSTKA = CUBE

# Polish:
SZEŚCIAN = CUBE

# German:
WÜRFEL = CUBE
WUERFEL = CUBE  # Alternative spelling without umlaut

# Spanish:
CUBO = CUBE

# Italian:
CUBO = CUBE  # Same as Spanish

# French:
CUBE = CUBE  # Same as English

__all__ = [
    "cube",
    "CUBE",
    "KRYCHLE",
    "KOSTKA",  # Czech
    "SZEŚCIAN",  # Polish
    "WÜRFEL",
    "WUERFEL",  # German
    "CUBO",  # Spanish
    "CUBO",  # Italian
    "CUBE",  # French
]
