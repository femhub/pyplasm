"""
TETRIS 3d Module
"""

from ..utils.common import flatten
from ..utils.constants import X, Y, Z
from ..colors.color_constants import STEEL
from ..geometry.cube import CUBE
from ..operations.move import MOVE
from ..operations.color import COLOR
from ..operations.rotate import ROTATE
from ..operations.erase import ERASE
from ..operations.union import UNION
from ..operations.copy_objects import COPY
from ..operations.weld import WELD

__all__ = [
    "block",
    "tetris_L",
    "tetris_S",
    "tetris_T",
    "tetris_C",
    "tetris_I",
    "tetris_D1",
    "tetris_D2",
    "tetris_D3",
    "TETRIS_L",
    "TETRIS_S",
    "TETRIS_T",
    "TETRIS_C",
    "TETRIS_I",
    "TETRIS_D1",
    "TETRIS_D2",
    "TETRIS_D3",
]


def block(color, layer=0):
    a = CUBE(1 + 2 * layer)
    MOVE(a, -layer, -layer, -layer)
    COLOR(a, color)
    ERASE(a, 0.5, 2, X)
    ERASE(a, 0.5, 2, Y)
    ERASE(a, 0.5, 2, Z)

    ROTATE(a, 45, Z, [0.1, 0.1, 0.1])
    ERASE(a, -5, -layer, Y)
    ROTATE(a, -45, Z, [0.1, 0.1, 0.1])

    ROTATE(a, 45, X, [0.1, 0.1, 0.1])
    ERASE(a, -5, -layer, Z)
    ROTATE(a, -45, X, [0.1, 0.1, 0.1])

    ROTATE(a, -45, Y, [0.1, 0.1, 0.1])
    ERASE(a, -5, -layer, Z)
    ROTATE(a, 45, Y, [0.1, 0.1, 0.1])

    a2 = COPY(a)
    ROTATE(a2, 90, Z, [0.5, 0.5, 0.5])
    a = UNION(a, a2)
    a3 = COPY(a)
    ROTATE(a3, 180, Z, [0.5, 0.5, 0.5])
    a = UNION(a, a3)
    a4 = COPY(a)
    ROTATE(a4, 180, X, [0.5, 0.5, 0.5])
    a = UNION(a, a4)
    a = flatten(a)
    a = WELD(a)
    return a


def tetris_L(color=STEEL, layer=0):
    b1 = block(color, layer)
    b2 = block(color, layer)
    MOVE(b2, 1, 0, 0)
    b3 = block(color, layer)
    MOVE(b3, 0, 1, 0)
    b4 = block(color, layer)
    MOVE(b4, 0, 2, 0)
    b = UNION(b1, b2, b3, b4)
    return flatten(b)


def tetris_S(color=STEEL, layer=0):
    b1 = block(color, layer)
    b2 = block(color, layer)
    MOVE(b2, 1, 0, 0)
    b3 = block(color, layer)
    MOVE(b3, 1, 1, 0)
    b4 = block(color, layer)
    MOVE(b4, 2, 1, 0)
    b = UNION(b1, b2, b3, b4)
    return flatten(b)


def tetris_T(color=STEEL, layer=0):
    b1 = block(color, layer)
    b2 = block(color, layer)
    MOVE(b2, 1, 0, 0)
    b3 = block(color, layer)
    MOVE(b3, 1, 1, 0)
    b4 = block(color, layer)
    MOVE(b4, 2, 0, 0)
    b = UNION(b1, b2, b3, b4)
    return flatten(b)


def tetris_C(color=STEEL, layer=0):
    b1 = block(color, layer)
    b2 = block(color, layer)
    MOVE(b2, 1, 0, 0)
    b3 = block(color, layer)
    MOVE(b3, 0, 1, 0)
    b4 = block(color, layer)
    MOVE(b4, 1, 1, 0)
    b = UNION(b1, b2, b3, b4)
    return flatten(b)


def tetris_I(color=STEEL, layer=0):
    b1 = block(color, layer)
    b2 = block(color, layer)
    MOVE(b2, 1, 0, 0)
    b3 = block(color, layer)
    MOVE(b3, 2, 0, 0)
    b4 = block(color, layer)
    MOVE(b4, 3, 0, 0)
    b = UNION(b1, b2, b3, b4)
    return flatten(b)


def tetris_D1(color=STEEL, layer=0):
    b1 = block(color, layer)
    b2 = block(color, layer)
    MOVE(b2, 1, 0, 0)
    b3 = block(color, layer)
    MOVE(b3, 0, 1, 0)
    b4 = block(color, layer)
    MOVE(b4, 0, 0, 1)
    b = UNION(b1, b2, b3, b4)
    return flatten(b)


def tetris_D2(color=STEEL, layer=0):
    b1 = block(color, layer)
    b2 = block(color, layer)
    MOVE(b2, 1, 0, 0)
    b3 = block(color, layer)
    MOVE(b3, 0, 1, 0)
    b4 = block(color, layer)
    MOVE(b4, 1, 0, 1)
    b = UNION(b1, b2, b3, b4)
    return flatten(b)


def tetris_D3(color=STEEL, layer=0):
    b1 = block(color, layer)
    b2 = block(color, layer)
    MOVE(b2, 1, 0, 0)
    b3 = block(color, layer)
    MOVE(b3, 0, 1, 0)
    b4 = block(color, layer)
    MOVE(b4, 0, 1, 1)
    b = UNION(b1, b2, b3, b4)
    return flatten(b)


TETRIS_L = tetris_L()
TETRIS_S = tetris_S()
TETRIS_T = tetris_T()
TETRIS_C = tetris_C()
TETRIS_I = tetris_I()
TETRIS_D1 = tetris_D1()
TETRIS_D2 = tetris_D2()
TETRIS_D3 = tetris_D3()
