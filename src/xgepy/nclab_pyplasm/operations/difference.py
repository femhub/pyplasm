"""
Difference Operations Module

This module provides functions for performing geometric difference operations between objects.
The DIFFERENCE function supports various combinations of single objects and lists of objects,
with automatic flattening of nested structures.
"""


from nclab.tools import ExceptionWT
from ..utils.common import flatten
from ..geometry.base import BASEOBJ, EMPTYSET


def difference(*args):
    raise ExceptionWT("Command difference() is undefined. Try DIFFERENCE() instead?")


def diff(*args):
    raise ExceptionWT("Command diff() is undefined. Try DIFF() instead?")


def DIFFERENCE(a, b, warn=True):
    if isinstance(a, list):
        if a == []:
            raise ExceptionWT(
                "Cannot subtract an object from an empty list of objects."
            )
    if isinstance(b, list):
        if b == []:
            raise ExceptionWT(
                "Cannot subtract an empty list of objects from an object."
            )
    # a is single object, b is single object:
    if not isinstance(a, list) and not isinstance(b, list):
        if isinstance(a, tuple):
            raise ExceptionWT("Use the UNION command to create unions of objects.")
        if not isinstance(a, BASEOBJ):
            raise ExceptionWT("Invalid object found (diff - 1).")
        if isinstance(b, tuple):
            raise ExceptionWT("Use the UNION command to create unions of objects.")
        if not isinstance(b, BASEOBJ):
            raise ExceptionWT("Invalid object found (diff - 2).")
        out = a.diff(b)
        if EMPTYSET(out) and warn == True:
            print("WARNING: Empty set created while subtracting objects.")
        return out
    # a is single object, b is a list:
    if not isinstance(a, list) and isinstance(b, list):
        flatb = flatten(b)  # flatten the list as there may be structs
        for x in flatb:
            if isinstance(x, tuple):
                raise ExceptionWT("Use the UNION command to create unions of objects.")
            if not isinstance(x, BASEOBJ):
                raise ExceptionWT("Invalid object found (diff - 3).")
        if isinstance(a, tuple):
            raise ExceptionWT("Use the UNION command to create unions of objects.")
        if not isinstance(a, BASEOBJ):
            raise ExceptionWT("Invalid object found (diff - 4).")
        out = a.diff(flatb)
        if EMPTYSET(out) and warn == True:
            print("WARNING: Empty set created while subtracting objects.")
        return out
    # a is a list, b is single object:
    if isinstance(a, list) and not isinstance(b, list):
        flata = flatten(a)  # flatten the list as there may be structs
        for x in flata:
            if isinstance(x, tuple):
                raise ExceptionWT("Use the UNION command to create unions of objects.")
            if not isinstance(x, BASEOBJ):
                raise ExceptionWT("Invalid object found (diff - 5).")
        if isinstance(b, tuple):
            raise ExceptionWT("Use the UNION command to create unions of objects.")
        if not isinstance(b, BASEOBJ):
            raise ExceptionWT("Invalid object found (diff - 6).")
        newlist = []
        for x in flata:
            out = x.diff(b)
            if not EMPTYSET(out):
                newlist.append(out)
        if EMPTYSET(newlist) and warn == True:
            print("WARNING: Empty set created while subtracting objects.")
        return newlist
    # a is a list, b is a list:
    if isinstance(a, list) and isinstance(b, list):
        flata = flatten(a)  # flatten the list as there may be structs
        for x in flata:
            if isinstance(x, tuple):
                raise ExceptionWT("Use the UNION command to create unions of objects.")
            if not isinstance(x, BASEOBJ):
                raise ExceptionWT("Invalid object found (diff - 7).")
        flatb = flatten(b)  # flatten the list as there may be structs
        for x in flatb:
            if isinstance(x, tuple):
                raise ExceptionWT("Use the UNION command to create unions of objects.")
            if not isinstance(x, BASEOBJ):
                raise ExceptionWT("Invalid object found (diff - 8).")
        newlist = []
        for x in flata:
            out = x.diff(flatb)
            if not EMPTYSET(out):
                newlist.append(out)
        if EMPTYSET(newlist) and warn == True:
            print("WARNING: Empty set created while subtracting objects.")
        return newlist


# English:
DIFF = DIFFERENCE
D = DIFF

# Czech:
ROZDIL = DIFF

# Polish:
ROZNICA = DIFF

# German:
DIFFERENZ = DIFF

# Spanish:
DIFERENCIA = DIFF
DIF = DIFF

# Italian:
DIFFERENZA = DIFF

# French:
DIFF = DIFF

__all__ = [
    "difference",
    "diff",
    "DIFFERENCE",
    "DIFF",
    "D",
    # Language variants
    "ROZDIL",  # Czech
    "ROZNICA",  # Polish
    "DIFFERENZ",  # German
    "DIFERENCIA",
    "DIF",  # Spanish
    "DIFFERENZA",  # Italian
    "DIFF",  # French
]
