"""
Object Movement Module

This module provides functions for translating geometric objects in 2D and 3D space.
The MOVE function supports various input patterns for specifying translations along
different axes, with support for both single objects and lists of objects.
"""


from nclab.tools import ExceptionWT
from ..utils.common import flatten, ISNUMBER
from ..operations.clean import CLEAN
from ..operations.copy_objects import COPY
from ..geometry.base import BASEOBJ, EMPTYSET


def move(*args):
    raise ExceptionWT("Command move() is undefined. Try MOVE() instead?")


def MOVE(*args):
    arglist = list(args)
    if len(arglist) <= 1:
        raise ExceptionWT(
            "Command MOVE() expects at least two arguments: a 2D or 3D object and a distance!"
        )
    obj = arglist[0]
    t1 = arglist[1]
    t2 = 0
    t3 = 0
    letterfound = False
    if len(arglist) == 3:
        t2 = arglist[2]
        if t2 == "x" or t2 == "X":
            if not ISNUMBER(t1):
                raise ExceptionWT("In MOVE(obj, dist, X), dist must be a number!")
            t2 = 0
            t3 = 0
            letterfound = True
        if t2 == "y" or t2 == "Y":
            if not ISNUMBER(t1):
                raise ExceptionWT("In MOVE(obj, dist, Y), dist must be a number!")
            t2 = t1
            t1 = 0
            t3 = 0
            letterfound = True
        if t2 == "z" or t2 == "Z":
            if not ISNUMBER(t1):
                raise ExceptionWT("In MOVE(obj, dist, Z), dist must be a number!")
            t3 = t1
            t1 = 0
            t2 = 0
            letterfound = True
    if len(arglist) >= 4:
        t2 = arglist[2]
        t3 = arglist[3]
    # Tests:
    if not ISNUMBER(t1):
        raise ExceptionWT("In MOVE(obj, dx, ...), dx must be a number!")
    if not ISNUMBER(t2):
        raise ExceptionWT("In MOVE(obj, dx, dy, ...), dy must be a number!")
    if not ISNUMBER(t3):
        raise ExceptionWT("In MOVE(obj, dx, dy, dz), dz must be a number!")
    if obj == []:
        return
    # Remove empty sets:
    CLEAN(obj)
    # Move it:
    if not isinstance(obj, list):
        if not isinstance(obj, BASEOBJ) and obj != []:
            raise ExceptionWT("In MOVE(obj, ...), obj must be a 2D or 3D object!")
        if not EMPTYSET(obj):
            obj.move(t1, t2, t3)
    else:
        obj = flatten(obj)
        newobj = []
        for oo in obj:
            if not isinstance(oo, BASEOBJ):
                raise ExceptionWT("In MOVE(obj, ...), obj must be a 2D or 3D object!")
            if not EMPTYSET(oo) and oo != []:
                oo.move(t1, t2, t3)
                newobj.append(COPY(oo))


# English:
TRANSLATE = MOVE
T = MOVE
M = MOVE
SHIFT = TRANSLATE

# Czech:
POSUN = TRANSLATE
POSUNUTÍ = TRANSLATE

# Polish:
PRZENIEŚ = TRANSLATE
PRZESUŃ = TRANSLATE

# German:
BEWEGE = TRANSLATE
BEWEGEN = TRANSLATE
BEWEGUNG = TRANSLATE
VERSCHIEBUNG = TRANSLATE
VERSCHIEBEN = TRANSLATE
VERSCHIEBE = TRANSLATE

# Spanish:
MOVER = TRANSLATE
MUEVA = TRANSLATE
MUEVE = TRANSLATE

# Italian:
MUOVERE = TRANSLATE
MUOVI = TRANSLATE
SPOSTARE = TRANSLATE
SPOSTA = TRANSLATE

# French:
DÉPLACER = TRANSLATE
DÉPLACE = TRANSLATE

__all__ = [
    "move",
    "MOVE",
    "TRANSLATE",
    "T",
    "M",
    "SHIFT",
    # Language variants
    "POSUN",
    "POSUNUTÍ",  # Czech
    "PRZENIEŚ",
    "PRZESUŃ",  # Polish
    "BEWEGE",
    "BEWEGEN",
    "BEWEGUNG",
    "VERSCHIEBUNG",
    "VERSCHIEBEN",
    "VERSCHIEBE",  # German
    "MOVER",
    "MUEVA",
    "MUEVE",  # Spanish
    "MUOVERE",
    "MUOVI",
    "SPOSTARE",
    "SPOSTA",  # Italian
    "DÉPLACER",
    "DÉPLACE",  # French
]
