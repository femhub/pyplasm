"""
Rectangle Creation Module

This module provides functions for creating 2D and 3D rectangle objects with optional rounded corners.
The module supports both 2D rectangles (RECTANGLE) and 3D thin rectangles (RECTANGLE3D) with multilingual aliases.
"""


from nclab.tools import ExceptionWT
from ..utils.common import ISNUMBER
from ..geometry.arc import ARC
from ..geometry.box import BOX
from ..geometry.base import BASEOBJ
from ..operations.move import MOVE
from ..operations.rotate import ROTATE
from ..operations.weld import WELD
from ..operations.copy_objects import COPY
from ...fenvs import CUBOID


def rectangle(*args):
    raise ExceptionWT("Command rectangle() is undefined. Try RECTANGLE() instead?")


def RECTANGLE(a, b, r=0):
    if not ISNUMBER(a):
        raise ExceptionWT("Size a in RECTANGLE(a, b, r=0) must be a number!")
    if not ISNUMBER(b):
        raise ExceptionWT("Size b in RECTANGLE(a, b, r=0) must be a number!")
    if a <= 0:
        raise ExceptionWT("Size a in RECTANGLE(a, b, r=0) must be positive!")
    if b <= 0:
        raise ExceptionWT("Size b in RECTANGLE(a, b, r=0) must be positive!")
    if not ISNUMBER(r):
        raise ExceptionWT("Radius r in RECTANGLE(a, b, r=0) must be a number!")
    if r < -1e-10:
        raise ExceptionWT("Radius r in RECTANGLE(a, b, r=0) must be positive!")
    m = min(a, b)
    if r > 0.5 * m:
        raise ExceptionWT("Radius r in RECTANGLE(a, b, r=0) too large!")
    if abs(r) < 1e-10:
        return BOX(a, b)
    else:
        if r < a - r:
            o1 = BOX(r, a - r, 0, b)
        else:
            o1 = []
        if r < b - r:
            o2 = BOX(0, a, r, b - r)
        else:
            o2 = []
        arc1 = ARC(0, r, 90, 8)
        arc2 = COPY(arc1)
        ROTATE(arc2, 90)
        arc3 = COPY(arc2)
        ROTATE(arc3, 90)
        arc4 = COPY(arc3)
        ROTATE(arc4, 90)
        MOVE(arc1, a - r, b - r)
        MOVE(arc2, r, b - r)
        MOVE(arc3, r, r)
        MOVE(arc4, a - r, r)
        return WELD(o1, o2, arc1, arc2, arc3, arc4)


# English:
RECT = RECTANGLE
RECTANGLE = RECTANGLE

# Czech:
OBDÉLNÍK = RECTANGLE

# Polish:
PROSTOKĄT = RECTANGLE

# German:
RECHTECK = RECTANGLE

# Spanish:
RECTÁNGULO = RECTANGLE

# Italian:
RETTANGOLO = RECTANGLE

# French:
RECTANGLE = RECTANGLE  # Same as in English


def rectangle3d(*args):
    raise ExceptionWT("Command rectangle3d() is undefined. Try RECTANGLE3D() instead?")


def RECTANGLE3D(a, b):
    if not ISNUMBER(a):
        raise ExceptionWT("Size a in RECTANGLE3D(a, b) must be a number!")
    if not ISNUMBER(b):
        raise ExceptionWT("Size b in RECTANGLE3D(a, b) must be a number!")
    if a <= 0:
        raise ExceptionWT("Size a in RECTANGLE3D(a, b) must be positive!")
    if b <= 0:
        raise ExceptionWT("Size b in RECTANGLE3D(a, b) must be positive!")
    # height is kept the same for add these thin objects,
    # so that logical operations with them work:
    h = 0.001
    return BASEOBJ(CUBOID([a, b, h]))


# English:
RECTANGLE3D = RECTANGLE3D

# Czech:
OBDÉLNÍK3D = RECTANGLE3D

# Polish:
PROSTOKĄT3D = RECTANGLE3D

# German:
RECHTECK3D = RECTANGLE3D

# Spanish:
RECTÁNGULO3D = RECTANGLE3D

# Italian:
RETTANGOLO3D = RECTANGLE3D

# French:
RECTANGLE3D = RECTANGLE3D  # Same as in English

__all__ = [
    "rectangle",
    "RECTANGLE",
    "RECT",  # English
    "OBDÉLNÍK",  # Czech
    "PROSTOKĄT",  # Polish
    "RECHTECK",  # German
    "RECTÁNGULO",  # Spanish
    "RETTANGOLO",  # Italian
    "RECTANGLE",  # French
    "rectangle3d",
    "RECTANGLE3D",  # English
    "OBDÉLNÍK3D",  # Czech
    "PROSTOKĄT3D",  # Polish
    "RECHTECK3D",  # German
    "RECTÁNGULO3D",  # Spanish
    "RETTANGOLO3D",  # Italian
    "RECTANGLE3D",  # French
]
