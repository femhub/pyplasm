"""
Join Operations Module
"""

from nclab.tools import ExceptionWT
from ..geometry.base import BASEOBJ
from ...fenvs import PLASM_JOIN


__all__ = [
    "join",
    "JOIN",
    # Language variants
    "SPOJ",
    "SPOJIT",
    "SPOJENI",  # Czech
    "POLACZ",
    "POLACZENIE",  # Polish
    "VERBINDE",
    "VERBINDUNG",  # German
    "UNIR",
    "UNION",  # Spanish
    "UNIRE",
    "UNIONE",  # Italian
    "JOINDRE",
    "RELIER",  # French
]


def join(*args):
    raise ExceptionWT("Command join() is undefined. Try JOIN() instead?")


def JOIN(a, b=None):
    ageom = a.geom
    if b != None:
        if not isinstance(a, BASEOBJ) or not isinstance(b, BASEOBJ):
            raise ExceptionWT(
                "In JOIN(obj1, obj2), both obj1 and obj2 must be PLaSM surfaces."
            )
        bgeom = b.geom
        return BASEOBJ(PLASM_JOIN([ageom, bgeom]))
    else:  # single argument must be list
        if not isinstance(a, BASEOBJ):
            raise ExceptionWT("In JOIN(obj), obj must be a PLaSM surface.")
        return BASEOBJ(PLASM_JOIN(ageom))


# Czech:
SPOJ = JOIN
SPOJIT = JOIN
SPOJENI = JOIN

# Polish:
POLACZ = JOIN
POLACZENIE = JOIN

# German:
VERBINDE = JOIN
VERBINDUNG = JOIN

# Spanish:
UNIR = JOIN
UNION = JOIN

# Italian:
UNIRE = JOIN
UNIONE = JOIN

# French:
JOINDRE = JOIN
RELIER = JOIN
