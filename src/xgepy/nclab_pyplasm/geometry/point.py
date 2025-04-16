"""
POINT MODULE
"""

from nclab.tools import ExceptionWT
from ..utils.common import flatten


__all__ = ["POINT"]


def POINT(*args):
    L = flatten(*args)
    d = len(L)
    if d != 2 and d != 3:
        raise ExceptionWT(
            "2D points are created as POINT(x, y), 3D points as POINT(x, y, z)!"
        )
    # return the list:
    return L
