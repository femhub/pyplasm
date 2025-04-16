"""
Product and Power Operations Module

This module provides functions for performing geometric product/power operations.
The PRODUCT function creates a new object by combining two geometric objects,
preserving color information and handling various input types.
"""


from nclab.tools import ExceptionWT
from ..utils.common import flatten
from ..geometry.base import BASEOBJ
from ...fenvs import PLASM_POWER


__all__ = [
    "product",
    "power",
    "PRODUCT",
    "POWER",
    # Language variants
    "MOCNINA",
    "PRODUKT",
    "SOUCIN",
    "UMOCNIT",
    "UMOCNI",  # Czech
    "MOC",
    "ILOCZYN",
    "PRODUKT",  # Polish
    "PRODUKT",  # German
    "POTENCIA",
    "PRODUCTO",  # Spanish
    "POTENZA",
    "PRODOTTO",  # Italian
    "PUISSANCE",
    "PRODUIT",  # French
]


def product(*args):
    raise ExceptionWT("Command product() is undefined. Try PRODUCT() instead?")


def power(*args):
    raise ExceptionWT("Command power() is undefined. Try POWER() instead?")


def PRODUCT(*args):
    list1 = list(args)
    list1 = flatten(list1)
    if len(list1) != 2:
        raise Exception("PRODUCT(...) requires two arguments!")
    list2 = []
    color = list1[0].color
    for x in list1:
        list2.append(x.geom)
    obj = BASEOBJ(PLASM_POWER(list2))
    obj.setcolor(color)
    return obj


# English:
POWER = PRODUCT

# Czech:
MOCNINA = POWER
PRODUKT = POWER
SOUCIN = POWER
UMOCNIT = POWER
UMOCNI = POWER

# Polish:
MOC = POWER
ILOCZYN = POWER
PRODUKT = POWER

# German:
PRODUKT = POWER

# Spanish:
POTENCIA = POWER
PRODUCTO = POWER

# Italian:
POTENZA = POWER
PRODOTTO = POWER

# French:
PUISSANCE = POWER
PRODUIT = POWER
