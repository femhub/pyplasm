"""
Quadrilateral Geometry Module
"""

from nclab.tools import ExceptionWT
from ..geometry.base import BASEOBJ
from ...fenvs import PLASM_CONVEXHULL

__all__ = [
    "quadrilateral",
    "quad",
    "QUAD",
    "QUADRILATERAL",
    # Language variants
    "CTYRUHELNIK",  # Czech
    "CZWOROBOK",  # Polish
    "VIERECK",  # German
    "CUADRILATERO",  # Spanish
    "QUADRILATERO",  # Italian
    "QUADRILATERE",  # French
]


def quadrilateral(*args):
    raise ExceptionWT(
        "Command quadrilateral() is undefined. Try QUADRILATERAL() instead?"
    )


def quad(*args):
    raise ExceptionWT("Command quad() is undefined. Try QUAD() instead?")


def QUAD(a, b, c, d):
    if not isinstance(a, list):
        raise ExceptionWT(
            "First argument a in QUAD(a, b, c, d) must either be a 2D point [x, y] or a 3D point [x, y, z]."
        )
    if not isinstance(b, list):
        raise ExceptionWT(
            "Second argument b in QUAD(a, b, c, d) must either be a 2D point [x, y] or a 3D point [x, y, z]."
        )
    if not isinstance(c, list):
        raise ExceptionWT(
            "Third argument c in QUAD(a, b, c, d) must either be a 2D point [x, y] or a 3D point [x, y, z]."
        )
    if not isinstance(d, list):
        raise ExceptionWT(
            "Fourth argument d in QUAD(a, b, c, d) must either be a 2D point [x, y] or a 3D point [x, y, z]."
        )
    la = len(a)
    lb = len(b)
    lc = len(c)
    ld = len(d)
    m1 = min(la, lb, lc, ld)
    m2 = max(la, lb, lc, ld)
    if m1 != m2:
        raise ExceptionWT(
            "All points a, b, c, d in QUAD(a, b, c, d) must be 2D points, or all must be 3D points."
        )
    if m1 != 2 and m1 != 3:
        raise ExceptionWT(
            "All points a, b, c, d in QUAD(a, b, c, d) must be 2D points, or all must be 3D points."
        )
    # Are some of the points the same?
    if (a == b) or (a == c) or (a == d) or (b == c) or (b == d) or (c == d):
        raise ExceptionWT(
            "Invalid quadrilateral detected - two or more vertices are the same!"
        )
    return BASEOBJ(PLASM_CONVEXHULL([a, b, c, d]))


QUADRILATERAL = QUAD

# Language aliases
# Czech:
CTYRUHELNIK = QUAD  # four-sided

# Polish:
CZWOROBOK = QUAD  # four-sided

# German:
VIERECK = QUAD  # four-cornered

# Spanish:
CUADRILATERO = QUAD  # quadrilateral

# Italian:
QUADRILATERO = QUAD  # quadrilateral

# French:
QUADRILATERE = QUAD  # quadrilateral
