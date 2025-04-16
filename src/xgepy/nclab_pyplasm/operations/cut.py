"""
COMMAND CUT
"""

from nclab.tools import ExceptionWT
from ..utils.common import ISNUMBER
from ..geometry.bounds import *
from ..geometry.box import BOX
from ..operations.intersection import INTERSECTION


def cut(*args):
    raise ExceptionWT("Command cut() is undefined. Try CUT() instead?")


def CUT(obj, coord, axis, h=0.001):
    if not axis in ["x", "y", "z", "X", "Y", "Z", 1, 2, 3]:
        raise ExceptionWT("Use X, Y or Z as axis in CUT(obj, coord, axis)!")
    if not ISNUMBER(coord):
        raise ExceptionWT("In CUT(obj, coord, axis), coord must be a number!")
    if axis == "x" or axis == "X" or axis == 1:
        axis = 1
    elif axis == "y" or axis == "Y" or axis == 2:
        axis = 2
    elif axis == "z" or axis == "Z" or axis == 3:
        axis = 3
    else:
        raise ExceptionWT("In CUT(obj, coord, axis), axis must be X, Y or Z!")
    if axis == 1:
        if coord <= MINX(obj) or coord >= MAXX(obj):
            raise ExceptionWT(
                "In CUT(obj, coord, axis), plane X = "
                + str(coord)
                + " does not intersect with object."
            )
        return INTERSECTION(
            obj,
            BOX(
                coord - 0.5 * h,
                coord + 0.5 * h,
                MINY(obj) - 1,
                MAXY(obj) + 1,
                MINZ(obj) - 1,
                MAXZ(obj) + 1,
            ),
        )
    elif axis == 2:
        if coord <= MINY(obj) or coord >= MAXY(obj):
            raise ExceptionWT(
                "In CUT(obj, coord, axis), plane Y = "
                + str(coord)
                + " does not intersect with object."
            )
        return INTERSECTION(
            obj,
            BOX(
                MINX(obj) - 1,
                MAXX(obj) + 1,
                coord - 0.5 * h,
                coord + 0.5 * h,
                MINZ(obj) - 1,
                MAXZ(obj) + 1,
            ),
        )
    else:
        if coord <= MINZ(obj) or coord >= MAXZ(obj):
            raise ExceptionWT(
                "In CUT(obj, coord, axis), plane Z = "
                + str(coord)
                + " does not intersect with object."
            )
        return INTERSECTION(
            obj,
            BOX(
                MINX(obj) - 1,
                MAXX(obj) + 1,
                MINY(obj) - 1,
                MAXY(obj) + 1,
                coord - 0.5 * h,
                coord + 0.5 * h,
            ),
        )


__all__ = ["cut", "CUT"]
