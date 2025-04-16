"""
Brick Creation Module

This module provides functions for creating brick objects with rounded corners in 3D space.
The BRICK function creates a rectangular prism with optional rounded edges using a specified
radius.
"""

from nclab.tools import ExceptionWT
from ..utils.common import ISNUMBER
from ..utils.constants import X, Y, Z
from ..geometry.prism import PRISM
from ..geometry.rectangle import RECTANGLE
from ..geometry.sphere import SPHERE
from ..operations.move import MOVE
from ..operations.rotate import ROTATE
from ..operations.copy_objects import COPY
from ..operations.erase import ERASE
from ..operations.weld import WELD
from .box import BOX


def brick(*args):
    raise ExceptionWT("Command brick() is undefined. Try BRICK() instead?")


def BRICK(a, b, c, r=0):
    if not ISNUMBER(a):
        raise ExceptionWT("Size a in BRICK(a, b, c, r=0) must be a number!")
    if not ISNUMBER(b):
        raise ExceptionWT("Size b in BRICK(a, b, c, r=0) must be a number!")
    if not ISNUMBER(c):
        raise ExceptionWT("Size c in BRICK(a, b, c, r=0) must be a number!")
    if a <= 0:
        raise ExceptionWT("Size a in BRICK(a, b, c, r=0) must be positive!")
    if b <= 0:
        raise ExceptionWT("Size b in BRICK(a, b, c, r=0) must be positive!")
    if c <= 0:
        raise ExceptionWT("Size c in BRICK(a, b, c, r=0) must be positive!")
    if not ISNUMBER(r):
        raise ExceptionWT("Radius r in BRICK(a, b, c, r=0) must be a number!")
    if r < -1e-10:
        raise ExceptionWT("Radius r in BRICK(a, b, c, r=0) must be positive!")
    m = min(a, b, c)
    if r > 0.5 * m:
        raise ExceptionWT("Radius r in BRICK(a, b, c, r=0) too large!")
    if abs(r) < 1e-10:
        return BOX(a, b, c)
    else:
        if r < a - r:
            o1 = PRISM(RECTANGLE(c, b, r), a - 2 * r)
            MOVE(o1, -c, 0, 0)
            ROTATE(o1, 90, Y)
            MOVE(o1, r, 0, 0)
        else:
            o1 = []
        if r < b - r:
            o2 = PRISM(RECTANGLE(a, c, r), b - 2 * r)
            MOVE(o2, 0, -c, 0)
            ROTATE(o2, -90, X)
            MOVE(o2, 0, r, 0)
        else:
            o2 = []
        if r < c - r:
            o3 = PRISM(RECTANGLE(a, b, r), c - 2 * r)
            MOVE(o3, 0, 0, r)
        else:
            o3 = []
        c1 = SPHERE(r)
        c5 = COPY(c1)
        ERASE(c1, -2 * r, 0, Z)
        ERASE(c1, -2 * r, 0, Y)
        ERASE(c1, -2 * r, 0, X)
        c2 = COPY(c1)
        MOVE(c1, a - r, b - r, c - r)
        ROTATE(c2, 90, Z)
        c3 = COPY(c2)
        MOVE(c2, r, b - r, c - r)
        ROTATE(c3, 90, Z)
        c4 = COPY(c3)
        MOVE(c3, r, r, c - r)
        ROTATE(c4, 90, Z)
        MOVE(c4, a - r, r, c - r)
        ROTATE(c5, 90, Y)
        ERASE(c5, 0, 2 * r, Z)
        ERASE(c5, -2 * r, 0, Y)
        ERASE(c5, -2 * r, 0, X)
        c6 = COPY(c5)
        MOVE(c5, a - r, b - r, r)
        ROTATE(c6, 90, Z)
        c7 = COPY(c6)
        MOVE(c6, r, b - r, r)
        ROTATE(c7, 90, Z)
        c8 = COPY(c7)
        MOVE(c7, r, r, r)
        ROTATE(c8, 90, Z)
        MOVE(c8, a - r, r, r)
        return WELD(o1, o2, o3, c1, c2, c3, c4, c5, c6, c7, c8)


# English:
BRICK = BRICK

# Czech:
KVADR = BRICK
CIHLA = BRICK

# Polish:
PUDEŁKO = BRICK
CEGŁA = BRICK

# German:
KASTEN = BRICK
SCHACHTEL = BRICK  # Also means "box"

# Spanish:
BLOQUE = BRICK

# Italian:
COTTO = BRICK  # Refers to terracotta (baked clay)
SCATOLA = BRICK  # Box
MATTONE = BRICK  # Common word for brick
LATERIZIO = BRICK  # General term for brickwork
PARALLELEPIPEDO = BRICK  # Geometric term

# French:
BRIQUE = BRICK
BOÎTE = BRICK  # Box

__all__ = [
    "brick",
    "BRICK",  # English
    "KVADR",
    "CIHLA",  # Czech
    "PUDEŁKO",
    "CEGŁA",  # Polish
    "KASTEN",
    "SCHACHTEL",  # German
    "BLOQUE",  # Spanish
    "COTTO",
    "SCATOLA",
    "MATTONE",
    "LATERIZIO",
    "PARALLELEPIPEDO",  # Italian
    "BRIQUE",
    "BOÎTE",  # French
]
