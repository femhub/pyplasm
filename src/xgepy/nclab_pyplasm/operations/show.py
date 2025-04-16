"""
Command SHOW()
"""

from nclab.tools import ExceptionWT
from ..utils.common import flatten
from ..geometry.base import BASEOBJ, EMPTYSET
from ..utils.viewbase import VIEWBASE


def show(*args):
    raise ExceptionWT("Command show() is undefined. Try SHOW() instead?")


def SHOW(*args):
    sequence = flatten(*args)
    if sequence == []:
        print("WARNING: The SHOW command received no objects.")
        return
    # Check if they are valid objects or empty lists:
    for obj in sequence:
        if isinstance(obj, tuple):
            raise ExceptionWT(
                "Please use the UNION command to create unions of objects."
            )
        if not isinstance(obj, BASEOBJ) and obj != []:
            raise ExceptionWT("The SHOW command received an invalid object.")
    # Remove empty lists and empty sets:
    newseq = []
    for obj in sequence:
        if obj != [] and not EMPTYSET(obj):
            newseq.append(obj)
    # for obj in sequence:
    #    if SIZEX(obj) == 0 and SIZEY(obj) == 0 and SIZEZ(obj) == 0:
    #        raise ExceptionWT("One of the objects that you are trying to display is empty!")
    if len(newseq) == 0:
        raise ExceptionWT(
            "The SHOW command received an empty set.\nNote: SUBTRACT(a, b) subtracts object 'b' from object 'a'."
        )
    for obj in newseq:
        if isinstance(obj, tuple):
            raise ExceptionWT("Use the UNION command to create unions of objects.")
        if not isinstance(obj, BASEOBJ):
            raise ExceptionWT("The SHOW command received an invalid object.")
    VIEWBASE(sequence)


# Czech:
UKAZ = SHOW
# Polish:
POKAZ = SHOW
# German:
ZEIGE = SHOW
# Italian:
MOSTRA = SHOW
# French:
MONTRE = SHOW
# Spanish:
MUESTRA = SHOW


__all__ = [
    "show",
    "SHOW",
    "UKAZ",  # Czech
    "POKAZ",  # Polish
    "ZEIGE",  # German
    "MOSTRA",  # Italian
    "MONTRE",  # French
    "MUESTRA",  # Spanish
]
