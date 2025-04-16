"""
MATERIAL MODULE
"""

from nclab.tools import ExceptionWT
from ..utils.common import flatten
from ..operations.copy_objects import COPY

__all__ = [
    "material",
    "MATERIAL",
    # Language variants
    "MATERIAL",
    "MATERIÁL",  # Czech
    "MATERIAŁ",
    "MATERIA",  # Polish
    "MATERIAL",
    "WERKSTOFF",  # German
    "MATERIAL",
    "MATERIA",  # Spanish
    "MATERIALE",
    "MATERIA",  # Italian
    "MATERIAU",
    "MATERIEL",  # French
]


def material(*args):
    raise ExceptionWT("Command material() is undefined. Try MATERIAL() instead?")


def MATERIAL(obj, mat):
    # obj may be a single object or a list of objects
    if not isinstance(obj, list):
        obj.setmaterial(mat)
    else:
        obj = flatten(obj)
        for x in obj:
            x.setmaterial(mat)
    return COPY(obj)


# Language variants
# Czech:
MATERIAL = MATERIAL  # Material
MATERIÁL = MATERIAL  # Material

# Polish:
MATERIAŁ = MATERIAL  # Material
MATERIA = MATERIAL  # Material

# German:
MATERIAL = MATERIAL  # Material
WERKSTOFF = MATERIAL  # Material

# Spanish:
MATERIAL = MATERIAL  # Material
MATERIA = MATERIAL  # Material

# Italian:
MATERIALE = MATERIAL  # Material
MATERIA = MATERIAL  # Material

# French:
MATERIAU = MATERIAL  # Material
MATERIEL = MATERIAL  # Material
