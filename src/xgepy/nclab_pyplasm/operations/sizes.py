"""
Size Operations Module

This module provides functions for calculating dimensions of geometric objects.
It includes functions for calculating overall size (SIZE) and specific axis sizes
(SIZEX, SIZEY, SIZEZ) of objects, with support for both single objects and lists.
"""


from nclab.tools import ExceptionWT
from ..utils.common import flatten
from ..geometry.base import BASEOBJ, EMPTYSET
from ..geometry.bounds import MAXX, MAXY, MINY, MINX, MAXZ, MINZ
from ...fenvs import PLASM_SIZE


__all__ = [
    "size",
    "sizex",
    "sizey",
    "sizez",
    "SIZE",
    "SIZEX",
    "SIZEY",
    "SIZEZ",
    # Language variants for SIZE
    "VELIKOST",
    "ROZMER",
    "DELKA",  # Czech
    "ROZMIAR",  # Polish
    "GRÖSSE",
    "GROESSE",
    "LÄNGE",
    "LAENGE",  # German
    "TAMANO",
    "LONGITUD",  # Spanish
    "TAGLIA",
    "LUNGHEZZA",  # Italian
    "TAILLE",
    "LONGUEUR",  # French
]


def size(*args):
    raise ExceptionWT("Command size() is undefined. Try SIZE() instead?")


def SIZE(pol, List):
    return PLASM_SIZE(List)(pol.geom)


# Czech:
VELIKOST = SIZE
ROZMER = SIZE
DELKA = SIZE

# Polish:
ROZMIAR = SIZE

# German:
GRÖSSE = SIZE
GROESSE = SIZE  # Alternative without Umlaut
LÄNGE = SIZE
LAENGE = SIZE  # Alternative without Umlaut

# Spanish:
TAMANO = SIZE  # Simplified form of TAMAÑO
LONGITUD = SIZE

# Italian:
TAGLIA = SIZE
LUNGHEZZA = SIZE

# French:
TAILLE = SIZE
LONGUEUR = SIZE


def sizex(*args):
    raise ExceptionWT("Command sizex() is undefined. Try SIZEX() instead?")


def SIZEX(obj):
    # Sanity test:
    if isinstance(obj, list):
        obj = flatten(obj)
        for oo in obj:
            if isinstance(oo, tuple):
                raise ExceptionWT("Use the UNION command to create unions of objects.")
            if not isinstance(oo, BASEOBJ):
                raise ExceptionWT("Invalid object obj detected in SIZEX(obj)!")
    else:
        if isinstance(obj, tuple):
            raise ExceptionWT("Use the UNION command to create unions of objects.")
        if not isinstance(obj, BASEOBJ):
            raise ExceptionWT("Invalid object obj detected in SIZEX(obj)!")
    # Size calculation:
    if EMPTYSET(obj):
        return 0
    else:
        return MAXX(obj) - MINX(obj)


def sizey(*args):
    raise ExceptionWT("Command sizey() is undefined. Try SIZEY() instead?")


def SIZEY(obj):
    # Sanity test:
    if isinstance(obj, list):
        obj = flatten(obj)
        for oo in obj:
            if isinstance(oo, tuple):
                raise ExceptionWT("Use the UNION command to create unions of objects.")
            if not isinstance(oo, BASEOBJ):
                raise ExceptionWT("Invalid object obj detected in SIZEY(obj)!")
    else:
        if isinstance(obj, tuple):
            raise ExceptionWT("Use the UNION command to create unions of objects.")
        if not isinstance(obj, BASEOBJ):
            raise ExceptionWT("Invalid object obj detected in SIZEY(obj)!")
    # Size calculation:
    if EMPTYSET(obj):
        return 0
    else:
        return MAXY(obj) - MINY(obj)


def sizez(*args):
    raise ExceptionWT("Command sizez() is undefined. Try SIZEZ() instead?")


def SIZEZ(obj):
    # Sanity test:
    if isinstance(obj, list):
        obj = flatten(obj)
        for oo in obj:
            if isinstance(oo, tuple):
                raise ExceptionWT("Use the UNION command to create unions of objects.")
            if not isinstance(oo, BASEOBJ):
                raise ExceptionWT("Invalid object obj detected in SIZEZ(obj)!")
    else:
        if isinstance(obj, tuple):
            raise ExceptionWT("Use the UNION command to create unions of objects.")
        if not isinstance(obj, BASEOBJ):
            raise ExceptionWT("Invalid object obj detected in SIZEZ(obj)!")
    # Size calculation:
    if EMPTYSET(obj):
        return 0
    else:
        return MAXZ(obj) - MINZ(obj)
