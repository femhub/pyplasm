"""
Union Operations Module
"""

from nclab.tools import ExceptionWT
from ..utils.common import flatten
from ..geometry.base import BASEOBJ
from ..operations.copy_objects import COPY


# NEW DEFINITION - UNION IS JUST STRUCT
def union(*args):
    raise ExceptionWT("Command union() is undefined. Try UNION() instead?")


def UNION(*args):
    list1 = list(args)
    list1 = flatten(list1)  # flatten the rest as there may be structs
    if len(list1) < 2:
        raise ExceptionWT("UNION() must be applied to at least two objects!")
    for o in list1:
        if isinstance(o, tuple):
            raise ExceptionWT("Use the UNION command to create unions of objects.")
        if not isinstance(o, BASEOBJ):
            raise ExceptionWT("Invalid object found in UNION().")
    return [COPY(obj) for obj in list1]


# English:
GLUE = UNION
U = UNION
SUM = UNION

# Czech:
SJEDNOCENI = UNION
SOUCET = UNION
SECTI = UNION
SECIST = UNION
SUMA = UNION

# Polish:
UNIA = UNION
SUMA = UNION

# German:
VEREINIGE = UNION
VEREINIGUNG = UNION
SUMME = UNION

# Spanish:
SUMA = UNION

# Italian:
SOMMA = UNION
UNIONE = UNION

# French:
UNION = UNION
SOMME = UNION

__all__ = [
    "union",
    "UNION",
    "GLUE",
    "U",
    "SUM",
    # Language variants
    "SJEDNOCENI",
    "SOUCET",
    "SECTI",
    "SECIST",
    "SUMA",  # Czech
    "UNIA",
    "SUMA",  # Polish
    "VEREINIGE",
    "VEREINIGUNG",
    "SUMME",  # German
    "SUMA",  # Spanish
    "SOMMA",
    "UNIONE",  # Italian
    "UNION",
    "SOMME",  # French
]
