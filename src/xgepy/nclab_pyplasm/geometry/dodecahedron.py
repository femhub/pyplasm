"""
Dodecahedron Geometry Module
"""

import math

from nclab.tools import ExceptionWT
from ..geometry.base import BASEOBJ
from ...fenvs import (
    MKPOL,
    EMBED,
    CUBOID,
    PLASM_T,
    PLASM_JOIN,
    PLASM_STRUCT,
    PLASM_R,
    PI,
    PLASM_S,
    Plasm,
)

# Public API
__all__ = [
    "dodecahedron",
    "build_DODECAHEDRON",
    "DODECAHEDRON",
    # Language variants
    "DODEKAEDR",
    "DODEKAEDER",  # Czech/German
    "DWUNASTOSCIAN",  # Polish
    "DODECAEDRO",  # Spanish/Italian
    "DODECAEDRE",  # French
]


def dodecahedron(*args):
    raise ExceptionWT(
        "Command dodecahedron() is undefined. Try DODECAHEDRON() instead?"
    )


def build_DODECAHEDRON():
    a = 1.0 / (math.sqrt(3.0))
    g = 0.5 * (math.sqrt(5.0) - 1)
    top = MKPOL([[[1 - g, 1, 0 - g], [1 + g, 1, 0 - g]], [[1, 2]], [[1]]])
    basis = EMBED(1)(CUBOID([2, 2]))
    roof = PLASM_T([1, 2, 3])([-1, -1, -1])(PLASM_JOIN([basis, top]))
    roofpair = PLASM_STRUCT([roof, PLASM_R([2, 3])(PI), roof])
    geom = PLASM_S([1, 2, 3])([a, a, a])(
        PLASM_STRUCT(
            [
                Plasm.cube(3, -1, +1),
                roofpair,
                PLASM_R([1, 3])(PI / 2),
                PLASM_R([1, 2])(PI / 2),
                roofpair,
                PLASM_R([1, 2])(PI / 2),
                PLASM_R([2, 3])(PI / 2),
                roofpair,
            ]
        )
    )
    return BASEOBJ(geom)


# Main function
DODECAHEDRON = build_DODECAHEDRON()

# Language aliases
# Czech/German:
DODEKAEDR = DODECAHEDRON  # Czech
DODEKAEDER = DODECAHEDRON  # German

# Polish:
DWUNASTOSCIAN = DODECAHEDRON  # twelve-sided figure

# Spanish/Italian:
DODECAEDRO = DODECAHEDRON  # dodecahedron

# French:
DODECAEDRE = DODECAHEDRON  # dodecahedron
