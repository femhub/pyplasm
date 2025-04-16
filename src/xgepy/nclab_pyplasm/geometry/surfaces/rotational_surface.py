"""
Rotational Surface Geometry Module
"""

from nclab.tools import ExceptionWT

from ...utils.constants import X
from ...operations.map import MAP
from ...operations.rotate import ROTATE
from ...domain.references import REFDOMAIN
from ....fenvs import (
    PLASM_BEZIER,
    PLASM_ROTATIONALSURFACE,
    plasm_config,
    Plasm,
    PLASM_MAP,
    PLASM_INTERVALS,
    PLASM_VIEW,
    S1,
    PI,
)

# Public API
__all__ = [
    # Main functions
    "rotationalsurface",  # Error-raising lowercase version
    "ROTATIONALSURFACE",  # Main function
    "ROSURFACE",
    "ROSURF",
    "ROSU",  # English aliases
    # Language variants
    "ROTACNI_PLOCHA",
    "RPLOCHA",  # Czech
    "POWIERZCHNIA_OBROTOWA",
    "POBROTOWA",  # Polish
    "ROTATIONSFLACHE",
    "RFLACHE",  # German
    "SUPERFICIE_ROTACIONAL",
    "SROTACIONAL",  # Spanish
    "SUPERFICIE_ROTAZIONALE",
    "SROTAZIONALE",  # Italian
    "SURFACE_ROTATIONNELLE",
    "SROTATIONNELLE",  # French
]


def rotationalsurface(*args):
    raise ExceptionWT(
        "Command rotationalsurface() is undefined. Try ROTATIONALSURFACE() instead?"
    )


def ROTATIONALSURFACE(point_list, angle=360, nx=32, na=32):
    # Sanitize point list. They need to be 2D points. Zero needs
    # to be added as the middle coordinate.
    if not isinstance(point_list, list):
        raise ExceptionWT(
            "First argument of rotational surface must be a list of 2D points in the XY plane!"
        )
    if len(point_list) < 2:
        raise ExceptionWT("Rotational surface requires at least two points!")
    newpoints = []
    for pt in point_list:
        if not isinstance(pt, list):
            raise ExceptionWT(
                "First argument of rotational surface must be a list of 2D points in the XY plane!"
            )
        if len(pt) != 2:
            raise ExceptionWT(
                "First argument of rotational surface must be a list of 2D points in the XY plane!"
            )
        newpoints.append([pt[0], 0, pt[1]])
    # Create the Bezier curve in the XZ plane:
    curve_xz = PLASM_BEZIER(S1)(newpoints)
    anglerad = angle / 180.0 * PI
    surf = PLASM_ROTATIONALSURFACE(curve_xz)
    refdomain = REFDOMAIN(1, anglerad, nx, na)
    out = MAP(refdomain, surf)
    # Rotate object back:
    ROTATE(out, -90, X)
    return out


# English aliases
ROSURFACE = ROTATIONALSURFACE
ROSURF = ROTATIONALSURFACE
ROSU = ROTATIONALSURFACE

# Language variants
# Czech:
ROTACNI_PLOCHA = ROTATIONALSURFACE  # Rotational surface
RPLOCHA = ROTATIONALSURFACE  # Short form

# Polish:
POWIERZCHNIA_OBROTOWA = ROTATIONALSURFACE  # Rotational surface
POBROTOWA = ROTATIONALSURFACE  # Short form

# German:
ROTATIONSFLACHE = ROTATIONALSURFACE  # Rotational surface
RFLACHE = ROTATIONALSURFACE  # Short form

# Spanish:
SUPERFICIE_ROTACIONAL = ROTATIONALSURFACE  # Rotational surface
SROTACIONAL = ROTATIONALSURFACE  # Short form

# Italian:
SUPERFICIE_ROTAZIONALE = ROTATIONALSURFACE  # Rotational surface
SROTAZIONALE = ROTATIONALSURFACE  # Short form

# French:
SURFACE_ROTATIONNELLE = ROTATIONALSURFACE  # Rotational surface
SROTATIONNELLE = ROTATIONALSURFACE  # Short form

# Self-test code
if __name__ == "__main__":
    # Test profile defined in XZ plane
    profile = PLASM_BEZIER(S1)([[0, 0, 0], [2, 0, 1], [3, 0, 4]])

    # Configure precision
    plasm_config.push(1e-4)

    # Create domain for mapping
    domain = Plasm.power(PLASM_INTERVALS(1)(10), PLASM_INTERVALS(2 * PI)(30))

    # Generate and view the surface
    out = PLASM_MAP(ROTATIONALSURFACE(profile))(domain)
    plasm_config.pop()
    PLASM_VIEW(out)
