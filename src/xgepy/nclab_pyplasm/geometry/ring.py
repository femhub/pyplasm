"""
Ring Geometry Module
"""


from nclab.tools import ExceptionWT
from ..geometry.base import BASEOBJ
from ..geometry.tube import TUBE
from ...fenvs import CUBOID, PLASM_RING

__all__ = [
    # Main functions
    "ring",
    "RING",
    # Language variants
    "KRUH",
    "PRSTEN",
    "KRUZOK",  # Czech
    "PIERSCIEN",
    "KOLO",  # Polish
    "RING",
    "KREISRING",  # German
    "ANILLO",
    "ARO",  # Spanish
    "ANELLO",
    "CERCHIO",  # Italian
    "ANNEAU",
    "CERCLE",  # French
    "ring3d",
    "RING3D",
    # Language variants
    "KRUH3D",
    "PRSTEN3D",
    "KRUZOK3D",  # Czech
    "PIERSCIEN3D",
    "KOLO3D",  # Polish
    "RING3D",
    "KREISRING3D",  # German
    "ANILLO3D",
    "ARO3D",  # Spanish
    "ANELLO3D",
    "CERCHIO3D",  # Italian
    "ANNEAU3D",
    "CERCLE3D",  # French
]


def ring(*args):
    raise ExceptionWT("Command ring() is undefined. Try RING() instead?")


def RING(r1, r2, division=[48, 1]):
    if r1 <= 0:
        raise ExceptionWT("Inner radius r1 in RING(r1, r2) must be positive!")
    if r2 <= 0:
        raise ExceptionWT("Outer radius r2 in RING(r1, r2) must be positive!")
    if r1 >= r2:
        raise ExceptionWT(
            "Inner radius r1 must be smaller than outer radius r2 in RING(r1, r2)!"
        )
    obj = BASEOBJ(CUBOID([1, 1, 1]))  # just to create the variable
    if type(division) == list:
        obj = BASEOBJ(PLASM_RING([r1, r2])(division))
    else:
        if int(division) != division:
            raise ExceptionWT(
                "The optional third argument of RING(r1, r2, n) must be an integer. Try TUBE(r1, r2, h) instead?"
            )
        if division < 3:
            raise ExceptionWT(
                "Number of edges n in RING(r1, r2, n) must be at least 3!"
            )
        else:
            obj = BASEOBJ(PLASM_RING([r1, r2])([division, 1]))
    return obj


# Czech:
KRUH = RING  # circle
PRSTEN = RING  # ring
KRUZOK = RING  # small ring

# Polish:
PIERSCIEN = RING  # ring
KOLO = RING  # circle

# German:
RING = RING  # ring
KREISRING = RING  # circle ring

# Spanish:
ANILLO = RING  # ring
ARO = RING  # ring/hoop

# Italian:
ANELLO = RING  # ring
CERCHIO = RING  # circle

# French:
ANNEAU = RING  # ring
CERCLE = RING  # circle


def ring3d(*args):
    raise ExceptionWT("Command ring3d() is undefined. Try RING3D() instead?")


def RING3D(r1, r2, division=48):
    h = 0.001
    return TUBE(r1, r2, h, division)


# Czech:
KRUH3D = RING3D  # 3D circle
PRSTEN3D = RING3D  # 3D ring
KRUZOK3D = RING3D  # 3D small ring

# Polish:
PIERSCIEN3D = RING3D  # 3D ring
KOLO3D = RING3D  # 3D circle

# German:
RING3D = RING3D  # 3D ring
KREISRING3D = RING3D  # 3D circle ring

# Spanish:
ANILLO3D = RING3D  # 3D ring
ARO3D = RING3D  # 3D ring/hoop

# Italian:
ANELLO3D = RING3D  # 3D ring
CERCHIO3D = RING3D  # 3D circle

# French:
ANNEAU3D = RING3D  # 3D ring
CERCLE3D = RING3D  # 3D circle
