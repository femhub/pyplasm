"""
Circle Geometry Module
"""

from nclab.tools import ExceptionWT
from ..geometry.base import BASEOBJ
from ..geometry.prism import PRISM
from ...fenvs import PLASM_CIRCLE

__all__ = [
    "circle",
    "CIRCLE",
    "circle3d",
    "CIRCLE3D",
    # Language variants for 2D
    "KRUH",
    "KRUZNICE",  # Czech
    "KOLO",
    "KRAG",
    "OKRAG",  # Polish
    "KREIS",  # German
    "CIRCULO",  # Spanish
    "CERCHIO",  # Italian
    "CERCLE",
    "ROND",  # French
    # Language variants for 3D
    "KRUH3D",  # Czech
    "KOLO3D",  # Polish
    "KREIS3D",  # German
    "CIRCULO3D",  # Spanish
    "CERCHIO3D",  # Italian
    "CERCLE3D",
    "ROND3D",  # French
]


def circle(*args):
    raise ExceptionWT("Command circle() is undefined. Try CIRCLE() instead?")


def CIRCLE(r, division=[48, 1]):
    if r <= 0.0000001:
        raise ExceptionWT("Radius r in CIRCLE(r) must be positive!")
    if type(division) == list:
        return BASEOBJ(PLASM_CIRCLE(r)(division))
    else:
        if division < 3:
            raise ExceptionWT("Number of edges n in CIRCLE(r, n) must be at least 3!")
        return BASEOBJ(PLASM_CIRCLE(r)([division, 1]))


def circle3d(*args):
    raise ExceptionWT("Command circle3d() is undefined. Try CIRCLE3D() instead?")


def CIRCLE3D(r, division=[48, 1]):
    if r <= 0:
        raise ExceptionWT("Radius r in CIRCLE3D(r) must be positive!")
    # height is kept the same for add these thin objects,
    # so that logical operations with them work:
    h = 0.001
    if type(division) == list:
        return PRISM(BASEOBJ(PLASM_CIRCLE(r)(division)), h)
    else:
        if division < 3:
            raise ExceptionWT("Number of edges n in CIRCLE3D(r, n) must be at least 3!")
        return PRISM(BASEOBJ(PLASM_CIRCLE(r)([division, 1])), h)


# Czech:
KRUH = CIRCLE  # circle
KRUZNICE = CIRCLE  # circumference

# Polish:
KOLO = CIRCLE  # circle
KRAG = CIRCLE  # circle
OKRAG = CIRCLE  # circle

# German:
KREIS = CIRCLE  # circle

# Spanish:
CIRCULO = CIRCLE  # circle

# Italian:
CERCHIO = CIRCLE  # circle

# French:
CERCLE = CIRCLE  # circle
ROND = CIRCLE  # round

# Language aliases for 3D
# Czech:
KRUH3D = CIRCLE3D  # 3D circle

# Polish:
KOLO3D = CIRCLE3D  # 3D circle

# German:
KREIS3D = CIRCLE3D  # 3D circle

# Spanish:
CIRCULO3D = CIRCLE3D  # 3D circle

# Italian:
CERCHIO3D = CIRCLE3D  # 3D circle

# French:
CERCLE3D = CIRCLE3D  # 3D circle
ROND3D = CIRCLE3D  # 3D round
