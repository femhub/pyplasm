"""
Icosahedron Geometry Module
"""

import math
from nclab.tools import ExceptionWT
from ..geometry.base import BASEOBJ
from ...fenvs import PLASM_T, CUBOID, PLASM_R, PI, PLASM_S, PLASM_JOIN

__all__ = [
    "icosahedron",
    "build_ICOSAHEDRON",
    "ICOSAHEDRON",
    # Language variants
    "IKOSAEDR",
    "IKOSAEDER",  # Czech/German
    "DWUDZIESTOSCIAN",  # Polish
    "ICOSAEDRO",  # Spanish/Italian
    "ICOSAEDRE",  # French
]


def icosahedron(*args):
    raise ExceptionWT("Command icosahedron() is undefined. Try ICOSAHEDRON() instead?")


def build_ICOSAHEDRON():
    g = 0.5 * (math.sqrt(5) - 1)
    b = 2.0 / (math.sqrt(5 * math.sqrt(5)))
    rectx = PLASM_T([1, 2])([-g, -1])(CUBOID([2 * g, 2]))
    recty = PLASM_R([1, 3])(PI / 2)(PLASM_R([1, 2])(PI / 2)(rectx))
    rectz = PLASM_R([2, 3])(PI / 2)(PLASM_R([1, 2])(PI / 2)(rectx))
    geom = PLASM_S([1, 2, 3])([b, b, b])(PLASM_JOIN([rectx, recty, rectz]))
    return BASEOBJ(geom)


# Main function
ICOSAHEDRON = build_ICOSAHEDRON()

# Language aliases
# Czech/German:
IKOSAEDR = ICOSAHEDRON  # Czech
IKOSAEDER = ICOSAHEDRON  # German

# Polish:
DWUDZIESTOSCIAN = ICOSAHEDRON  # twenty-sided figure

# Spanish/Italian:
ICOSAEDRO = ICOSAHEDRON  # icosahedron

# French:
ICOSAEDRE = ICOSAHEDRON  # icosahedron
