"""
Reference Domain Module
"""

from nclab.tools import ExceptionWT
from ..geometry.base import BASEOBJ
from ..operations.get_dim import GETDIM
from ..geometry.bounds import MINX, MINY, MINZ, MAXX, MAXY, MAXZ
from ...fenvs import SIMPLEXGRID

__all__ = [
    "refdomain",
    "REFDOMAIN",
    "refdomain3d",
    "REFDOMAIN3D",
    # Unit domains
    "unitsquare",
    "UNITSQUARE",
    "unitcube",
    "UNITCUBE",
    # Measurement functions
    "PRINTSIZE",
    "EXTREMA",
    "EXTREMS",
    "EXTREMES",
    # Language variants for EXTREMA
    "EXTREMY",
    "EXTREMA",  # Czech
    "EKSTREMA",
    "EKSTREMY",  # Polish
    "EXTREMA",
    "EXTREMEN",  # German
    "EXTREMOS",
    "EXTREMAS",  # Spanish
    "ESTREMI",
    "ESTREMA",  # Italian
    "EXTREMES",
    "EXTREMA",  # French
]


def refdomain(*args):
    raise ExceptionWT("Command refdomain() is undefined. Try REFDOMAIN() instead?")


def REFDOMAIN(a, b, m, n):
    # return POWER(INTERVALS(a, m), INTERVALS(b, n))
    return BASEOBJ(SIMPLEXGRID([a, b])([m, n]))


def refdomain3d(*args):
    raise ExceptionWT("Command refdomain3d() is undefined. Try REFDOMAIN3D() instead?")


def REFDOMAIN3D(a, b, c, m, n, o):
    # return POWER(INTERVALS(a, m), INTERVALS(b, n))
    return BASEOBJ(SIMPLEXGRID([a, b, c])([m, n, o]))


def unitsquare(*args):
    raise ExceptionWT("Command unitsquare() is undefined. Try UNITSQUARE() instead?")


def UNITSQUARE(m, n):
    # return POWER(INTERVALS(1.0, n), INTERVALS(1.0, m))
    return BASEOBJ(SIMPLEXGRID([1.0, 1.0])([m, n]))


def unitcube(*args):
    raise ExceptionWT("Command unitcube() is undefined. Try UNITCUBE() instead?")


def UNITCUBE(m, n, o):
    # return POWER(INTERVALS(1.0, n), INTERVALS(1.0, m))
    return BASEOBJ(SIMPLEXGRID([1.0, 1.0, 1.0])([m, n, o]))


def PRINTSIZE(obj):
    minx = MINX(obj)
    maxx = MAXX(obj)
    miny = MINY(obj)
    maxy = MAXY(obj)
    minz = MINZ(obj)
    maxz = MAXZ(obj)
    print(("SIZE:", maxx - minx, maxy - miny, maxz - minz))
    print(("BBOX:", minx, maxx, miny, maxy, minz, maxz))


# Returns extrema, rounded to 3 digits:


def EXTREMA(obj):
    ddd = GETDIM(obj)
    if ddd == -1:
        raise ExceptionWT("EXTREMA() can be used for 3D objects only.")
    minx = MINX(obj)
    maxx = MAXX(obj)
    miny = MINY(obj)
    maxy = MAXY(obj)
    minz = 0
    maxz = 0
    if ddd == 3:
        minz = MINZ(obj)
        maxz = MAXZ(obj)
    # Rounding:
    minx = (int)(1000 * minx + 0.5) / 1000.0
    maxx = (int)(1000 * maxx + 0.5) / 1000.0
    miny = (int)(1000 * miny + 0.5) / 1000.0
    maxy = (int)(1000 * maxy + 0.5) / 1000.0
    if ddd == 3:
        minz = (int)(1000 * minz + 0.5) / 1000.0
        maxz = (int)(1000 * maxz + 0.5) / 1000.0
    print(("X:", minx, maxx))
    print(("Y:", miny, maxy))
    if ddd == 3:
        print(("Z:", minz, maxz))


# English aliases
EXTREMS = EXTREMA
EXTREMES = EXTREMA

# Czech:
EXTREMY = EXTREMA  # Extrema
EXTREMA = EXTREMA  # Extrema

# Polish:
EKSTREMA = EXTREMA  # Extrema
EKSTREMY = EXTREMA  # Extrema

# German:
EXTREMA = EXTREMA  # Extrema
EXTREMEN = EXTREMA  # Extrema

# Spanish:
EXTREMOS = EXTREMA  # Extrema
EXTREMAS = EXTREMA  # Extrema

# Italian:
ESTREMI = EXTREMA  # Extrema
ESTREMA = EXTREMA  # Extrema

# French:
EXTREMES = EXTREMA  # Extrema
EXTREMA = EXTREMA  # Extrema
