"""
Scaling Operations Module
"""


from nclab.tools import ExceptionWT
from ..utils.common import flatten, ISNUMBER
from ..operations.clean import CLEAN
from ..geometry.base import BASEOBJ, EMPTYSET


def scale(*args):
    raise ExceptionWT("Command scale() is undefined. Try SCALE() instead?")


def SCALE(*args):
    arglist = list(args)
    if len(arglist) <= 2:
        raise ExceptionWT("Command SCALE() expects at least three arguments!")
    obj = arglist[0]
    a = arglist[1]
    b = arglist[2]
    c = 1
    if len(arglist) >= 4:
        c = arglist[3]
    else:
        if b == "x" or b == "X":
            b = 1
            c = 1
        if b == "y" or b == "Y":
            b = a
            a = 1
            c = 1
        if b == "z" or b == "Z":
            c = a
            a = 1
            b = 1
    # Sanity tests:
    if not ISNUMBER(a):
        raise ExceptionWT(
            "In the SCALE command, the first argument is a 2D or 3D object and the second one is a number!"
        )
    if not ISNUMBER(b):
        raise ExceptionWT(
            "In SCALE(obj, sx, sy) or SCALE(obj, sx, sy, sz), sy must be a number!"
        )
    if not ISNUMBER(c):
        raise ExceptionWT("In SCALE(obj, sx, sy, sz), sz must be a number!")
    if obj == []:
        return
    # Remove empty sets:
    CLEAN(obj)
    # Scale it:
    if not isinstance(obj, list):
        if not isinstance(obj, BASEOBJ):
            raise ExceptionWT(
                "In SCALE(obj, sx, sy) or SCALE(obj, sx, sy, sz), obj must be a 2D or 3D object!"
            )
        if not EMPTYSET(obj) and obj != []:
            obj.scale(a, b, c)
    else:
        obj = flatten(obj)
        for oo in obj:
            if not isinstance(oo, BASEOBJ):
                raise ExceptionWT(
                    "In SCALE(obj, sx, sy) or SCALE(obj, sx, sy, sz), obj must be a 2D or 3D object!"
                )
            if not EMPTYSET(oo) and oo != []:
                oo.scale(a, b, c)


S = SCALE
# Czech:
SKALUJ = SCALE
SKALOVANI = SCALE
# Polish:
SKALUJ = SCALE
PRZESKALUJ = SCALE
# German:
SKALIERE = SCALE
SKALIEREN = SCALE
# Spanish:
ESCALA = SCALE
ESCALAR = SCALE
# Italian:
SCALA = SCALE
SCALARE = SCALE
# French:
ECHELLE = SCALE
REDIMENSIONNER = SCALE

__all__ = [
    "scale",
    "SCALE",
    "S",
    # Language variants
    "SKALUJ",
    "SKALOVANI",  # Czech
    "SKALUJ",
    "PRZESKALUJ",  # Polish
    "SKALIERE",
    "SKALIEREN",  # German
    "ESCALA",
    "ESCALAR",  # Spanish
    "SCALA",
    "SCALARE",  # Italian
    "ECHELLE",
    "REDIMENSIONNER",  # French
]
