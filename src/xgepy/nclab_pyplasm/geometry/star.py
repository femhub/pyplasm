"""
STAR MODULE
"""

from numpy import tan

from nclab.tools import ExceptionWT
from ..geometry.triangle import TRIANGLE
from ..operations.union import UNION
from ..operations.rotate import ROTATE
from ..operations.copy_objects import COPY
from ...fenvs import PI

__all__ = [
    "star",
    "STAR",
    # Language variants
    "HVĚZDA",
    "HVĚZDIČKA",  # Czech
    "GWIAZDA",
    "GWIAZDKA",  # Polish
    "STERN",
    "STERNCHEN",  # German
    "ESTRELLA",
    "ESTRELLITA",  # Spanish
    "STELLA",
    "STELLINA",  # Italian
    "ETOILE",
    "ETOILETTE",  # French
]


def star(*args):
    raise ExceptionWT("Command star() is undefined. Try STAR() instead?")


def STAR(r, n):
    if n < 5:
        raise ExceptionWT("In the STAR(r, n) command, n must be at least 5!")
    if r <= 0:
        raise ExceptionWT("In the STAR(r, n) command, the radius r must be positive!")
    beta = 2.0 * PI / n
    x = r / tan(beta)
    t0 = TRIANGLE([-x, 0], [x, 0], [0, r])
    l1 = [t0]
    angle = 360.0 / n
    for i in range(n - 1):
        l1.append(ROTATE(COPY(t0), (i + 1) * angle))
    return UNION(l1)


HVĚZDA = STAR  # Star
HVĚZDIČKA = STAR  # Little star

# Polish:
GWIAZDA = STAR  # Star
GWIAZDKA = STAR  # Little star

# German:
STERN = STAR  # Star
STERNCHEN = STAR  # Little star

# Spanish:
ESTRELLA = STAR  # Star
ESTRELLITA = STAR  # Little star

# Italian:
STELLA = STAR  # Star
STELLINA = STAR  # Little star

# French:
ETOILE = STAR  # Star
ETOILETTE = STAR  # Little star
