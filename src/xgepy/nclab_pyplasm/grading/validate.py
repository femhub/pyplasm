"""
TEST VALIDITY OF OBJECTS
"""

from ..utils.common import flatten
from ..geometry.base import BASEOBJ, EMPTYSET


def VALIDATE(obj, name, dim):
    if isinstance(obj, int):
        return (
            False,
            "'" + name + "' is a number while it should be a " + str(dim) + "D object.",
        )
    if isinstance(obj, float):
        return (
            False,
            "'" + name + "' is a number while it should be a " + str(dim) + "D object.",
        )
    if isinstance(obj, str):
        return (
            False,
            "'"
            + name
            + "' is a text string while it should be a "
            + str(dim)
            + "D object.",
        )
    if isinstance(obj, bool):
        return (
            False,
            "'"
            + name
            + "' is a True/False value while it should be a "
            + str(dim)
            + "D object.",
        )
    if hasattr(obj, "__call__"):
        return (
            False,
            "'"
            + name
            + "' is a callable function while it should be a "
            + str(dim)
            + "D object.",
        )

    if isinstance(obj, tuple):
        m = len(obj)
        if m == 0:
            return False, "It looks like your object '" + name + "' is empty."
        else:
            return False, "Please use the UNION command to create unions of objects."

    if not isinstance(obj, BASEOBJ) and not isinstance(obj, list):
        return False, "Object '" + name + "' is invalid."

    if isinstance(obj, BASEOBJ):
        if dim == 2 and obj.dim == 3:
            return (
                False,
                "Your object '" + name + "' should be a 2D object (it is a 3D object).",
            )
        if dim == 3 and obj.dim == 2:
            return (
                False,
                "Your object '" + name + "' should be a 3D object (it is a 2D object).",
            )

    if isinstance(obj, list):
        m = len(obj)
        if m == 0:
            return False, "It looks like your object '" + name + "' is empty."
        newobj = flatten(obj)
        for ooo in newobj:
            if not isinstance(ooo, BASEOBJ):
                return False, "'" + name + "' is not a valid " + str(dim) + "D object."
            if dim == 2 and ooo.dim == 3:
                return (
                    False,
                    "Your object '"
                    + name
                    + "' should be a 2D object (it is a 3D object).",
                )
            if dim == 3 and ooo.dim == 2:
                return (
                    False,
                    "Your object '"
                    + name
                    + "' should be a 3D object (it is a 2D object).",
                )

    if EMPTYSET(obj):
        return False, "Your object '" + name + "' is an empty set."

    return True, None
