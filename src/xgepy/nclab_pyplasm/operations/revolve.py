"""
REVOLVE MODULE
"""

from nclab.tools import ExceptionWT
from ..utils.common import flatten, ISNUMBER
from ..geometry.base import BASEOBJ
from ...fenvs import PLASM_REVOLVE

__all__ = ["revolve", "REVOLVE"]


def revolve(*args):
    raise ExceptionWT("Command revolve() is undefined. Try REVOLVE() instead?")


def REVOLVE(basis, angle, division=48):
    if not ISNUMBER(angle):
        raise ExceptionWT("Angle in REVOLVE(base, angle, division) must be a number!")
    if angle <= 0:
        raise ExceptionWT("Angle in REVOLVE(base, angle, division) must be positive!")
    if not isinstance(basis, list):
        if basis.dim != 2:
            raise ExceptionWT(
                "The base object in REVOLVE(base, angle, division) must be 2-dimensional!"
            )
        color = basis.getcolor()
        elevation = 0
        obj = BASEOBJ(PLASM_REVOLVE([basis, angle, elevation, division]))
        obj.setcolor(color)
        return obj
    else:
        basis = flatten(basis)
        for obj in basis:
            if obj.dim != 2:
                raise ExceptionWT(
                    "The base object in REVOLVE(base, angle, division) must be 2-dimensional!"
                )
        obj = []
        for oo in basis:
            color = oo.getcolor()
            elevation = 0
            oo3d = BASEOBJ(PLASM_REVOLVE([oo, angle, elevation, division]))
            oo3d.setcolor(color)
            obj.append(oo3d)
        return obj
