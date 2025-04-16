"""
Conical Surface Module
"""

from nclab.tools import ExceptionWT
from ...operations.map import MAP
from ...domain.references import UNITSQUARE
from ....fenvs import PLASM_CONICALSURFACE


__all__ = [
    "conicalsurface",
    "CONICALSURFACE",
    "COSURFACE",
    "COSURF",
    "COSU",
    # Language variants
    "KUSOVA_PLOCHA",
    "KPLOCHA",  # Czech
    "POWIERZCHNIA_STOZKOWA",
    "PSTOZKOWA",  # Polish
    "KEGELFLACHE",
    "KFLACHE",  # German
    "SUPERFICIE_CONICA",
    "SCONICA",  # Spanish
    "SUPERFICIE_CONICA",
    "SCONICA",  # Italian
    "SURFACE_CONIQUE",
    "SCONIQUE",  # French
]


def conicalsurface(*args):
    raise ExceptionWT(
        "Command conicalsurface() is undefined. Try CONICALSURFACE() instead?"
    )


def CONICALSURFACE(curve, point, nx=32, ny=32):
    refdomain = UNITSQUARE(nx, ny)
    surf = PLASM_CONICALSURFACE([point, curve])
    return MAP(refdomain, surf)


COSURFACE = CONICALSURFACE  # Conical surface
COSURF = CONICALSURFACE  # Short form
COSU = CONICALSURFACE  # Shortest form

# Language variants
# Czech:
KUSOVA_PLOCHA = CONICALSURFACE  # Conical surface
KPLOCHA = CONICALSURFACE  # Short form

# Polish:
POWIERZCHNIA_STOZKOWA = CONICALSURFACE  # Conical surface
PSTOZKOWA = CONICALSURFACE  # Short form

# German:
KEGELFLACHE = CONICALSURFACE  # Conical surface
KFLACHE = CONICALSURFACE  # Short form

# Spanish:
SUPERFICIE_CONICA = CONICALSURFACE  # Conical surface
SCONICA = CONICALSURFACE  # Short form

# Italian:
SUPERFICIE_CONICA = CONICALSURFACE  # Conical surface
SCONICA = CONICALSURFACE  # Short form

# French:
SURFACE_CONIQUE = CONICALSURFACE  # Conical surface
SCONIQUE = CONICALSURFACE
