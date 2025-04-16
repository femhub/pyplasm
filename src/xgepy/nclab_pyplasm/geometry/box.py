"""
Box Creation Module

This module provides functions for creating box objects in 2D and 3D space with various
parameter configurations. The BOX function supports multiple input patterns for creating
boxes with different dimensions and positions.
"""

from nclab.tools import ExceptionWT
from ..utils.common import flatten, ISNUMBER
from ..geometry.base import BASEOBJ
from ..operations.move import MOVE
from ...fenvs import CUBOID


def box(*args):
    raise ExceptionWT("Command box() is undefined. Try BOX() instead?")


def BOX(*args):
    list1 = list(args)
    list1 == flatten(list1)
    if len(list1) == 1:
        a = list1[0]
        if not ISNUMBER(a):
            raise ExceptionWT("Size a in BOX(a) must be a number!")
        if a <= 0:
            raise ExceptionWT("Size a in BOX(a) must be positive!")
        return BASEOBJ(CUBOID([a, a, a]))
    if len(list1) == 2:
        a = list1[0]
        b = list1[1]
        if not ISNUMBER(a):
            raise ExceptionWT("Size a in BOX(a, b) must be a number!")
        if not ISNUMBER(b):
            raise ExceptionWT("Size b in BOX(a, b) must be a number!")
        if a <= 0 or b <= 0:
            raise ExceptionWT("Sizes a, b in BOX(a, b) must be positive!")
        return BASEOBJ(CUBOID([a, b]))
    if len(list1) == 3:
        a = list1[0]
        b = list1[1]
        c = list1[2]
        if not ISNUMBER(a):
            raise ExceptionWT("Size a in BOX(a, b, c) must be a number!")
        if not ISNUMBER(b):
            raise ExceptionWT("Size b in BOX(a, b, c) must be a number!")
        if not ISNUMBER(c):
            raise ExceptionWT("Size c in BOX(a, b, c) must be a number!")
        if a <= 0 or b <= 0 or c <= 0:
            raise ExceptionWT("Sizes a, b, c in BOX(a, b, c) must be positive!")
        return BASEOBJ(CUBOID([a, b, c]))
    if len(list1) == 4:
        xmin = list1[0]
        xmax = list1[1]
        ymin = list1[2]
        ymax = list1[3]
        if not ISNUMBER(xmin):
            raise ExceptionWT(
                "Minimum x coordinate xmin in BOX(xmin, xmax, ymin, ymax) must be a number!"
            )
        if not ISNUMBER(xmax):
            raise ExceptionWT(
                "Maximum x coordinate xmax in BOX(xmin, xmax, ymin, ymax) must be a number!"
            )
        if not ISNUMBER(ymin):
            raise ExceptionWT(
                "Minimum y coordinate ymin in BOX(xmin, xmax, ymin, ymax) must be a number!"
            )
        if not ISNUMBER(ymax):
            raise ExceptionWT(
                "Maximum y coordinate ymax in BOX(xmin, xmax, ymin, ymax) must be a number!"
            )
        if xmin >= xmax:
            raise ExceptionWT("xmin >= xmax in BOX(xmin, xmax, ymin, ymax)!")
        if ymin >= ymax:
            raise ExceptionWT("ymin >= ymax in BOX(xmin, xmax, ymin, ymax)!")
        obj = BASEOBJ(CUBOID([xmax - xmin, ymax - ymin]))
        MOVE(obj, xmin, ymin)
        return obj
    if len(list1) == 6:
        xmin = list1[0]
        xmax = list1[1]
        ymin = list1[2]
        ymax = list1[3]
        zmin = list1[4]
        zmax = list1[5]
        if not ISNUMBER(xmin):
            raise ExceptionWT(
                "Minimum x coordinate xmin in BOX(xmin, xmax, ymin, ymax, zmin, zmax) must be a number!"
            )
        if not ISNUMBER(xmax):
            raise ExceptionWT(
                "Maximum x coordinate xmax in BOX(xmin, xmax, ymin, ymax, zmin, zmax) must be a number!"
            )
        if not ISNUMBER(ymin):
            raise ExceptionWT(
                "Minimum y coordinate ymin in BOX(xmin, xmax, ymin, ymax, zmin, zmax) must be a number!"
            )
        if not ISNUMBER(ymax):
            raise ExceptionWT(
                "Maximum y coordinate ymax in BOX(xmin, xmax, ymin, ymax, zmin, zmax) must be a number!"
            )
        if not ISNUMBER(zmin):
            raise ExceptionWT(
                "Minimum z coordinate zmin in BOX(xmin, xmax, ymin, ymax, zmin, zmax) must be a number!"
            )
        if not ISNUMBER(zmax):
            raise ExceptionWT(
                "Maximum z coordinate zmax in BOX(xmin, xmax, ymin, ymax, zmin, zmax) must be a number!"
            )
        if xmin >= xmax:
            raise ExceptionWT(
                "xmin >= xmax in BOX(xmin, xmax, ymin, ymax, zmin, zmax)!"
            )
        if ymin >= ymax:
            raise ExceptionWT(
                "ymin >= ymax in BOX(xmin, xmax, ymin, ymax, zmin, zmax)!"
            )
        if zmin >= zmax:
            raise ExceptionWT(
                "zmin >= zmax in BOX(xmin, xmax, ymin, ymax, zmin, zmax)!"
            )
        obj = BASEOBJ(CUBOID([xmax - xmin, ymax - ymin, zmax - zmin]))
        MOVE(obj, xmin, ymin, zmin)
        return obj

    raise ExceptionWT("The BOX command accepts 1, 2, 3, 4 or 6 parameters!")


__all__ = [
    "box",
    "BOX",
]
