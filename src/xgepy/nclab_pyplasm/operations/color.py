"""
Color Module
"""

from nclab.tools import ExceptionWT
from ..utils.common import flatten
from ..geometry.base import BASEOBJ

__all__ = [
    # Main functions
    "color",  # Error-raising lowercase version
    "COLOR",  # Main function
    "C",  # English alias
    # Language variants
    "BARVA",
    "OBARVI",
    "OBARVIT",  # Czech
    "KOLOR",  # Polish
    "FARBE",  # German
    "COLORE",  # Italian
    "COULEUR",  # French
]


def color(*args):
    raise ExceptionWT("Command color() is undefined. Try COLOR() instead?")


def COLOR(obj, col=None):
    # obj may be a single object or a list of objects
    if col is None:
        raise ExceptionWT(
            "The COLOR command takes two arguments: a 2D or 3D object and a color."
        )
    if not isinstance(obj, list):
        if not isinstance(obj, BASEOBJ):
            raise ExceptionWT("The first argument of COLOR must be an object!")
        obj.setcolor(col)
    else:
        obj = flatten(obj)
        for x in obj:
            if isinstance(x, tuple):
                raise ExceptionWT("Use the UNION command to create unions of objects.")
            if not isinstance(x, BASEOBJ):
                raise ExceptionWT("Invalid object found (color - 1).")
            x.setcolor(col)


C = COLOR  # Short form

# Language variants
# Czech:
BARVA = COLOR  # Color
OBARVI = COLOR  # Color it
OBARVIT = COLOR  # To color

# Polish:
KOLOR = COLOR  # Color

# German:
FARBE = COLOR  # Color

# Italian:
COLORE = COLOR  # Color

# French:
COULEUR = COLOR  # Color
