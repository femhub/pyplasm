"""
Extrusion Module
"""


from nclab.tools import ExceptionWT
from ..utils.common import flatten
from ..geometry.base import BASEOBJ
from ..geometry.prism import PRISM
from ..operations.rotate import ROTATE
from ..operations.move import MOVE
from ..operations.scale import SCALE
from ...fenvs import PI, PLASM_EXTRUSION


__all__ = [
    "extrude",
    "EXTRUDE",
    "EXT",
    "E",
    # Language variants
    "VYTLACIT",
    "VYTLAK",  # Czech
    "WYTŁOCZYC",
    "WYTŁOK",  # Polish
    "EXTRUDIEREN",
    "EXTRUSION",  # German
    "EXTRUIR",
    "EXTRUSION",  # Spanish
    "ESTRUDERE",
    "ESTRUSIONE",  # Italian
    "EXTRUDER",
    "EXTRUSION",  # French
]


def EXTRUDEONE(shape2d, height, angle_deg, n=1):
    if shape2d.dim != 2:
        raise ExceptionWT(
            "Base object in EXTRUDE(base, height, angle, n) must be 2-dimensional!"
        )
    if height <= 0:
        raise ExceptionWT(
            "Extrusion height in EXTRUDE(base, height, angle, n) must be positive!"
        )
    col = shape2d.getcolor()
    dh = float(height) / n
    angle_rad = angle_deg * PI / 180.0
    da = float(angle_rad) / n
    dangle = da * 180.0 / PI
    L = []
    for i in range(0, n):
        newlayer = BASEOBJ(PLASM_EXTRUSION(da)(1)(shape2d.geom))
        COLOR(newlayer, col)
        SCALE(newlayer, 1, 1, dh)
        MOVE(newlayer, 0, 0, i * dh)
        ROTATE(newlayer, i * dangle, 3)
        newlayer.dim = 3
        L.append(newlayer)
    return L  # I tried to return a union but it took too much time


def extrude(*args):
    raise ExceptionWT("Command extrude() is undefined. Try EXTRUDE() instead?")


def EXTRUDE(*args):
    arglist = list(args)
    if len(arglist) < 2:
        raise ExceptionWT("EXTRUDE(base, height, ...) takes at least two arguments!")
    basis = arglist[0]
    height = arglist[1]
    if height <= 0:
        raise ExceptionWT("Height in EXTRUDE(base, height, ...) must be positive!")
    if len(arglist) == 2:
        return PRISM(basis, height)
    angle_deg = 0
    if len(arglist) >= 3:
        angle_deg = arglist[2]
    n = 1
    if len(arglist) >= 4:
        n = arglist[3]
    # Check that the basis is two-dimensional:
    if not isinstance(basis, list):
        if basis.dim != 2:
            raise ExceptionWT(
                "The base object in EXTRUDE(base, height, angle, n) must be 2-dimensional!"
            )
        color = basis.getcolor()
        oo3d = EXTRUDEONE(basis, height, angle_deg, n)
        for a in oo3d:
            a.setcolor(color)
        return oo3d
    else:
        basis = flatten(basis)
        for obj in basis:
            if obj.dim != 2:
                raise ExceptionWT(
                    "The base object in EXTRUDE(base, height, angle, n) must be 2-dimensional!"
                )
        obj = []
        for oo in basis:
            color = oo.getcolor()
            oo3d = EXTRUDEONE(oo, height, angle_deg, n)
            for a in oo3d:
                a.setcolor(color)
            obj.append(oo3d)
        obj = flatten(obj)
        return obj


EXT = EXTRUDE  # Short form
E = EXTRUDE  # Shortest form

# Language variants
# Czech:
VYTLACIT = EXTRUDE  # Extrude
VYTLAK = EXTRUDE  # Extrusion

# Polish:
WYTŁOCZYC = EXTRUDE  # Extrude
WYTŁOK = EXTRUDE  # Extrusion

# German:
EXTRUDIEREN = EXTRUDE  # Extrude
EXTRUSION = EXTRUDE  # Extrusion

# Spanish:
EXTRUIR = EXTRUDE  # Extrude
EXTRUSION = EXTRUDE  # Extrusion

# Italian:
ESTRUDERE = EXTRUDE  # Extrude
ESTRUSIONE = EXTRUDE  # Extrusion

# French:
EXTRUDER = EXTRUDE  # Extrude
EXTRUSION = EXTRUDE  # Extrusion
