"""
Shell Geometry Module
"""

__all__ = [
    "shell",
    "SHELL",
    # Language variants
    "SKORUPA",
    "OBAL",  # Czech
    "POWLOKA",
    "SKORUPA",  # Polish
    "SCHALE",
    "MUSCHEL",  # German
    "CASCARON",
    "CONCHA",  # Spanish
    "GUSCIO",
    "CONCHIGLIA",  # Italian
    "COQUILLE",
    "COQUE",  # French
]


from nclab.tools import ExceptionWT
from ..utils.common import ISNUMBER
from ..geometry.base import BASEOBJ
from ..geometry.shells.spherical_shell import PLASM_SHELL


def shell(*args):
    raise ExceptionWT("Command shell() is undefined. Try SHELL() instead?")


def SHELL(radius1, radius2, divisions=[16, 32]):
    if not ISNUMBER(radius1):
        raise ExceptionWT("Radius r1 in SHELL(r1, r2) must be a number!")
    if not ISNUMBER(radius2):
        raise ExceptionWT("Radius r2 in SHELL(r1, r2) must be a number!")
    if radius1 < -1e-8:
        raise ExceptionWT("Radius r1 in SHELL(r1, r2) must be nonnegative!")
    if radius2 <= 0:
        raise ExceptionWT("Radius r2 in SHELL(r1, r2) must be positive!")
    if radius2 <= radius1:
        raise ExceptionWT("Radius r2 must be greater than r1 in SHELL(r1, r2)!")
    divisionslist = divisions
    if not isinstance(divisions, list):
        if divisions <= 4:
            raise ExceptionWT("Bad division in the SHELL command!")
        divisionslist = [int(divisions / 2), divisions]
    # Making it s solid:
    return BASEOBJ(PLASM_SHELL(radius1, radius2)(divisionslist))


# Czech:
SKORUPA = SHELL  # shell
OBAL = SHELL  # cover

# Polish:
POWLOKA = SHELL  # shell
SKORUPA = SHELL  # shell

# German:
SCHALE = SHELL  # shell
MUSCHEL = SHELL  # shell

# Spanish:
CASCARON = SHELL  # shell
CONCHA = SHELL  # shell

# Italian:
GUSCIO = SHELL  # shell
CONCHIGLIA = SHELL  # shell

# French:
COQUILLE = SHELL  # shell
COQUE = SHELL  # shell
