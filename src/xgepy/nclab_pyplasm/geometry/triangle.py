"""
Triangle Geometry Module
"""

from nclab.tools import ExceptionWT
from ..geometry.base import BASEOBJ
from ...fenvs import PLASM_CONVEXHULL

__all__ = [
    "triangle",
    "triangle3d",
    "TRIANGLE",
    "TRIANGLE3D",
    # Language variants for 2D
    "TROJUHELNIK",  # Czech
    "TROJKAT",  # Polish
    "DREIECK",  # German
    "TRIANGULO",  # Spanish
    "TRIANGOLO",  # Italian
    # Language variants for 3D
    "TROJUHELNIK3D",  # Czech
    "TROJKAT3D",  # Polish
    "DREIECK3D",  # German
    "TRIANGULO3D",  # Spanish
    "TRIANGOLO3D",  # Italian
]


def triangle(*args):
    raise ExceptionWT("Command triangle() is undefined. Try TRIANGLE() instead?")


def TRIANGLE(a, b, c):
    if not isinstance(a, list):
        raise ExceptionWT(
            "First argument a in TRIANGLE(a, b, c) must either be a 2D point [x, y] or a 3D point [x, y, z]!"
        )
    if not isinstance(b, list):
        raise ExceptionWT(
            "Second argument b in TRIANGLE(a, b, c) must either be a 2D point [x, y] or a 3D point [x, y, z]!"
        )
    if not isinstance(c, list):
        raise ExceptionWT(
            "Third argument c in TRIANGLE(a, b, c) must either be a 2D point [x, y] or a 3D point [x, y, z]!"
        )
    la = len(a)
    lb = len(b)
    lc = len(c)
    if la != lb or la != lc or lb != lc:
        raise ExceptionWT(
            "All points a, b, c in TRIANGLE(a, b, c) must be 2D points, or all must be 3D points!"
        )
    # Are some of the points the same?
    if (a == b) or (b == c) or (a == c):
        raise ExceptionWT(
            "Invalid triangle detected - two or more vertices are the same!"
        )
    return BASEOBJ(PLASM_CONVEXHULL([a, b, c]))


def triangle3d(*args):
    raise ExceptionWT("Command triangle3d() is undefined. Try TRIANGLE3D() instead?")


def TRIANGLE3D(a, b, c):
    if not isinstance(a, list):
        raise ExceptionWT(
            "First argument a in TRIANGLE3D(a, b, c) must either be a 2D point [x, y] or a 3D point [x, y, z]!"
        )
    if not isinstance(b, list):
        raise ExceptionWT(
            "Second argument b in TRIANGLE3D(a, b, c) must either be a 2D point [x, y] or a 3D point [x, y, z]!"
        )
    if not isinstance(c, list):
        raise ExceptionWT(
            "Third argument c in TRIANGLE3D(a, b, c) must either be a 2D point [x, y] or a 3D point [x, y, z]!"
        )
    la = len(a)
    lb = len(b)
    lc = len(c)
    if la != lb or la != lc or lb != lc:
        raise ExceptionWT(
            "All points a, b, c in TRIANGLE3D(a, b, c) must be 2D points, or all must be 3D points!"
        )
    # height is kept the same for add these thin objects,
    # so that logical operations with them work:
    h = 0.001
    # Get maximum edge length:
    # e1 = sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
    # e2 = sqrt((c[0] - b[0])**2 + (c[1] - b[1])**2)
    # e3 = sqrt((c[0] - a[0])**2 + (c[1] - a[1])**2)
    # h = e1
    # if e2 > h: h = e2
    # if e3 > h: h = e3
    # Get six points for the prism:
    a_low = [a[0], a[1], 0]
    a_high = [a[0], a[1], h]
    b_low = [b[0], b[1], 0]
    b_high = [b[0], b[1], h]
    c_low = [c[0], c[1], 0]
    c_high = [c[0], c[1], h]
    # Get the convex hull:
    return BASEOBJ(PLASM_CONVEXHULL([a_low, a_high, b_low, b_high, c_low, c_high]))


# Czech:
TROJUHELNIK = TRIANGLE  # triangle

# Polish:
TROJKAT = TRIANGLE  # triangle

# German:
DREIECK = TRIANGLE  # triangle

# Spanish:
TRIANGULO = TRIANGLE  # triangle

# Italian:
TRIANGOLO = TRIANGLE  # triangle

# Language aliases for 3D
# Czech:
TROJUHELNIK3D = TRIANGLE3D  # 3D triangle

# Polish:
TROJKAT3D = TRIANGLE3D  # 3D triangle

# German:
DREIECK3D = TRIANGLE3D  # 3D triangle

# Spanish:
TRIANGULO3D = TRIANGLE3D  # 3D triangle

# Italian:
TRIANGOLO3D = TRIANGLE3D  # 3D triangle
