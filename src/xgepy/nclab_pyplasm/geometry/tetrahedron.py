"""
Tetrahedron Geometry Module
"""


from nclab.tools import ExceptionWT
from ..geometry.base import BASEOBJ
from ...fenvs import PLASM_CONVEXHULL

__all__ = [
    "tetrahedron",
    "TETRAHEDRON",
    # English aliases
    "TET",
    # Language variants
    "TETRAEDR",
    "CTYRSTEN",  # Czech
    "CZWOROBOK",
    "CZWOROSCIAN",  # Polish
    "TETRAEDER",  # German
    "TETRAEDRO",  # Spanish/Italian
    "TETRAEDRE",  # French
]


def tetrahedron(*args):
    raise ExceptionWT("Command tetrahedron() is undefined. Try TETRAHEDRON() instead?")


def TETRAHEDRON(a, b, c, d):
    return BASEOBJ(PLASM_CONVEXHULL([a, b, c, d]))


# English aliases
TET = TETRAHEDRON  # Short form

# Language aliases
# Czech:
TETRAEDR = TETRAHEDRON  # tetrahedron
CTYRSTEN = TETRAHEDRON  # four-sided

# Polish:
CZWOROBOK = TETRAHEDRON  # four-sided
CZWOROSCIAN = TETRAHEDRON  # four-faced

# German:
TETRAEDER = TETRAHEDRON  # tetrahedron

# Spanish/Italian:
TETRAEDRO = TETRAHEDRON  # tetrahedron

# French:
TETRAEDRE = TETRAHEDRON  # tetrahedron
