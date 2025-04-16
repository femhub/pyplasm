"""
Cubic Hermite Curves Module
"""

from nclab.tools import ExceptionWT
from ...fenvs import PLASM_CUBICHERMITE, S1, S2, S3

__all__ = [
    # Main functions
    "cubichermite1",
    "cubichermite2",
    "cubichermite3",
    "CUBICHERMITE1",
    "CUBICHERMITE2",
    "CUBICHERMITE3",
    "CH1",
    "CH2",
    "CH3",
    # Language variants
    "KUBICKA_HERMITOVA1",
    "KUBICKA_HERMITOVA2",
    "KUBICKA_HERMITOVA3",  # Czech
    "KUBICZNA_HERMITOWA1",
    "KUBICZNA_HERMITOWA2",
    "KUBICZNA_HERMITOWA3",  # Polish
    "KUBISCHE_HERMITE1",
    "KUBISCHE_HERMITE2",
    "KUBISCHE_HERMITE3",  # German
    "HERMITA_CUBICA1",
    "HERMITA_CUBICA2",
    "HERMITA_CUBICA3",  # Spanish
    "HERMITE_CUBICA1",
    "HERMITE_CUBICA2",
    "HERMITE_CUBICA3",  # Italian
    "HERMITE_CUBIQUE1",
    "HERMITE_CUBIQUE2",
    "HERMITE_CUBIQUE3",  # French
]


def cubichermite1(*args):
    raise ExceptionWT(
        "Command cubichermite1() is undefined. Try CUBICHERMITE1() instead?"
    )


def cubichermite2(*args):
    raise ExceptionWT(
        "Command cubichermite2() is undefined. Try CUBICHERMITE2() instead?"
    )


def cubichermite3(*args):
    raise ExceptionWT(
        "Command cubichermite3() is undefined. Try CUBICHERMITE3() instead?"
    )


def CUBICHERMITE1(*args):
    return PLASM_CUBICHERMITE(S1)(list(args))


def CUBICHERMITE2(*args):
    return PLASM_CUBICHERMITE(S2)(list(args))


def CUBICHERMITE3(*args):
    return PLASM_CUBICHERMITE(S3)(list(args))


CH1 = CUBICHERMITE1  # Cubic Hermite 1
CH2 = CUBICHERMITE2  # Cubic Hermite 2
CH3 = CUBICHERMITE3  # Cubic Hermite 3

# Czech:
KUBICKA_HERMITOVA1 = CUBICHERMITE1  # Cubic Hermite 1
KUBICKA_HERMITOVA2 = CUBICHERMITE2  # Cubic Hermite 2
KUBICKA_HERMITOVA3 = CUBICHERMITE3  # Cubic Hermite 3

# Polish:
KUBICZNA_HERMITOWA1 = CUBICHERMITE1  # Cubic Hermite 1
KUBICZNA_HERMITOWA2 = CUBICHERMITE2  # Cubic Hermite 2
KUBICZNA_HERMITOWA3 = CUBICHERMITE3  # Cubic Hermite 3

# German:
KUBISCHE_HERMITE1 = CUBICHERMITE1  # Cubic Hermite 1
KUBISCHE_HERMITE2 = CUBICHERMITE2  # Cubic Hermite 2
KUBISCHE_HERMITE3 = CUBICHERMITE3  # Cubic Hermite 3

# Spanish:
HERMITA_CUBICA1 = CUBICHERMITE1  # Cubic Hermite 1
HERMITA_CUBICA2 = CUBICHERMITE2  # Cubic Hermite 2
HERMITA_CUBICA3 = CUBICHERMITE3  # Cubic Hermite 3

# Italian:
HERMITE_CUBICA1 = CUBICHERMITE1  # Cubic Hermite 1
HERMITE_CUBICA2 = CUBICHERMITE2  # Cubic Hermite 2
HERMITE_CUBICA3 = CUBICHERMITE3  # Cubic Hermite 3

# French:
HERMITE_CUBIQUE1 = CUBICHERMITE1  # Cubic Hermite 1
HERMITE_CUBIQUE2 = CUBICHERMITE2  # Cubic Hermite 2
HERMITE_CUBIQUE3 = CUBICHERMITE3
