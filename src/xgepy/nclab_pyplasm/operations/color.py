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


def COLOR(obj, color=None, opacity=None, shininess=None):
    # obj may be a single object or a list of objects
    if color is None:
        raise ExceptionWT(
            "The COLOR command takes two arguments: a 2D or 3D object and a color."
        )

    if opacity is not None and (opacity < 0.0 or opacity > 1.0):
        raise ExceptionWT("Opacity value must be between 0.0 and 1.0.")

    if isinstance(color, list) and len(color) == 4 and (opacity is not None):
        raise ExceptionWT(
            "You are already providing an opacity value in the color list. Please remove the 'opacity' parameter."
        )

    if shininess is not None and (shininess < 0.0 or shininess > 1.0):
        raise ExceptionWT("Shininess value must be between 0.0 and 1.0.")

    if not isinstance(obj, list):
        if not isinstance(obj, BASEOBJ):
            raise ExceptionWT("The first argument of COLOR must be an object!")
        if opacity is not None:
            object.opacity = opacity
        if shininess is not None:
            object.shininess = shininess
        obj.setcolor(color)
    else:
        obj = flatten(obj)
        for x in obj:
            if isinstance(x, tuple):
                raise ExceptionWT("Use the UNION command to create unions of objects.")
            if not isinstance(x, BASEOBJ):
                raise ExceptionWT("Invalid object found (color - 1).")
            if opacity is not None:
                object.opacity = opacity
            if shininess is not None:
                object.shininess = shininess
            x.setcolor(color)


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
