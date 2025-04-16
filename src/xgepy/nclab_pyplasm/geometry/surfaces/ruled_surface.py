"""
Ruled Surface Geometry Module
"""

from nclab.tools import ExceptionWT
from ....fenvs import PLASM_RULEDSURFACE

__all__ = [
    "ruledsurface",
    "RULEDSURFACE",
    "RUSURFACE",
    "RUSURF",
    "RUSU",
    # Language variants
    "PRAVCOVA_PLOCHA",
    "PPLOCHA",  # Czech
    "POWIERZCHNIA_PROWADZACA",
    "PPOWIERZCHNIA",  # Polish
    "REGELFLACHE",
    "RFLACHE",  # German
    "SUPERFICIE_REGIDA",
    "SREGIDA",  # Spanish
    "SUPERFICIE_RIGATA",
    "SRIGATA",  # Italian
    "SURFACE_REGLEE",
    "SREGLEE",  # French
]


def ruledsurface(*args):
    raise ExceptionWT(
        "Command ruledsurface() is undefined. Try RULEDSURFACE() instead?"
    )


def RULEDSURFACE(a, b):
    return PLASM_RULEDSURFACE([a, b])


# English aliases
RUSURFACE = RULEDSURFACE
RUSURF = RULEDSURFACE
RUSU = RULEDSURFACE

# Language variants
# Czech:
PRAVCOVA_PLOCHA = RULEDSURFACE  # Ruled surface
PPLOCHA = RULEDSURFACE  # Short form

# Polish:
POWIERZCHNIA_PROWADZACA = RULEDSURFACE  # Ruled surface
PPOWIERZCHNIA = RULEDSURFACE  # Short form

# German:
REGELFLACHE = RULEDSURFACE  # Ruled surface
RFLACHE = RULEDSURFACE  # Short form

# Spanish:
SUPERFICIE_REGIDA = RULEDSURFACE  # Ruled surface
SREGIDA = RULEDSURFACE  # Short form

# Italian:
SUPERFICIE_RIGATA = RULEDSURFACE  # Ruled surface
SRIGATA = RULEDSURFACE  # Short form

# French:
SURFACE_REGLEE = RULEDSURFACE  # Ruled surface
SREGLEE = RULEDSURFACE  # Short form
