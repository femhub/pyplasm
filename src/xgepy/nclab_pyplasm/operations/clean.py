"""
CLEAN - REMOVE EMPTY SETS FROM OBJECTS WHICH ARE LISTS
"""

from nclab.tools import ExceptionWT
from ..geometry.base import EMPTYSET


def clean(*args):
    raise ExceptionWT("Command clean() is undefined. Try CLEAN() instead?")


def CLEAN(obj):
    if not isinstance(obj, list):
        return
    while obj.count([]) > 0:
        obj.remove([])
    ok = False
    while not ok:
        for x in obj:
            if EMPTYSET(x):
                obj.remove(x)
                ok = False
                break
            ok = True
    return


__all__ = [
    "clean",
    "CLEAN",
]
