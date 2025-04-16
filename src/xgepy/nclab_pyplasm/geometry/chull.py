"""
Convex Hull Operations Module

This module provides functions for computing the convex hull of a set of points.
"""


from nclab.tools import ExceptionWT
from ..geometry.base import BASEOBJ
from ...fenvs import PLASM_CONVEXHULL


def chull(*args):
    raise ExceptionWT("Command chull() is undefined. Try CHULL() instead?")


def CHULL(*args):
    list1 = list(args)
    # User supplied a list of points
    if len(list1) == 1 and isinstance(list1[0], list) and isinstance(list1[0][0], list):
        list1 = list1[0]
    if len(list1) <= 2:
        raise ExceptionWT("CHULL(...) requires at least three points!")
    return BASEOBJ(PLASM_CONVEXHULL(list1))


# English:
CONVEXHULL = CHULL
CONVEX = CHULL
CH = CHULL
SPAN = CHULL
# Czech:
KONVEXNIOBAL = CHULL
KONVEX = CHULL
OBAL = CHULL
KOBAL = CHULL
# Polish:
OTOCZKAWYPUKLA = CHULL
OTOCZKA = CHULL
# German:
HUELLE = CHULL
HULLE = CHULL
SPANNE = CHULL
# Spanish:
CASCO = CHULL
CONVEXA = CHULL
# Italian:
CONVESSO = CHULL
SPANNA = CHULL
# French:
CONVEXE = CHULL
ENVELOPPE = CHULL
DUREE = CHULL

__all__ = [
    "chull",
    "CHULL",
    "CONVEXHULL",
    "CONVEX",
    "CH",
    "SPAN",
    # Language variants
    "KONVEXNIOBAL",
    "KONVEX",
    "OBAL",
    "KOBAL",  # Czech
    "OTOCZKAWYPUKLA",
    "OTOCZKA",  # Polish
    "HUELLE",
    "HULLE",
    "SPANNE",  # German
    "CASCO",
    "CONVEXA",  # Spanish
    "CONVESSO",
    "SPANNA",  # Italian
    "CONVEXE",
    "ENVELOPPE",
    "DUREE",  # French
]
