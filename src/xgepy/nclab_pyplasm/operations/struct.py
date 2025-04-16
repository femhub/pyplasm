"""
Structure Operations Module
"""

from nclab.tools import ExceptionWT
from ..utils.common import flatten


def struct(*args):
    raise ExceptionWT("Command struct() is undefined. Try STRUCT() instead?")


def STRUCT(*args):
    list1 = list(args)
    list1 = flatten(list1)  # flatten the rest as there may be structs
    if len(list1) < 1:
        raise ExceptionWT("STRUCT() must be applied to some objects!")
    return list1


# OLD DEFINITION - THERE WERE PROBLEMS WITH COLORS
# def STRUCT(*args):
#    list1 = list(args)
#    if len(list1) <= 1: raise ExceptionWT("STRUCT(...) requires at least two objects!")
#    return PLASM_STRUCT(list1)
# Czech:
SPOJ = STRUCT
SPOJIT = STRUCT
SPOJENI = STRUCT
STRUKTURA = STRUCT
# Polish:
# It is also "STRUKTURA"
# German:
STRUKTUR = STRUCT
VERBINDE = STRUCT
# Spanish:
ESTRUCTURA = STRUCT
ESTRUCT = STRUCT
# Italian:
STRUTTURA = STRUCT


# French:
# Same as English

__all__ = [
    "struct",
    "STRUCT",
    # Language variants
    "SPOJ",
    "SPOJIT",
    "SPOJENI",
    "STRUKTURA",  # Czech
    "STRUKTURA",  # Polish
    "STRUKTUR",
    "VERBINDE",  # German
    "ESTRUCTURA",
    "ESTRUCT",  # Spanish
    "STRUTTURA",  # Italian
    "STRUCT",  # French (same as English)
]
