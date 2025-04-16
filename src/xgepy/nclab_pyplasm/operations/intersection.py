"""
Intersection Operations Module

This module provides various functions for performing geometric intersections between objects.
The main functionality includes binary intersections and more complex intersection operations
that handle different combinations of single objects and lists of objects.
"""

from nclab.tools import ExceptionWT
from ..utils.common import flatten
from ..geometry.base import BASEOBJ, EMPTYSET
from ..operations.color import COLOR
from ...fenvs import PLASM_INTERSECTION

__all__ = [
    "BINARYINTERSECTION",
    "INTERSECTION",
    "I",  # English alias
    "PRUNIK",  # Czech
    "PRZECIECIE",
    "PRZETNIJ",  # Polish
    "DURCHSCHNITT",
    "SCHNITT",  # German
    "INTERSECCION",  # Spanish
    "INTERSEZIONE",
    "INTERSECA",  # Italian
]


def BINARYINTERSECTION(a, b):
    if isinstance(a, list):
        raise ExceptionWT("Lists are not allowed in BINARYINTERSECTION().")
    if isinstance(b, list):
        raise ExceptionWT("Lists are not allowed in BINARYINTERSECTION().")
    col = a.getcolor()
    c = BASEOBJ(PLASM_INTERSECTION([a.geom, b.geom]))
    COLOR(c, col)
    return c


def intersection(*args):
    raise ExceptionWT(
        "Command intersection() is undefined. Try INTERSECTION() instead?"
    )


def INTERSECTION(a, b, warn=True):
    if isinstance(a, list):
        if a == []:
            raise ExceptionWT(
                "In your INTERSECTION command, the first object is empty."
            )
        a = flatten(a)
    if isinstance(b, list):
        if b == []:
            raise ExceptionWT(
                "In your INTERSECTION command, the second object is empty."
            )
        b = flatten(b)
    # a is single object, b is single object:
    if not isinstance(a, list) and not isinstance(b, list):
        res = BINARYINTERSECTION(a, b)
        if EMPTYSET(res) and warn == True:
            print("WARNING: Empty object created while intersecting objects.")
        return res
    # a is single object, b is a list:
    if not isinstance(a, list) and isinstance(b, list):
        res = []
        for y in b:
            res0 = BINARYINTERSECTION(a, y)
            if not EMPTYSET(res0):
                res.append(res0)
        if EMPTYSET(res) and warn == True:
            print("WARNING: Empty object created while intersecting objects.")
        return res
    # a is a list, b is single object:
    if isinstance(a, list) and not isinstance(b, list):
        res = []
        for x in a:
            res0 = BINARYINTERSECTION(x, b)
            if not EMPTYSET(res0):
                res.append(res0)
        if EMPTYSET(res) and warn == True:
            print("WARNING: Empty object created while intersecting objects.")
        return res
    # a is a list, b is a list:
    if isinstance(a, list) and isinstance(b, list):
        res = []
        for x in a:
            for y in b:
                res0 = BINARYINTERSECTION(x, y)
                if not EMPTYSET(res0):
                    res.append(res0)
        if EMPTYSET(res) and warn == True:
            print("WARNING: Empty object created while intersecting objects.")
        return res


def INTERSECTIONOLDUNUSED(*args):
    list1 = list(args)
    l = len(list1)
    if l < 2:
        raise ExceptionWT("INTERSECTION(...) requires at least two objects!")
    for i in range(1, l):
        if isinstance(list1[i], list):
            raise ExceptionWT(
                "Only the first argument of INTERSECTION(...) may be a struct (list)!"
            )

    item1 = list1[0]  # this is either a single item or a list
    if not isinstance(item1, list):
        geoms = []
        for x in list1:
            geoms.append(x.geom)
        obj = BASEOBJ(PLASM_INTERSECTION(geoms))
        obj.setcolor(list1[0].color)
        return obj
    else:
        item1 = list1.pop(0)
        item1flat = flatten(item1)
        result = []
        for x in item1flat:
            list1_new = [x] + list1
            geoms = []
            for y in list1_new:
                geoms.append(y.geom)
            obj = BASEOBJ(PLASM_INTERSECTION(geoms))
            obj.setcolor(list1_new[0].color)
            result.append(obj)
        return result


# English:
I = INTERSECTION

# Czech:
PRUNIK = INTERSECTION

# Polish:
PRZECIECIE = INTERSECTION
PRZETNIJ = INTERSECTION

# German:
DURCHSCHNITT = INTERSECTION
SCHNITT = INTERSECTION

# Spanish:
INTERSECCION = INTERSECTION

# Italian:
INTERSEZIONE = INTERSECTION
INTERSECA = INTERSECTION

# French:
INTERSECTION = INTERSECTION
