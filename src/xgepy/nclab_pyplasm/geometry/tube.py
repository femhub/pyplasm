"""
Tube Geometry Module
"""


from nclab.tools import ExceptionWT
from ..geometry.base import BASEOBJ
from ...fenvs import PLASM_TUBE

__all__ = [
    "tube",
    "TUBE",
    # Language variants
    "TRUBICE",
    "TRUBKA",
    "TUBA",
    "ROURA",  # Czech
    "RURA",  # Polish
    "ROHR",  # German
    "TUBO",  # Spanish
    "TUBO",  # Italian
    "TUBE",  # French
]


def tube(*args):
    raise ExceptionWT("Command tube() is undefined. Try TUBE() instead?")


def TUBE(r1, r2, h, division=48):
    if r1 <= 0:
        raise ExceptionWT("Inner radius r1 in TUBE(r1, r2, h) must be positive!")
    if r2 <= 0:
        raise ExceptionWT("Outer radius r2 in TUBE(r1, r2, h) must be positive!")
    if h <= 0:
        raise ExceptionWT("Height h in TUBE(r1, r2, h) must be positive!")
    if r1 >= r2:
        raise ExceptionWT(
            "Inner radius r1 must be smaller than outer radius r2 in TUBE(r1, r2, h)!"
        )
    if division < 3:
        raise ExceptionWT(
            "The number of sides n in TUBE(r1, r2, h, n) must be at least 3!"
        )
    return BASEOBJ(PLASM_TUBE([r1, r2, h])(division))


# Czech:
TRUBICE = TUBE  # tube
TRUBKA = TUBE  # pipe
TUBA = TUBE  # tube
ROURA = TUBE  # pipe

# Polish:
RURA = TUBE  # pipe

# German:
ROHR = TUBE  # pipe

# Spanish:
TUBO = TUBE  # tube

# Italian:
TUBO = TUBE  # tube

# French:
TUBE = TUBE  # tube
