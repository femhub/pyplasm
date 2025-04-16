"""
Rotation Operations Module

This module provides functions for rotating geometric objects in 2D and 3D space.
The ROTATE function supports rotation around specified axes with customizable rotation
centers and handles both single objects and lists of objects.
"""

from nclab.tools import ExceptionWT
from ..utils.common import flatten, ISNUMBER
from ..operations.copy_objects import COPY


def rotate(*args):
    raise ExceptionWT("Command rotate() is undefined. Try ROTATE() instead?")


def ROTATE(obj, angle_deg, axis=3, point=[0, 0, 0]):
    if not ISNUMBER(angle_deg):
        raise ExceptionWT("In ROTATE(obj, alpha, axis), angle alpha must be a number!")
    # this is a bit nasty but it allows to skip axis in 2D (it will be Z) and
    # give just the center point:
    centerpoint = point
    if isinstance(axis, list):
        centerpoint = axis
        axis = 3
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
        # print("Axis is:", axis)
        raise ExceptionWT("In ROTATE(obj, angle, axis), axis must be X, Y or Z!")
    if axis == "x" or axis == "X":
        axis = 1
    if axis == "y" or axis == "Y":
        axis = 2
    if axis == "z" or axis == "Z":
        axis = 3
    if not isinstance(centerpoint, list):
        raise ExceptionWT(
            "In ROTATE(obj, angle, axis, point), point must be a list (use square brackets)!"
        )
    if not isinstance(obj, list):
        obj.rotate(angle_deg, axis, centerpoint)
    else:
        obj = flatten(obj)
        newobj = []
        for oo in obj:
            # Just a comment to test git:
            oo.rotate(angle_deg, axis, centerpoint)
            newobj.append(COPY(oo))


# English:
ROTATEDEG = ROTATE
RDEG = ROTATEDEG
R = ROTATEDEG

# Czech:
OTOČ = ROTATEDEG
OTOČENÍ = ROTATEDEG
ROTACE = ROTATEDEG
ROTUJ = ROTATEDEG

# Polish:
OBRÓĆ = ROTATEDEG

# German:
DREHE = ROTATEDEG
DREHEN = ROTATEDEG
DREHUNG = ROTATEDEG
ROTIERE = ROTATEDEG
ROTIEREN = ROTATEDEG
ROTIERUNG = ROTATEDEG

# Spanish:
GIRA = ROTATE
ROTA = ROTATE
GIRAR = ROTATE
ROTAR = ROTATE

# Italian:
RUOTARE = ROTATE
RUOTA = ROTATE

# French:
TOURNER = ROTATE
TOURNE = ROTATE

__all__ = [
    "rotate",
    "ROTATE",
    "ROTATEDEG",
    "RDEG",
    "R",
    # Language variants
    "OTOČ",
    "OTOČENÍ",
    "ROTACE",
    "ROTUJ",  # Czech
    "OBRÓĆ",  # Polish
    "DREHE",
    "DREHEN",
    "DREHUNG",
    "ROTIERE",
    "ROTIEREN",
    "ROTIERUNG",  # German
    "GIRA",
    "ROTA",
    "GIRAR",
    "ROTAR",  # Spanish
    "RUOTARE",
    "RUOTA",  # Italian
    "TOURNER",
    "TOURNE",  # French
]
