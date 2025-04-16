"""
SUBTRACT Module
"""

from nclab.tools import ExceptionWT
from ..utils.common import flatten
from ..geometry.base import BASEOBJ, EMPTYSET
from ..operations.copy_objects import COPY

__all__ = [
    "subtract",
    "SUBTRACT",
    "MINUS",
    # Language variants
    "ODECTI",
    "ODECIST",  # Czech
    "ODEJMIJ",  # Polish
    "ABZIEHE",
    "SUBTRAHIERE",  # German
    "SUSTRAER",
    "SUSTRAE",  # Spanish
    "SOTTRARRE",
    "SOTTRAI",  # Italian
    "SOUSTRAIRE",
    "SOUSTRAIS",  # French
]


def subtract(*args):
    raise ExceptionWT("Command subtract() is undefined. Try SUBTRACT() instead?")


def SUBTRACT(a, b, warn=True):
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
            raise ExceptionWT("Invalid object found (subtract - 1).")
        if isinstance(b, tuple):
            raise ExceptionWT("Use the UNION command to create unions of objects.")
        if not isinstance(b, BASEOBJ):
            raise ExceptionWT("Invalid object found (subtract - 2).")
        a.subtract(b)
        if EMPTYSET(a) and warn == True:
            print("WARNING: Empty object created while subtracting objects.")
        return
    # a is single object, b is a list:
    if not isinstance(a, list) and isinstance(b, list):
        flatb = flatten(b)  # flatten the list as there may be structs
        for x in flatb:
            if isinstance(x, tuple):
                raise ExceptionWT("Use the UNION command to create unions of objects.")
            if not isinstance(x, BASEOBJ):
                raise ExceptionWT("Invalid object found (subtract - 3).")
        if isinstance(a, tuple):
            raise ExceptionWT("Use the UNION command to create unions of objects.")
        if not isinstance(a, BASEOBJ):
            raise ExceptionWT("Invalid object found (subtract - 4).")
        a.subtract(flatb)
        if EMPTYSET(a) and warn == True:
            print("WARNING: Empty object created while subtracting objects.")
        return
    # a is a list, b is single object:
    if isinstance(a, list) and not isinstance(b, list):
        if isinstance(b, tuple):
            raise ExceptionWT("Use the UNION command to create unions of objects.")
        if not isinstance(b, BASEOBJ):
            raise ExceptionWT("Invalid object found (subtract - 5).")
        flata = flatten(a)  # flatten the list as there may be structs
        b2 = COPY(b)  # This is important as 'b' can be changed by the subtraction
        newlist = []
        for x in flata:
            if isinstance(x, tuple):
                raise ExceptionWT("Use the UNION command to create unions of objects.")
            if not isinstance(x, BASEOBJ):
                raise ExceptionWT("Invalid object found (subtract - 6).")
            x.subtract(b2)  # Important - do not subtract the original item
            if not EMPTYSET(x):
                newlist.append(COPY(x))
            if EMPTYSET(x) and warn == True:
                print("WARNING: Empty object created while subtracting objects.")
        return
    # a is a list, b is a list:
    if isinstance(a, list) and isinstance(b, list):
        flata = flatten(a)  # flatten the list as there may be structs
        for x in flata:
            if isinstance(x, tuple):
                raise ExceptionWT("Use the UNION command to create unions of objects.")
            if not isinstance(x, BASEOBJ):
                raise ExceptionWT("Invalid object found (subtract - 7).")
        flatb = flatten(b)  # flatten the list as there may be structs
        for x in flatb:
            if isinstance(x, tuple):
                raise ExceptionWT("Use the UNION command to create unions of objects.")
            if not isinstance(x, BASEOBJ):
                raise ExceptionWT("Invalid object found (subtract - 8).")
        newlist = []
        flatbcopy = []
        for it in flatb:
            flatbcopy.append(COPY(it))
        for x in flata:
            x.subtract(flatbcopy)  # Important - do not subtract the original item
            if not EMPTYSET(x):
                newlist.append(COPY(x))
            if EMPTYSET(x) and warn == True:
                print("WARNING: Empty object created while subtracting objects.")


MINUS = SUBTRACT  # Short form

# Czech:
ODECTI = SUBTRACT  # Subtract
ODECIST = SUBTRACT  # To subtract

# Polish:
ODEJMIJ = SUBTRACT  # Subtract

# German:
ABZIEHE = SUBTRACT  # Subtract
SUBTRAHIERE = SUBTRACT  # Subtract

# Spanish:
SUSTRAER = SUBTRACT  # Subtract
SUSTRAE = SUBTRACT  # Subtract

# Italian:
SOTTRARRE = SUBTRACT  # Subtract
SOTTRAI = SUBTRACT  # Subtract

# French:
SOUSTRAIRE = SUBTRACT  # Subtract
SOUSTRAIS = SUBTRACT  # Subtract
