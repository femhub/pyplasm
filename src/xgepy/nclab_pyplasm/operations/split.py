"""
SPLIT Module
"""

from nclab.tools import ExceptionWT
from ..utils.common import flatten, ISNUMBER
from ..geometry.base import BASEOBJ, EMPTYSET


_all__ = [
    "split",
    "SPLIT",
]


def split(*args):
    raise ExceptionWT("Command split() is undefined. Try SPLIT() instead?")


def SPLIT(obj, coord, axis, warn=True):
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
        raise ExceptionWT("Use X, Y or Z as axis in SPLIT(obj, coord, axis)!")
    if not ISNUMBER(coord):
        raise ExceptionWT("In SPLIT(obj, coord, axis), coord must be a number!")
    if axis == "x" or axis == "X":
        axis = 1
    if axis == "y" or axis == "Y":
        axis = 2
    if axis == "z" or axis == "Z":
        axis = 3
    if axis != 1 and axis != 2 and axis != 3:
        raise ExceptionWT("In SPLIT(obj, coord, axis), axis must be X, Y or Z!")

    if not isinstance(obj, list):
        if EMPTYSET(obj):
            raise ExceptionWT("In SPLIT(obj, coord, axis), obj is an empty set!")
        if not isinstance(obj, BASEOBJ):
            raise ExceptionWT(
                "In SPLIT(obj, coord, axis), obj must be a 2D or 3D object!"
            )
        if axis == 1:
            obj1, obj2 = obj.splitx(coord)
        if axis == 2:
            obj.rotate(-90, 3)
            obj1, obj2 = obj.splitx(coord)
            if not EMPTYSET(obj1):
                obj1.rotate(90, 3)
            else:
                print("WARNING: Empty object created while splitting an object.")
            if not EMPTYSET(obj2):
                obj2.rotate(90, 3)
            else:
                print("WARNING: Empty object created while splitting an object.")
        if axis == 3:
            if obj.dim == 2:
                raise ExceptionWT(
                    "In SPLIT(obj, coord, axis), axis = Z may not be used with 2D objects!"
                )
            obj.rotate(90, 2)
            obj1, obj2 = obj.splitx(coord)
            if not EMPTYSET(obj1):
                obj1.rotate(-90, 2)
            else:
                print("WARNING: Empty object created while splitting an object.")
            if not EMPTYSET(obj2):
                obj2.rotate(-90, 2)
            else:
                print("WARNING: Empty object created while splitting an object.")
    else:
        obj = flatten(obj)  # flatten the rest as there may be structs
        obj1 = []
        obj2 = []
        for oo in obj:
            if not isinstance(oo, BASEOBJ):
                raise ExceptionWT(
                    "In SPLIT(obj, coord, axis), obj must be a 2D or 3D object!"
                )
            if not EMPTYSET(oo):
                if axis == 1:
                    oo1, oo2 = oo.splitx(coord)
                    if not EMPTYSET(oo1):
                        obj1.append(oo1)
                    if not EMPTYSET(oo2):
                        obj2.append(oo2)
                if axis == 2:
                    oo.rotate(-90, 3)
                    oo1, oo2 = oo.splitx(coord)
                    if not EMPTYSET(oo1):
                        oo1.rotate(90, 3)
                        obj1.append(oo1)
                    if not EMPTYSET(oo2):
                        oo2.rotate(90, 3)
                        obj2.append(oo2)
                if axis == 3:
                    if oo.dim == 2:
                        raise ExceptionWT(
                            "In SPLIT(obj, coord, axis), axis = Z may not be used with 2D objects!"
                        )
                    oo.rotate(90, 2)
                    oo1, oo2 = oo.splitx(coord)
                    if not EMPTYSET(oo1):
                        oo1.rotate(-90, 2)
                        obj1.append(oo1)
                    if not EMPTYSET(oo2):
                        oo2.rotate(-90, 2)
                        obj2.append(oo2)
    if EMPTYSET(obj1):
        print("WARNING: Empty object created while splitting an object.")
    if EMPTYSET(obj2):
        print("WARNING: Empty object created while splitting an object.")
    return obj1, obj2
