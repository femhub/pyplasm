"""
Solidify Module
"""

from nclab.tools import ExceptionWT
from ..geometry.base import BASEOBJ
from ...fenvs import PLASM_SOLIDIFY

__all__ = [
    "solidify",
    "SOLIDIFY",
    # Language variants
    "ZPEVNIT",
    "ZTVRDIT",  # Czech
    "UTWARDZIC",
    "ZESTALIC",  # Polish
    "VERFESTIGEN",
    "VERHARTEN",  # German
    "SOLIDIFICAR",
    "ENDURECER",  # Spanish
    "SOLIDIFICARE",
    "INDURIRE",  # Italian
    "SOLIDIFIER",
    "DURCIR",  # French
]


def solidify(*args):
    raise ExceptionWT("Command solidify() is undefined. Try SOLIDIFY() instead?")


def SOLIDIFY(surf):
    if not isinstance(surf, BASEOBJ):
        raise ExceptionWT("In SOLIDIFY(surf), surf must be a PLaSM surface.")
    obj = BASEOBJ(PLASM_SOLIDIFY(surf.geom))
    return obj


ZPEVNIT = SOLIDIFY  # Solidify
ZTVRDIT = SOLIDIFY  # Harden

# Polish:
UTWARDZIC = SOLIDIFY  # Solidify
ZESTALIC = SOLIDIFY  # Harden

# German:
VERFESTIGEN = SOLIDIFY  # Solidify
VERHARTEN = SOLIDIFY  # Harden

# Spanish:
SOLIDIFICAR = SOLIDIFY  # Solidify
ENDURECER = SOLIDIFY  # Harden

# Italian:
SOLIDIFICARE = SOLIDIFY  # Solidify
INDURIRE = SOLIDIFY  # Harden

# French:
SOLIDIFIER = SOLIDIFY  # Solidify
DURCIR = SOLIDIFY
