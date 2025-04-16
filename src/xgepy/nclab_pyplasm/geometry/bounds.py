"""
Coordinate Bounds Module

This module provides functions for calculating the minimum and maximum coordinates
of geometric objects along the X, Y, and Z axes.
"""

from nclab.tools import ExceptionWT
from ..utils.common import flatten
from ..geometry.base import EMPTYSET


def minx(*args):
    raise ExceptionWT("Command minx() is undefined. Try MINX() instead?")


def MINX(obj):
    if isinstance(obj, list):
        obj = flatten(obj)
        for oo in obj:
            if EMPTYSET(oo):
                raise ExceptionWT("Cannot calculate MINX() of an empty set.")
        minx = obj[0].minx()
        n = len(obj)
        for i in range(1, n):
            if obj[i].minx() < minx:
                minx = obj[i].minx()
        return minx
    else:
        if EMPTYSET(obj):
            raise ExceptionWT("Cannot calculate MINX() of an empty set.")
        else:
            return obj.minx()


def miny(*args):
    raise ExceptionWT("Command miny() is undefined. Try MINY() instead?")


def MINY(obj):
    if isinstance(obj, list):
        obj = flatten(obj)
        for oo in obj:
            if EMPTYSET(oo):
                raise ExceptionWT("Cannot calculate MINY() of an empty set.")
        miny = obj[0].miny()
        n = len(obj)
        for i in range(1, n):
            if obj[i].miny() < miny:
                miny = obj[i].miny()
        return miny
    else:
        if EMPTYSET(obj):
            raise ExceptionWT("Cannot calculate MINY() of an empty set.")
        else:
            return obj.miny()


def minz(*args):
    raise ExceptionWT("Command minz() is undefined. Try MINZ() instead?")


def MINZ(obj):
    if isinstance(obj, list):
        obj = flatten(obj)
        for oo in obj:
            if EMPTYSET(oo):
                raise ExceptionWT("Cannot calculate MINZ() of an empty set.")
        minz = obj[0].minz()
        n = len(obj)
        for i in range(1, n):
            if obj[i].minz() < minz:
                minz = obj[i].minz()
        return minz
    else:
        if EMPTYSET(obj):
            raise ExceptionWT("Cannot calculate MINZ() of an empty set.")
        else:
            return obj.minz()


def maxx(*args):
    raise ExceptionWT("Command maxx() is undefined. Try MAXX() instead?")


def MAXX(obj):
    if isinstance(obj, list):
        obj = flatten(obj)
        for oo in obj:
            if EMPTYSET(oo):
                raise ExceptionWT("Cannot calculate MAXX() of an empty set.")
        maxx = obj[0].maxx()
        n = len(obj)
        for i in range(1, n):
            if obj[i].maxx() > maxx:
                maxx = obj[i].maxx()
        return maxx
    else:
        if EMPTYSET(obj):
            raise ExceptionWT("Cannot calculate MAXX() of an empty set.")
        else:
            return obj.maxx()


def maxy(*args):
    raise ExceptionWT("Command maxy() is undefined. Try MAXY() instead?")


def MAXY(obj):
    if isinstance(obj, list):
        obj = flatten(obj)
        for oo in obj:
            if EMPTYSET(oo):
                raise ExceptionWT("Cannot calculate MAXY() of an empty set.")
        maxy = obj[0].maxy()
        n = len(obj)
        for i in range(1, n):
            if obj[i].maxy() > maxy:
                maxy = obj[i].maxy()
        return maxy
    else:
        if EMPTYSET(obj):
            raise ExceptionWT("Cannot calculate MAXY() of an empty set.")
        else:
            return obj.maxy()


def maxz(*args):
    raise ExceptionWT("Command maxz() is undefined. Try MAXZ() instead?")


def MAXZ(obj):
    if isinstance(obj, list):
        obj = flatten(obj)
        for oo in obj:
            if EMPTYSET(oo):
                raise ExceptionWT("Cannot calculate MAXZ() of an empty set.")
        maxz = obj[0].maxz()
        n = len(obj)
        for i in range(1, n):
            if obj[i].maxz() > maxz:
                maxz = obj[i].maxz()
        return maxz
    else:
        if EMPTYSET(obj):
            raise ExceptionWT("Cannot calculate MAXZ() of an empty set.")
        else:
            return obj.maxz()


__all__ = [
    "MINX",
    "MAXX",  # X-axis bounds
    "MINY",
    "MAXY",  # Y-axis bounds
    "MINZ",
    "MAXZ",  # Z-axis bounds
]
