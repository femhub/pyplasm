"""
Rotational Shell Module
"""

import math

from nclab.tools import ExceptionWT
from ...utils.constants import X
from ...geometry.base import BASEOBJ
from ...operations.rotate import ROTATE
from ....fenvs import (
    PLASM_INSR,
    PLASM_PROD,
    PLASM_INTERVALS,
    PLASM_MAP,
    PLASM_BEZIER,
    PI,
    S1,
)

__all__ = [
    "rotationalshell",
    "ROTATIONALSHELL",
    "ROTSHELL",
    "ROSHELL",
    # Language variants
    "ROTACNI_SKOREPA",
    "RSKOREPA",  # Czech
    "POWLOKA_OBROTOWA",
    "POBROTOWA",  # Polish
    "ROTATIONSSCHALE",
    "RSCHALE",  # German
    "CASCARON_ROTACIONAL",
    "CROTACIONAL",  # Spanish
    "GUSCIO_ROTAZIONALE",
    "GROTAZIONALE",  # Italian
    "COQUE_ROTATIONNELLE",
    "CROTATIONNELLE",  # French
]


def rotationalshell(*args):
    raise ExceptionWT(
        "Command rotationalshell() is undefined. Try ROTATIONALSHELL() instead?"
    )


def PLASM_ROTSHELL(profileanglethickness):
    profile, angle, thickness = profileanglethickness

    def PLASM_ROTSHELL0(divisions):
        n, m, o = divisions
        domain = PLASM_INSR(PLASM_PROD)(
            [
                PLASM_INTERVALS(1.0)(n),
                PLASM_INTERVALS(angle)(m),
                PLASM_INTERVALS(1.0)(o),
            ]
        )
        fx = lambda p: (profile(p))[0] * math.cos(p[1]) + thickness * p[2] * math.cos(
            p[1]
        )
        fy = lambda p: (profile(p))[0] * math.sin(p[1]) + thickness * p[2] * math.sin(
            p[1]
        )
        fz = lambda p: (profile(p))[2]
        return PLASM_MAP([fx, fy, fz])(domain)

    return PLASM_ROTSHELL0


# NEW COMMAND:


def ROTATIONALSHELL(point_list, thickness, angle=360, nx=32, na=32, nr=1):
    # Sanitize point list. They need to be 2D points. Zero needs
    # to be added as the middle coordinate.
    if not isinstance(point_list, list):
        raise ExceptionWT(
            "First argument of rotational shell must be a list of 2D points in the XY plane!"
        )
    if len(point_list) < 2:
        raise ExceptionWT("Rotational shell requires at least two points!")
    # Additional sanity tests:
    if angle <= 0:
        raise ExceptionWT("Rotational shell requires a positive angle!")
    if thickness < 0:
        raise ExceptionWT("Rotational shell requires a positive thickness!")
    newpoints = []
    for pt in point_list:
        if not isinstance(pt, list):
            raise ExceptionWT(
                "First argument of rotational shell must be a list of 2D points in the XY plane!"
            )
        if len(pt) != 2:
            raise ExceptionWT(
                "First argument of rotational shell must be a list of 2D points in the XY plane!"
            )
        newpoints.append([pt[0], 0, pt[1]])
    # Create the Bezier curve in the XZ plane:
    curve_xz = PLASM_BEZIER(S1)(newpoints)
    anglerad = angle / 180.0 * PI
    out = BASEOBJ(PLASM_ROTSHELL([curve_xz, anglerad, thickness])([nx, na, nr]))
    # Rotate object back:
    ROTATE(out, -90, X)
    out.dim = 3
    return out


ROTSHELL = ROTATIONALSHELL  # Rotational shell
ROSHELL = ROTATIONALSHELL  # Short form

# Language variants
# Czech:
ROTACNI_SKOREPA = ROTATIONALSHELL  # Rotational shell
RSKOREPA = ROTATIONALSHELL  # Short form

# Polish:
POWLOKA_OBROTOWA = ROTATIONALSHELL  # Rotational shell
POBROTOWA = ROTATIONALSHELL  # Short form

# German:
ROTATIONSSCHALE = ROTATIONALSHELL  # Rotational shell
RSCHALE = ROTATIONALSHELL  # Short form

# Spanish:
CASCARON_ROTACIONAL = ROTATIONALSHELL  # Rotational shell
CROTACIONAL = ROTATIONALSHELL  # Short form

# Italian:
GUSCIO_ROTAZIONALE = ROTATIONALSHELL  # Rotational shell
GROTAZIONALE = ROTATIONALSHELL  # Short form

# French:
COQUE_ROTATIONNELLE = ROTATIONALSHELL  # Rotational shell
CROTATIONNELLE = ROTATIONALSHELL  # Short form
