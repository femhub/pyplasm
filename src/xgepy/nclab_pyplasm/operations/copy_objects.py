"""
COPYING OBJECTS AND LISTS OF OBJECTS (LISTS ARE FLATTENED
"""

import copy

from nclab.tools import ExceptionWT
from ..utils.common import flatten
from ..geometry.base import BASEOBJ


# DO NOT DEFINE copy() !!!


def COPY(obj):
    if not isinstance(obj, list):
        if isinstance(obj, tuple):
            raise ExceptionWT("Use the UNION command to create unions of objects.")
        if not isinstance(obj, BASEOBJ):
            raise ExceptionWT("Invalid object found (copy - 1).")
        return copy.copy(obj)
    else:
        obj1 = flatten(obj)  # flatten the rest as there may be structs
        newlist = []
        for x in obj1:
            if isinstance(x, tuple):
                raise ExceptionWT("Use the UNION command to create unions of objects.")
            if not isinstance(x, BASEOBJ):
                raise ExceptionWT("Invalid object found (copy - 2).")
            newlist.append(copy.copy(x))
        return newlist


# Czech:
KOPIE = COPY

# Polish:
KOPIA = COPY

# German:
KOPIE = COPY

# Spanish:
COPIA = COPY

# Italian:
COPIA = COPY

# French:
COPIE = COPY

__all__ = [
    "COPY",
    # Language variants
    "KOPIE",  # Czech
    "KOPIA",  # Polish
    "KOPIE",  # German
    "COPIA",  # Spanish
    "COPIA",  # Italian
    "COPIE",  # French
]
