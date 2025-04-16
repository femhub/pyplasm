"""
ERASE(obj, min, max, axis) - ERASE PART OF OBJECT THAT LIES
BETWEEN MIN AND MAX in AXIAL DIRECTION "axis"
"""

from nclab.tools import ExceptionWT
from ..utils.common import flatten, ISNUMBER
from ..geometry.base import BASEOBJ, EMPTYSET


def erase(*args):
    raise ExceptionWT("Command erase() is undefined. Try ERASE() instead?")


def ERASE(obj, minval, maxval, axis, warn=True):
    if (
        axis != "x"
        and axis != "y"
        and axis != "z"
        and axis != "X"
        and axis != "Y"
        and axis != "Z"
        and axis != 1
        and axis != 2
        and axis != 3
    ):
        raise ExceptionWT("Use X, Y or Z as axis in ERASE(obj, minval, maxval, axis)!")
    if not ISNUMBER(minval):
        raise ExceptionWT(
            "In ERASE(obj, minval, maxval, axis), minval must be a number!"
        )
    if not ISNUMBER(maxval):
        raise ExceptionWT(
            "In ERASE(obj, minval, maxval, axis), maxval must be a number!"
        )
    if axis == "x" or axis == "X":
        axis = 1
    if axis == "y" or axis == "Y":
        axis = 2
    if axis == "z" or axis == "Z":
        axis = 3
    if axis != 1 and axis != 2 and axis != 3:
        raise ExceptionWT(
            "In ERASE(obj, minval, maxval, axis), axis must be X, Y or Z!"
        )
    if maxval <= minval:
        raise ExceptionWT(
            "In ERASE(obj, minval, maxval, axis), minval must be less than maxval!"
        )

    if not isinstance(obj, list):
        if EMPTYSET(obj):
            raise ExceptionWT(
                "In ERASE(obj, minval, maxval, axis), obj is an empty set!"
            )
        if not isinstance(obj, BASEOBJ):
            raise ExceptionWT(
                "In ERASE(obj, minval, maxval, axis), obj must be a 2D or 3D object!"
            )
        if axis == 1:
            obj.erasex(minval, maxval)
        if axis == 2:
            obj.rotate(-90, 3)
            obj.erasex(minval, maxval)
            if not EMPTYSET(obj):
                obj.rotate(90, 3)
        if axis == 3:
            if obj.dim == 2:
                raise ExceptionWT(
                    "In ERASE(obj, minval, maxval, axis), axis = Z may not be used with 2D objects!"
                )
            obj.rotate(90, 2)
            obj.erasex(minval, maxval)
            if not EMPTYSET(obj):
                obj.rotate(-90, 2)
    else:
        obj = flatten(obj)  # flatten the rest as there may be structs
        for oo in obj:
            if not isinstance(oo, BASEOBJ):
                raise ExceptionWT(
                    "In ERASE(obj, minval, maxval, axis), obj must be a 2D or 3D object!"
                )
            if not EMPTYSET(oo):
                if axis == 1:
                    oo.erasex(minval, maxval)
                if axis == 2:
                    oo.rotate(-90, 3)
                    oo.erasex(minval, maxval)
                    if not EMPTYSET(oo):
                        oo.rotate(90, 3)
                if axis == 3:
                    if oo.dim == 2:
                        raise ExceptionWT(
                            "In ERASE(obj, minval, maxval, axis), axis = Z may not be used with 2D objects!"
                        )
                    oo.rotate(90, 2)
                    oo.erasex(minval, maxval)
                    if not EMPTYSET(oo):
                        oo.rotate(-90, 2)
    if EMPTYSET(obj) and warn == True:
        print("WARNING: Empty object created while erasing part of an object.")


__all__ = [
    "erase",
    "ERASE",
]
