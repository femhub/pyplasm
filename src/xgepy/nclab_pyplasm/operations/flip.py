"""
Mirror and Flip Operations Module
"""

from nclab.tools import ExceptionWT
from ..utils.common import flatten, ISNUMBER
from ..geometry.base import BASEOBJ
from ..operations.copy_objects import COPY
from ..operations.move import MOVE
from ..operations.scale import SCALE
from ..utils.constants import X, Y, Z


def flip(*args):
    raise ExceptionWT("Command flip() is undefined. Try FLIP() instead?")


def mirror(*args):
    raise ExceptionWT("Command mirror() is undefined. Try MIRROR() instead?")


def MIRROR(obj, coord, axis):
    if not axis in ["x", "y", "z", "X", "Y", "Z", 1, 2, 3]:
        raise ExceptionWT("In MIRROR(obj, coord, axis), axis must be X, Y or Z!")
    if axis == "x" or axis == "X":
        axis = 1
    elif axis == "y" or axis == "Y":
        axis = 2
    else:
        axis = 3
    if not ISNUMBER(coord):
        raise ExceptionWT("In MIRROR(obj, coord, axis), coord must be a number!")
    if not isinstance(obj, list):
        if not isinstance(obj, BASEOBJ):
            raise ExceptionWT(
                "In MIRROR(obj, coord, axis), obj must be a 2D or 3D object!"
            )
        obj = COPY(obj)
        if obj.dim == 2:
            MIRROR2D(obj, coord, axis)
        else:
            MIRROR3D(obj, coord, axis)
    else:
        obj = flatten(obj)
        obj = COPY(obj)
        for oo in obj:
            if not isinstance(oo, BASEOBJ):
                raise ExceptionWT(
                    "In MIRROR(obj, coord, axis), obj must be a 2D or 3D object!"
                )
            if oo.dim == 2:
                MIRROR2D(oo, coord, axis)
            else:
                MIRROR3D(oo, coord, axis)
    return obj


def MIRROR2D(obj, coord, axis):
    if not axis in [X, Y] and not axis in [1, 2]:
        raise ExceptionWT("The axis in MIRROR2D(obj, coord, axis) must be X or Y.")
    if axis == X or axis == 1:
        MOVE(obj, -coord, 0)
        SCALE(obj, -1, 1)
        MOVE(obj, coord, 0)
    else:
        MOVE(obj, 0, -coord)
        SCALE(obj, 1, -1)
        MOVE(obj, 0, coord)


def MIRROR3D(obj, coord, axis):
    if not axis in [X, Y, Z] and not axis in [1, 2, 3]:
        raise ExceptionWT("The axis in MIRROR2D(obj, coord, axis) must be X, Y or Z.")
    if axis == X or axis == 1:
        MOVE(obj, -coord, 0, 0)
        SCALE(obj, -1, 1, 1)
        MOVE(obj, coord, 0, 0)
    elif axis == Y or axis == 2:
        MOVE(obj, 0, -coord, 0)
        SCALE(obj, 1, -1, 1)
        MOVE(obj, 0, coord, 0)
    else:
        MOVE(obj, 0, 0, -coord)
        SCALE(obj, 1, 1, -1)
        MOVE(obj, 0, 0, coord)


FLIP2D = MIRROR2D
FLIP3D = MIRROR3D
FLIP = MIRROR


__all__ = [
    "flip",
    "mirror",
    "MIRROR",
    "MIRROR2D",
    "MIRROR3D",  # Dimension-specific functions
    "FLIP",
    "FLIP2D",
    "FLIP3D",  # English aliases
]
