"""
Cylinder Geometry Module
"""

from nclab.tools import ExceptionWT
from ..utils.common import ISNUMBER
from ..geometry.base import BASEOBJ
from ...fenvs import PLASM_CYLINDER

__all__ = [
    "cylinder",
    "CYLINDER",
    "CYL",
    # Language variants
    "VALEC",  # Czech
    "CYLINDER",  # Polish
    "ZYLINDER",
    "ZYL",  # German
    "CILINDRO",
    "CIL",  # Spanish
    "CILINDRO",
    "CIL",  # Italian
    "CYLINDRE",  # French
]


def cylinder(*args):
    raise ExceptionWT("Command cylinder() is undefined. Try CYLINDER() instead?")


def CYLINDER(r, h, division=48):
    if not ISNUMBER(r):
        raise ExceptionWT("Radius r in CYLINDER(r, h) must be a number!")
    if not ISNUMBER(h):
        raise ExceptionWT("Height h in CYLINDER(r, h) must be a number!")
    if r <= 0:
        raise ExceptionWT("Radius r in CYLINDER(r, h) must be positive!")
    if h <= 0:
        raise ExceptionWT("Height h in CYLINDER(r, h) must be positive!")
    if division < 3:
        raise ExceptionWT("Number of sides n in CYLINDER(r, h, n) must be at least 3!")
    return BASEOBJ(PLASM_CYLINDER([r, h])(division))


CYL = CYLINDER  # short form

# Czech:
VALEC = CYLINDER  # cylinder

# Polish:
CYLINDER = CYLINDER  # same as English

# German:
ZYLINDER = CYLINDER  # cylinder
ZYL = CYLINDER  # short form

# Spanish:
CILINDRO = CYLINDER  # cylinder
CIL = CYLINDER  # short form

# Italian:
CILINDRO = CYLINDER  # cylinder
CIL = CYLINDER  # short form

# French:
CYLINDRE = CYLINDER  # cylinder
