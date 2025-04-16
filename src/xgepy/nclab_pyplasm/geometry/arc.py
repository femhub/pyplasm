"""
Arc Creation Module

This module provides functions for creating 2D and 3D arc objects with various parameters.
"""

from nclab.tools import ExceptionWT
from ..geometry.base import BASEOBJ
from ..geometry.prism import PRISM
from ...fenvs import PLASM_ARC


__all__ = [
    # 2D Arc functions
    "ARC",  # English
    "OBLOUK",
    "VYSEČ",  # Czech
    "LUK",
    "WYSEK",  # Polish
    "BOGEN",
    "BOGENSTÜCK",  # German
    "ARCO",
    "SECTOR",  # Spanish
    "ARCO",
    "SETTORE",  # Italian
    "ARC",
    "SECTEUR",  # French
    # 3D Arc functions
    "ARC3D",  # English
    "OBLOUK3D",
    "VYSEČ3D",  # Czech
    "LUK3D",
    "WYSEK3D",  # Polish
    "BOGEN3D",
    "BOGENSTÜCK3D",  # German
    "ARCO3D",
    "SECTOR3D",  # Spanish
    "ARCO3D",
    "SETTORE3D",  # Italian
    "ARC3D",
    "SECTEUR3D",  # French
]


def arc(*args):
    raise ExceptionWT("Command arc() is undefined. Try ARC() instead?")


def ARC(r1, r2, angle, division=[48, 1]):
    if r1 < 0:
        raise ExceptionWT("Radius r1 in ARC(r1, r2, angle) must be nonnegative!")
    if r2 <= r1:
        raise ExceptionWT(
            "Radiuses r1 and r2 in ARC(r1, r2, angle) must satisfy r1 < r2!"
        )
    if angle <= 0:
        raise ExceptionWT("Angle in ARC(r1, r2, angle) must be positive!")
    if type(division) == list:
        return BASEOBJ(PLASM_ARC([r1, r2, angle])(division))
    else:
        return BASEOBJ(PLASM_ARC([r1, r2, angle])([division, 1]))


def arc3d(*args):
    raise ExceptionWT("Command arc3d() is undefined. Try ARC3D() instead?")


def ARC3D(r1, r2, angle, h, division=[48, 1]):
    if r1 < 0:
        raise ExceptionWT("Radius r1 in ARC3D(r1, r2, h, angle) must be nonnegative!")
    if r2 <= r1:
        raise ExceptionWT(
            "Radiuses r1 and r2 in ARC3D(r1, r2, h, angle) must satisfy r1 < r2!"
        )
    if angle <= 0:
        raise ExceptionWT("Angle in ARC3D(r1, r2, h, angle) must be positive!")
    if h <= 0:
        raise ExceptionWT("Height 'h' in ARC3D(r1, r2, h, angle) must be positive!")
    if type(division) == list:
        return PRISM(BASEOBJ(PLASM_ARC([r1, r2, angle])(division)), h)
    else:
        return PRISM(BASEOBJ(PLASM_ARC([r1, r2, angle])([division, 1])), h)


# English:
ARC = ARC

# Czech:
OBLOUK = ARC
VYSEČ = ARC

# Polish:
LUK = ARC
WYSEK = ARC

# German:
BOGEN = ARC
BOGENSTÜCK = ARC

# Spanish:
ARCO = ARC
SECTOR = ARC

# Italian:
ARCO = ARC
SETTORE = ARC

# French:
ARC = ARC
SECTEUR = ARC


# English:
ARC3D = ARC3D

# Czech:
OBLOUK3D = ARC3D
VYSEČ3D = ARC3D

# Polish:
LUK3D = ARC3D
WYSEK3D = ARC3D

# German:
BOGEN3D = ARC3D
BOGENSTÜCK3D = ARC3D

# Spanish:
ARCO3D = ARC3D
SECTOR3D = ARC3D

# Italian:
ARCO3D = ARC3D
SETTORE3D = ARC3D

# French:
ARC3D = ARC3D
SECTEUR3D = ARC3D
