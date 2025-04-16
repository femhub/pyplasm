"""
Bezier Curve Geometry Module
"""

from nclab.tools import ExceptionWT
from ...fenvs import PLASM_BEZIER, S1, S2, S3

__all__ = [
    "bezier1",
    "bezier2",
    "bezier3",
    "BEZIER1",
    "BEZIER2",
    "BEZIER3",
    "BEZIER",
    "BEZIERX",
    "BE1",  # X-axis aliases
    "BEZIERY",
    "BE2",  # Y-axis aliases
    "BEZIERZ",
    "BE3",  # Z-axis aliases
    # Language variants
    "BEZIEROVA1",
    "BEZIEROVA2",
    "BEZIEROVA3",  # Czech
    "BEZIEROWA1",
    "BEZIEROWA2",
    "BEZIEROWA3",  # Polish
    "BEZIER1",
    "BEZIER2",
    "BEZIER3",  # German
    "BEZIER1",
    "BEZIER2",
    "BEZIER3",  # Spanish
    "BEZIER1",
    "BEZIER2",
    "BEZIER3",  # Italian
    "BEZIER1",
    "BEZIER2",
    "BEZIER3",  # French
]


def bezier1(*args):
    raise ExceptionWT("Command bezier1() is undefined. Try BEZIER1() instead?")


def BEZIER1(*args):
    list1 = list(args)
    if len(list1) <= 1:
        raise ExceptionWT("BEZIER curve expects at least two control points!")
    return PLASM_BEZIER(S1)(list1)


def bezier2(*args):
    raise ExceptionWT("Command bezier2() is undefined. Try BEZIER2() instead?")


def BEZIER2(*args):
    list1 = list(args)
    if len(list1) <= 1:
        raise ExceptionWT("BEZIER curve expects at least two control points!")
    return PLASM_BEZIER(S2)(list1)


def bezier3(*args):
    raise ExceptionWT("Command bezier3() is undefined. Try BEZIER3() instead?")


def BEZIER3(*args):
    list1 = list(args)
    if len(list1) <= 1:
        raise ExceptionWT("BEZIER curve expects at least two control points!")
    return PLASM_BEZIER(S3)(list1)


# X-axis aliases
BEZIER = BEZIER1  # General Bezier curve
BEZIERX = BEZIER1  # X-axis specific
BE1 = BEZIER1  # Short form

# Y-axis aliases
BEZIERY = BEZIER2  # Y-axis specific
BE2 = BEZIER2  # Short form

# Z-axis aliases
BEZIERZ = BEZIER3  # Z-axis specific
BE3 = BEZIER3  # Short form

# Language variants
# Czech:
BEZIEROVA1 = BEZIER1  # Bezier curve 1
BEZIEROVA2 = BEZIER2  # Bezier curve 2
BEZIEROVA3 = BEZIER3  # Bezier curve 3

# Polish:
BEZIEROWA1 = BEZIER1  # Bezier curve 1
BEZIEROWA2 = BEZIER2  # Bezier curve 2
BEZIEROWA3 = BEZIER3  # Bezier curve 3

# German:
BEZIER1 = BEZIER1  # Bezier curve 1
BEZIER2 = BEZIER2  # Bezier curve 2
BEZIER3 = BEZIER3  # Bezier curve 3

# Spanish:
BEZIER1 = BEZIER1  # Bezier curve 1
BEZIER2 = BEZIER2  # Bezier curve 2
BEZIER3 = BEZIER3  # Bezier curve 3

# Italian:
BEZIER1 = BEZIER1  # Bezier curve 1
BEZIER2 = BEZIER2  # Bezier curve 2
BEZIER3 = BEZIER3  # Bezier curve 3

# French:
BEZIER1 = BEZIER1  # Bezier curve 1
BEZIER2 = BEZIER2  # Bezier curve 2
BEZIER3 = BEZIER3  # Bezier curve 3
