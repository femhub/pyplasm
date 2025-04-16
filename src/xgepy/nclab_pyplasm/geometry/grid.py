"""
Grid Creation Module

This module provides functions for creating grid objects based on interval sequences.
The GRID function creates a 1D grid structure from a sequence of interval lengths.
"""

from nclab.tools import ExceptionWT
from ..utils.common import flatten
from ..geometry.base import BASEOBJ
from ...fenvs import plasm_config, CAT, Plasm


__all__ = [
    "grid",
    "GRID",
    "QUOTE",
    # Language variants
    "SIT",
    "MRIZ",  # Czech
    "SIATKA",  # Polish
    "GITTER",
    "NETZ",  # German
    "REJILLA",
    "CUADRICULA",  # Spanish
    "GRIGLIA",  # Italian
    "GRILLE",  # French
]


def grid(*args):
    raise ExceptionWT("Command grid() is undefined. Try GRID() instead?")


def GRID(*args):
    sequence = flatten(*args)
    if len(sequence) == 0:
        raise ExceptionWT("GRID(...) requires at least one interval length!")
    cursor, points, hulls = (0, [[0]], [])
    for value in sequence:
        points = points + [[cursor + abs(value)]]
        if value >= 0:
            hulls += [[len(points) - 2, len(points) - 1]]
        cursor = cursor + abs(value)
    obj = BASEOBJ(Plasm.mkpol(1, CAT(points), hulls, plasm_config.tolerance()))
    return obj


# English:
QUOTE = GRID

# Czech:
SIT = GRID
MRIZ = GRID

# Polish:
SIATKA = GRID

# German:
GITTER = GRID
NETZ = GRID

# Spanish:
REJILLA = GRID
CUADRICULA = GRID

# Italian:
GRIGLIA = GRID

# French:
GRILLE = GRID
