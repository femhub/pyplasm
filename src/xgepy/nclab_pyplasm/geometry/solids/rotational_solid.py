"""
Rotational Solid Module
"""

import math

from nclab.tools import ExceptionWT
from ...utils.constants import X
from ...geometry.base import BASEOBJ
from ...operations.rotate import ROTATE
from ....fenvs import (
    PLASM_INTERVALS,
    PLASM_PROD,
    PLASM_MAP,
    PLASM_BEZIER,
    PI,
    S1,
    PLASM_INSR,
)

__all__ = [
    "rotationalsolid",
    "ROTATIONALSOLID",
    "ROTSOLID",
    "ROSOLID",
    "ROSOL",
    # Language variants
    "ROTACNI_TELESO",
    "RTELESO",  # Czech
    "BRYLA_OBROTOWA",
    "BOBROTOWA",  # Polish
    "ROTATIONSKORPER",
    "RKORPER",  # German
    "SOLIDO_ROTACIONAL",
    "SROTACIONAL",  # Spanish
    "SOLIDO_ROTAZIONALE",
    "SROTAZIONALE",  # Italian
    "SOLIDE_ROTATIONNEL",
    "SROTATIONNEL",  # French
]


def PLASM_ROTSOLID(profileangleminr):
    profile, angle, minr = profileangleminr

    def PLASM_ROTSOLID0(divisions):
        n, m, o = divisions
        domain = PLASM_INSR(PLASM_PROD)(
            [
                PLASM_INTERVALS(1.0)(n),
                PLASM_INTERVALS(angle)(m),
                PLASM_INTERVALS(1.0)(o),
            ]
        )
        fx = lambda p: minr * math.cos(p[1]) + ((profile(p))[0] - minr) * p[
            2
        ] * math.cos(p[1])
        fy = lambda p: minr * math.sin(p[1]) + ((profile(p))[0] - minr) * p[
            2
        ] * math.sin(p[1])
        fz = lambda p: (profile(p))[2]
        return PLASM_MAP([fx, fy, fz])(domain)

    return PLASM_ROTSOLID0


def rotationalsolid(*args):
    raise ExceptionWT(
        "Command rotationalsolid() is undefined. Try ROTATIONALSOLID() instead?"
    )


def ROTATIONALSOLID(point_list, angle=360, minr=0, nx=32, na=32, nr=1):
    # Sanitize point list. They need to be 2D points. Zero needs
    # to be added as the middle coordinate.
    if not isinstance(point_list, list):
        raise ExceptionWT(
            "First argument of rotational solid must be a list of 2D points in the XY plane!"
        )
    if len(point_list) < 2:
        raise ExceptionWT("Rotational solid requires at least two points!")
    # Additional sanity tests:
    if angle <= 0:
        raise ExceptionWT("Rotational solid requires a positive angle!")
    if minr < 0:
        raise ExceptionWT("Rotational solid requires a positive minimum radius!")
    newpoints = []
    for pt in point_list:
        if not isinstance(pt, list):
            raise ExceptionWT(
                "First argument of rotational solid must be a list of 2D points in the XY plane!"
            )
        if len(pt) != 2:
            raise ExceptionWT(
                "First argument of rotational solid must be a list of 2D points in the XY plane!"
            )
        newpoints.append([pt[0], 0, pt[1]])
    # Create the Bezier curve in the XZ plane:
    curve_xz = PLASM_BEZIER(S1)(newpoints)
    anglerad = angle / 180.0 * PI
    out = BASEOBJ(PLASM_ROTSOLID([curve_xz, anglerad, minr])([nx, na, nr]))
    # Rotate object back:
    ROTATE(out, -90, X)
    out.dim = 3
    return out


ROTSOLID = ROTATIONALSOLID  # Rotational solid
ROSOLID = ROTATIONALSOLID  # Short form
ROSOL = ROTATIONALSOLID  # Very short form

# Language variants
# Czech:
ROTACNI_TELESO = ROTATIONALSOLID  # Rotational solid
RTELESO = ROTATIONALSOLID  # Short form

# Polish:
BRYLA_OBROTOWA = ROTATIONALSOLID  # Rotational solid
BOBROTOWA = ROTATIONALSOLID  # Short form

# German:
ROTATIONSKORPER = ROTATIONALSOLID  # Rotational solid
RKORPER = ROTATIONALSOLID  # Short form

# Spanish:
SOLIDO_ROTACIONAL = ROTATIONALSOLID  # Rotational solid
SROTACIONAL = ROTATIONALSOLID  # Short form

# Italian:
SOLIDO_ROTAZIONALE = ROTATIONALSOLID  # Rotational solid
SROTAZIONALE = ROTATIONALSOLID  # Short form

# French:
SOLIDE_ROTATIONNEL = ROTATIONALSOLID  # Rotational solid
SROTATIONNEL = ROTATIONALSOLID
