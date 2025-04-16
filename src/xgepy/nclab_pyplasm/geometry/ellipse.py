"""
Ellipse Module
"""


from nclab.tools import ExceptionWT
from ..utils.constants import Y
from ..geometry.circle import CIRCLE
from ..operations.scale import SCALE


__all__ = [
    "ellipse",
    "ELLIPSE",
    # Language variants
    "ELIPSA",
    "OVAL",  # Czech
    "ELIPSA",
    "OWAL",  # Polish
    "ELLIPSE",
    "OVAL",  # German
    "ELIPSE",
    "OVALO",  # Spanish
    "ELLISSE",
    "OVALE",  # Italian
    "ELLIPSE",
    "OVALE",  # French
]


def ellipse(*args):
    raise ExceptionWT("Command ellipse() is undefined. Try ELLIPSE() instead?")


def ELLIPSE(a, b, n=64):
    if a <= 0 or b <= 0:
        raise ExceptionWT("In ELLIPSE(a, b), both a and b must be positive!")
    if n < 3:
        raise ExceptionWT("Number of edges n in ELLIPSE(a, b, n) must be at least 3!")
    c = CIRCLE(a, n)
    SCALE(c, b / a, Y)
    return c


ELIPSA = ELLIPSE  # Ellipse
OVAL = ELLIPSE  # Oval

# Polish:
ELIPSA = ELLIPSE  # Ellipse
OWAL = ELLIPSE  # Oval

# German:
ELLIPSE = ELLIPSE  # Ellipse
OVAL = ELLIPSE  # Oval

# Spanish:
ELIPSE = ELLIPSE  # Ellipse
OVALO = ELLIPSE  # Oval

# Italian:
ELLISSE = ELLIPSE  # Ellipse
OVALE = ELLIPSE  # Oval

# French:
ELLIPSE = ELLIPSE  # Ellipse
OVALE = ELLIPSE  # Oval
