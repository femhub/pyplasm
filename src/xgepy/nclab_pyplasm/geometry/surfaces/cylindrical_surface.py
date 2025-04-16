"""
Cylindrical Surface Module
"""


from nclab.tools import ExceptionWT
from ...operations.map import MAP
from ...domain.references import UNITSQUARE
from ....fenvs import PLASM_CYLINDRICALSURFACE


__all__ = [
    "cylindricalsurface",
    "CYLINDRICALSURFACE",
    "CYSURFACE",
    "CYSU",  # English aliases
    # Language variants
    "VALCOVA_PLOCHA",
    "VPLOCHA",  # Czech
    "POWIERZCHNIA_WALCOWA",
    "PWALCOWA",  # Polish
    "ZYLINDERFLACHE",
    "ZFLACHE",  # German
    "SUPERFICIE_CILINDRICA",
    "SCILINDRICA",  # Spanish
    "SUPERFICIE_CILINDRICA",
    "SCILINDRICA",  # Italian
    "SURFACE_CYLINDRIQUE",
    "SCYLINDRIQUE",  # French
]


def cylindricalsurface(*args):
    raise ExceptionWT(
        "Command cylindricalsurface() is undefined. Try CYLINDRICALSURFACE() instead?"
    )


def CYLINDRICALSURFACE(curve, vector, nx=32, ny=32):
    refdomain = UNITSQUARE(nx, ny)
    surf = PLASM_CYLINDRICALSURFACE([curve, vector])
    return MAP(refdomain, surf)


CYSURFACE = CYLINDRICALSURFACE  # Cylindrical surface
CYSU = CYLINDRICALSURFACE  # Short form

# Language variants
# Czech:
VALCOVA_PLOCHA = CYLINDRICALSURFACE  # Cylindrical surface
VPLOCHA = CYLINDRICALSURFACE  # Short form

# Polish:
POWIERZCHNIA_WALCOWA = CYLINDRICALSURFACE  # Cylindrical surface
PWALCOWA = CYLINDRICALSURFACE  # Short form

# German:
ZYLINDERFLACHE = CYLINDRICALSURFACE  # Cylindrical surface
ZFLACHE = CYLINDRICALSURFACE  # Short form

# Spanish:
SUPERFICIE_CILINDRICA = CYLINDRICALSURFACE  # Cylindrical surface
SCILINDRICA = CYLINDRICALSURFACE  # Short form

# Italian:
SUPERFICIE_CILINDRICA = CYLINDRICALSURFACE  # Cylindrical surface
SCILINDRICA = CYLINDRICALSURFACE  # Short form

# French:
SURFACE_CYLINDRIQUE = CYLINDRICALSURFACE  # Cylindrical surface
SCYLINDRIQUE = CYLINDRICALSURFACE
