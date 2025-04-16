"""
Sphere Creation Module

This module provides functions for creating sphere objects with customizable resolution.
The SPHERE function creates a 3D sphere with specified radius and optional division parameters.
"""

from nclab.tools import ExceptionWT
from ..utils.common import ISNUMBER
from ..geometry.base import BASEOBJ
from ...fenvs import PLASM_JOIN, PLASM_SPHERE


def sphere(*args):
    raise ExceptionWT("Command sphere() is undefined. Try SPHERE() instead?")


def SPHERE(radius, divisions=[16, 32]):
    if not ISNUMBER(radius):
        raise ExceptionWT("Radius r in SPHERE(r) must be a number!")
    if radius <= 0:
        raise ExceptionWT("Radius r in SPHERE(r) must be positive!")
    divisionslist = divisions
    if not isinstance(divisions, list):
        if divisions < 4:
            raise ExceptionWT("Bad division in the SPHERE command!")
        divisionslist = [int(divisions / 2), divisions]
    # Returning the sphere:
    return BASEOBJ(PLASM_JOIN(PLASM_SPHERE(radius)(divisionslist)))


# Czech:
KOULE = SPHERE
# Polish:
KULA = SPHERE
SFERA = SPHERE
# German:
KUGEL = SPHERE
# Spanish:
ESFERA = SPHERE
# Italian:
SFERA = SPHERE


# French:
# Same as English

__all__ = [
    "sphere",
    "SPHERE",  # English
    "KOULE",  # Czech
    "KULA",
    "SFERA",  # Polish
    "KUGEL",  # German
    "ESFERA",  # Spanish
    "SFERA",  # Italian
]
