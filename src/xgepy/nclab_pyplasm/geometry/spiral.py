"""
Spiral Geometry Module
"""


from nclab.tools import ExceptionWT
from ..utils.common import flatten, ISNUMBER
from ..geometry.base import BASEOBJ
from ...fenvs import PLASM_REVOLVE

__all__ = [
    "spiral",
    "SPIRAL",
    # Language variants
    "SPIRALA",
    "ZAVIT",  # Czech
    "SPIRALA",
    "ZWIN",  # Polish
    "SPIRALE",
    "WENDEL",  # German
    "ESPIRAL",
    "HELICE",  # Spanish
    "SPIRALE",
    "ELICA",  # Italian
    "SPIRALE",
    "HELICE",  # French
]


def spiral(*args):
    raise ExceptionWT("Command spiral() is undefined. Try SPIRAL() instead?")


def SPIRAL(basis, angle, elevation, division=48):
    if not ISNUMBER(angle):
        raise ExceptionWT(
            "Angle in SPIRAL(base, angle, elevation, division) must be a number!"
        )
    if angle <= 0:
        raise ExceptionWT(
            "Angle in SPIRAL(base, angle, elevation, division) must be positive!"
        )
    if not isinstance(basis, list):
        if basis.dim != 2:
            raise ExceptionWT(
                "The base object in SPIRAL(base, angle, elevation, division) must be 2-dimensional!"
            )
        color = basis.getcolor()
        obj = BASEOBJ(PLASM_REVOLVE([basis, angle, elevation, division]))
        obj.setcolor(color)
        obj.dim = 3
        return obj
    else:
        basis = flatten(basis)
        for obj in basis:
            if obj.dim != 2:
                raise ExceptionWT(
                    "The base object in SPIRAL(base, angle, elevation, division) must be 2-dimensional!"
                )
        obj = []
        for oo in basis:
            color = oo.getcolor()
            oo3d = BASEOBJ(PLASM_REVOLVE([oo, angle, elevation, division]))
            oo3d.setcolor(color)
            oo3d.dim = 3
            obj.append(oo3d)
        return obj


# Czech:
SPIRALA = SPIRAL  # spiral
ZAVIT = SPIRAL  # coil

# Polish:
SPIRALA = SPIRAL  # spiral
ZWIN = SPIRAL  # coil

# German:
SPIRALE = SPIRAL  # spiral
WENDEL = SPIRAL  # coil

# Spanish:
ESPIRAL = SPIRAL  # spiral
HELICE = SPIRAL  # helix

# Italian:
SPIRALE = SPIRAL  # spiral
ELICA = SPIRAL  # helix

# French:
SPIRALE = SPIRAL  # spiral
HELICE = SPIRAL  # helix
