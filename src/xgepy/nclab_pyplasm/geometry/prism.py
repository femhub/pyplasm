"""
Prism Creation Module

This module provides functions for creating prism objects by extruding 2D bases.
The PRISM function creates a 3D object by extruding a 2D base object along the Z-axis.
"""


from nclab.tools import ExceptionWT
from ..utils.common import flatten
from ..geometry.grid import GRID
from ..geometry.base import BASEOBJ
from ..operations.product import PRODUCT


__all__ = [
    "prism",
    "PRISM",
    "HRANOL",  # Czech
    "PRYZMA",
    "PRYZMAT",  # Polish
    "PRISMA",  # German
    "PRISMA",  # Spanish
    "PRISMA",  # Italian
    "PRISME",  # French
]


def prism(*args):
    raise ExceptionWT("Command prism() is undefined. Try PRISM() instead?")


def PRISM(basis, h, n=1):
    if h <= 0:
        raise ExceptionWT("Height in PRISM(base, height) must be positive!")
    # Grid list (points in the Z direction)
    h0 = float(h) / n
    gridlist = [h0 for i in range(n)]
    # Check that the basis is two-dimensional:
    if not isinstance(basis, list):
        if not isinstance(basis, BASEOBJ):
            raise ExceptionWT(
                "The base object in PRISM(base, height) must be a 2D object in the XY plane!"
            )
        if basis.dim != 2:
            raise ExceptionWT(
                "The base object in PRISM(base, height) must be a 2D object in the XY plane!"
            )
        color = basis.getcolor()
        obj = PRODUCT(basis, GRID(*gridlist))  # PRODUCT returns a class instance!
        obj.setcolor(color)
        obj.dim = 3
        return obj
    else:
        basis = flatten(basis)
        for obj in basis:
            if not isinstance(obj, BASEOBJ):
                raise ExceptionWT(
                    "The base object in PRISM(base, height) must be a 2D object in the XY plane!"
                )
            if obj.dim != 2:
                raise ExceptionWT(
                    "The base object in PRISM(base, height) must be a 2D object in the XY plane!"
                )
        obj = []
        for oo in basis:
            color = oo.getcolor()
            oo3d = PRODUCT(oo, GRID(*gridlist))  # PRODUCT returns a class instance!
            oo3d.setcolor(color)
            oo3d.dim = 3
            obj.append(oo3d)
        return obj


# English:
PRISM = PRISM

# Czech:
HRANOL = PRISM

# Polish:
PRYZMA = PRISM
PRYZMAT = PRISM

# German:
PRISMA = PRISM

# Spanish:
PRISMA = PRISM

# Italian:
PRISMA = PRISM

# French:
PRISME = PRISM
