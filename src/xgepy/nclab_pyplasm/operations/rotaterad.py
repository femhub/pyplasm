"""

"""


from nclab.tools import ExceptionWT
from ..utils.common import flatten, ISNUMBER
from ..geometry.base import BASEOBJ, EMPTYSET
from ..operations.clean import CLEAN


def rotaterad(*args):
    raise ExceptionWT("Command rotaterad() is undefined. Try ROTATERAD() instead?")


def ROTATERAD(obj, angle_rad, axis=3, point=[0, 0, 0]):
    if not ISNUMBER(angle_rad):
        raise ExceptionWT(
            "Angle alpha in ROTATERAD(obj, alpha, axis) must be a number!"
        )
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
        raise ExceptionWT("In ROTATERAD(obj, angle, axis), axis must be X, Y or Z!")
    if axis == "x" or axis == "X":
        axis = 1
    if axis == "y" or axis == "Y":
        axis = 2
    if axis == "z" or axis == "Z":
        axis = 3
    if not isinstance(centerpoint, list):
        raise ExceptionWT(
            "In ROTATERAD(obj, angle, axis, point), point must be a list (use square brackets)!"
        )
    # Remove empty sets:
    CLEAN(obj)
    # Rotate it:
    if not isinstance(obj, list):
        if not isinstance(obj, BASEOBJ):
            raise ExceptionWT(
                "In ROTATERAD(obj, angle, axis), obj must be a 2D or 3D object!"
            )
        if not EMPTYSET(obj) and obj != []:
            obj.rotaterad(angle_rad, axis, centerpoint)
    else:
        obj = flatten(obj)
        for oo in obj:
            if not isinstance(oo, BASEOBJ):
                raise ExceptionWT(
                    "In ROTATERAD(obj, angle, axis), obj must be a 2D or 3D object!"
                )
            if not EMPTYSET(oo) and oo != []:
                oo.rotaterad(angle_rad, axis, centerpoint)


RRAD = ROTATERAD

# Czech:
OTOCRAD = ROTATERAD
OTOCENIRAD = ROTATERAD
ROTACERAD = ROTATERAD
ROTUJRAD = ROTATERAD

# Polish:
OBROCRAD = ROTATERAD

# German:
DREHERAD = ROTATERAD
DREHENRAD = ROTATERAD
DREHUNGRAD = ROTATERAD
ROTIERERAD = ROTATERAD
ROTIERENRAD = ROTATERAD
ROTIERUNGRAD = ROTATERAD

# Spanish:
GIRARAD = ROTATERAD
ROTARAD = ROTATERAD
GIRARRAD = ROTATERAD
ROTARRAD = ROTATERAD

# Italian:
RUOTARERAD = ROTATERAD
RUOTARAD = ROTATERAD

# French:
TOURNERRAD = ROTATERAD
TOURNERAD = ROTATERAD

__all__ = [
    # Main functions
    "rotaterad",
    "ROTATERAD",
    "RRAD",
    # Language variants
    "OTOCRAD",
    "OTOCENIRAD",
    "ROTACERAD",
    "ROTUJRAD",  # Czech
    "OBROCRAD",  # Polish
    "DREHERAD",
    "DREHENRAD",
    "DREHUNGRAD",
    "ROTIERERAD",
    "ROTIERENRAD",
    "ROTIERUNGRAD",  # German
    "GIRARAD",
    "ROTARAD",
    "GIRARRAD",
    "ROTARRAD",  # Spanish
    "RUOTARERAD",
    "RUOTARAD",  # Italian
    "TOURNERRAD",
    "TOURNERAD",  # French
]
