"""
Elbow Geometry Module
"""
from nclab.tools import ExceptionWT
from ..utils.common import ISNUMBER
from ..geometry.base import BASEOBJ
from ...fenvs import PLASM_SOLIDELBOW

__all__ = [
    "elbow",
    "ELBOW",
    # Language variants
    "KOLENO",
    "OHYB",  # Czech
    "KOLANO",
    "ZAGIEK",  # Polish
    "KRUMMER",
    "BOGEN",  # German
    "CODO",
    "CURVA",  # Spanish
    "GOMMITO",
    "CURVA",  # Italian
    "COUDE",
    "COURBE",  # French
]


def elbow(*args):
    raise ExceptionWT("Command elbow() is undefined. Try ELBOW() instead?")


def ELBOW(r1, r2, angle, divisions=[24, 24]):
    if not ISNUMBER(angle):
        raise ExceptionWT("Angle alpha in ELBOW(r1, r2, alpha) must be a number!")
    if not ISNUMBER(r1):
        raise ExceptionWT("Inner radius r1 in ELBOW(r1, r2, alpha) must be a number!")
    if not ISNUMBER(r2):
        raise ExceptionWT("Outer radius r2 in ELBOW(r1, r2, alpha) must be a number!")
    if angle <= 0:
        raise ExceptionWT("Angle alpha in ELBOW(r1, r2, alpha) must be positive!")
    if r1 <= 0:
        raise ExceptionWT("Inner radius r1 in ELBOW(r1, r2, alpha) must be positive!")
    if r2 <= 0:
        raise ExceptionWT("Outer radius r2 in ELBOW(r1, r2, alpha) must be positive!")
    if r2 <= r1:
        raise ExceptionWT(
            "Inner radius r1 must be smaller than outer radius r2 in ELBOW(r1, r2, alpha)!"
        )
    divisionslist = divisions
    if not isinstance(divisions, list):
        if divisions / 2 <= 0:
            raise ExceptionWT("Bad division in the ELBOW command!")
        divisionslist = [divisions, int(divisions / 2)]
    return BASEOBJ(
        PLASM_SOLIDELBOW([r1, r2, angle])([divisionslist[0], divisionslist[1], 1])
    )


# Czech:
KOLENO = ELBOW  # elbow
OHYB = ELBOW  # bend

# Polish:
KOLANO = ELBOW  # elbow
ZAGIEK = ELBOW  # bend

# German:
KRUMMER = ELBOW  # elbow
BOGEN = ELBOW  # bend

# Spanish:
CODO = ELBOW  # elbow
CURVA = ELBOW  # bend

# Italian:
GOMMITO = ELBOW  # elbow
CURVA = ELBOW  # bend

# French:
COUDE = ELBOW  # elbow
COURBE = ELBOW  # bend
