"""
Geometry Arrangement Module
"""

from nclab.tools import ExceptionWT
from ..operations.union import UNION
from ..operations.rotate import ROTATE
from ..operations.move import MOVE


__all__ = [
    "top",
    "TOP",  # Top placement
    "bottom",
    "BOTTOM",  # Bottom placement
    "left",
    "LEFT",  # Left placement
    "right",
    "RIGHT",  # Right placement
    "front",
    "FRONT",  # Front placement
    "rear",
    "REAR",  # Rear placement
]


def top(*args):
    raise ExceptionWT("Command top() is undefined. Try TOP() instead?")


def TOP(obj1, obj2):  # obj2 goes on top of obj1
    if isinstance(obj2, list):
        raise ExceptionWT("Second argument of TOP(...) may not be a list!")
    if not isinstance(obj1, list):
        # z-direction:
        maxz1 = obj1.maxz()
        minz2 = obj2.minz()
        MOVE(obj2, 0, 0, maxz1 - minz2)
        # x-direction:
        cx1 = 0.5 * (obj1.minx() + obj1.maxx())
        cx2 = 0.5 * (obj2.minx() + obj2.maxx())
        MOVE(obj2, cx1 - cx2, 0, 0)
        # y-direction:
        cy1 = 0.5 * (obj1.miny() + obj1.maxy())
        cy2 = 0.5 * (obj2.miny() + obj2.maxy())
        MOVE(obj2, 0, cy1 - cy2, 0)
        return UNION(obj1, obj2)
    else:
        maxx1 = obj1[0].maxx()
        minx1 = obj1[0].minx()
        maxy1 = obj1[0].maxy()
        miny1 = obj1[0].miny()
        maxz1 = obj1[0].maxz()
        minz1 = obj1[0].minz()
        for x in obj1:
            if x.maxx() > maxx1:
                maxx1 = x.maxx()
            if x.minx() < minx1:
                minx1 = x.minx()
            if x.maxy() > maxy1:
                maxy1 = x.maxy()
            if x.miny() < miny1:
                miny1 = x.miny()
            if x.maxz() > maxz1:
                maxz1 = x.maxz()
            if x.minz() < minz1:
                minz1 = x.minz()
        # z-direction:
        minz2 = obj2.minz()
        MOVE(obj2, 0, 0, maxz1 - minz2)
        # x-direction:
        cx1 = 0.5 * (minx1 + maxx1)
        cx2 = 0.5 * (obj2.minx() + obj2.maxx())
        MOVE(obj2, cx1 - cx2, 0, 0)
        # y-direction:
        cy1 = 0.5 * (miny1 + maxy1)
        cy2 = 0.5 * (obj2.miny() + obj2.maxy())
        MOVE(obj2, 0, cy1 - cy2, 0)
        return UNION(obj1, obj2)


def bottom(*args):
    raise ExceptionWT("Command bottom() is undefined. Try BOTTOM() instead?")


def BOTTOM(obj1, obj2):
    ROTATE(obj1, 180, 1)
    ROTATE(obj2, 180, 1)
    TOP(obj1, obj2)
    ROTATE(obj1, -180, 1)
    ROTATE(obj2, -180, 1)
    return UNION(obj1, obj2)


# MOVE THE SECOND OBJECT TO BE CENTERED ON THE LEFT OF THE FIRST ONE


def left(*args):
    raise ExceptionWT("Command left() is undefined. Try LEFT() instead?")


def LEFT(obj1, obj2):
    ROTATE(obj1, -90, 2)
    ROTATE(obj2, -90, 2)
    TOP(obj1, obj2)
    ROTATE(obj1, 90, 2)
    ROTATE(obj2, 90, 2)
    return UNION(obj1, obj2)


# MOVE THE SECOND OBJECT TO BE CENTERED ON THE RIGHT OF THE FIRST ONE


def right(*args):
    raise ExceptionWT("Command right() is undefined. Try RIGHT() instead?")


def RIGHT(obj1, obj2):
    ROTATE(obj1, 90, 2)
    ROTATE(obj2, 90, 2)
    TOP(obj1, obj2)
    ROTATE(obj1, -90, 2)
    ROTATE(obj2, -90, 2)
    return UNION(obj1, obj2)


# MOVE THE SECOND OBJECT TO BE CENTERED ON THE FRONT OF THE FIRST ONE


def front(*args):
    raise ExceptionWT("Command front() is undefined. Try FRONT() instead?")


def FRONT(obj1, obj2):
    ROTATE(obj1, -90, 1)
    ROTATE(obj2, -90, 1)
    TOP(obj1, obj2)
    ROTATE(obj1, 90, 1)
    ROTATE(obj2, 90, 1)
    return UNION(obj1, obj2)


# MOVE THE SECOND OBJECT TO BE CENTERED ON THE REAR OF THE FIRST ONE


def rear(*args):
    raise ExceptionWT("Command rear() is undefined. Try REAR() instead?")


def REAR(obj1, obj2):
    ROTATE(obj1, 90, 1)
    ROTATE(obj2, 90, 1)
    TOP(obj1, obj2)
    ROTATE(obj1, -90, 1)
    ROTATE(obj2, -90, 1)
    return UNION(obj1, obj2)
