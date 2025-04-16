"""
Square Operations Module

This module provides functions for creating 2D and 3D square objects with multilingual support.
"""

from nclab.tools import ExceptionWT
from ..geometry.base import BASEOBJ
from ..geometry.rectangle import RECTANGLE
from ...fenvs import CUBOID


def square(*args):
    raise ExceptionWT("Command square() is undefined. Try SQUARE() instead?")


def SQUARE(size, r=0):
    return RECTANGLE(size, size, r)


# English:
SQUARE = SQUARE

# Czech:
ČTVEREC = SQUARE

# Polish:
KWADRAT = SQUARE

# German:
QUADRAT = SQUARE

# Spanish:
CUADRO = SQUARE

# Italian:
QUADRATO = SQUARE

# French:
CARRÉ = SQUARE


def square3d(*args):
    raise ExceptionWT("Command square3d() is undefined. Try SQUARE3D() instead?")


def SQUARE3D(a):
    if a <= 0:
        raise ExceptionWT("SQUARE3D(x) requires a positive value of x!")
    # height is kept the same for add these thin objects,
    # so that logical operations with them work:
    h = 0.001
    return BASEOBJ(CUBOID([a, a, h]))


# English:
SQUARE3D = SQUARE3D

# Czech:
ČTVEREC3D = SQUARE3D

# Polish:
KWADRAT3D = SQUARE3D

# German:
QUADRAT3D = SQUARE3D

# Spanish:
CUADRO3D = SQUARE3D

# Italian:
QUADRATO3D = SQUARE3D

# French:
CARRÉ3D = SQUARE3D


__all__ = [
    "square",
    "SQUARE",  # English
    "ČTVEREC",  # Czech
    "KWADRAT",  # Polish
    "QUADRAT",  # German
    "CUADRO",  # Spanish
    "QUADRATO",  # Italian
    "CARRÉ",  # French
    "square3d",
    "SQUARE3D",  # English 3D
    "ČTVEREC3D",  # Czech 3D
    "KWADRAT3D",  # Polish 3D
    "QUADRAT3D",  # German 3D
    "CUADRO3D",  # Spanish 3D
    "QUADRATO3D",  # Italian 3D
    "CARRÉ3D",  # French 3D
]
