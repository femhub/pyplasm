"""
TANGRAM Module
"""

from ..geometry.triangle import TRIANGLE
from ..geometry.prism import PRISM
from ..geometry.square import SQUARE
from ..geometry.quad import QUAD
from ..operations.rotate import ROTATE
from ..operations.move import MOVE
from ..colors.color_constants import BLUE, YELLOW, GREEN, RED, CYAN, PINK, ORANGE
from ..operations.color import COLOR


__all__ = [
    "TANGRAM1",
    "TANGRAM2",
    "TANGRAM3",
    "TANGRAM4",
    "TANGRAM5",
    "TANGRAM6",
    "TANGRAM7",
    # Color variants
    "TANGRAM_GREEN",
    "TANGRAM_YELLOW",
    "TANGRAM_BLUE",
    "TANGRAM_RED",
    "TANGRAM_CYAN",
    "TANGRAM_PINK",
    "TANGRAM_ORANGE",
]


def TANGRAM1():
    tangram1 = TRIANGLE([2, 2], [4, 4], [0, 4])
    tangram1 = PRISM(tangram1, 0.01)
    COLOR(tangram1, GREEN)
    return tangram1


def TANGRAM2():
    tangram2 = TRIANGLE([0, 0], [2, 2], [0, 4])
    tangram2 = PRISM(tangram2, 0.01)
    COLOR(tangram2, YELLOW)
    return tangram2


def TANGRAM3():
    tangram3 = TRIANGLE([3, 3], [4, 2], [4, 4])
    tangram3 = PRISM(tangram3, 0.01)
    COLOR(tangram3, BLUE)
    return tangram3


def TANGRAM4():
    tangram4 = SQUARE(1.4142)
    tangram4 = PRISM(tangram4, 0.01)
    COLOR(tangram4, RED)
    ROTATE(tangram4, 45)
    MOVE(tangram4, 3, 1)
    return tangram4


def TANGRAM5():
    tangram5 = TRIANGLE([1, 1], [3, 1], [2, 2])
    tangram5 = PRISM(tangram5, 0.01)
    COLOR(tangram5, CYAN)
    return tangram5


def TANGRAM6():
    tangram6 = QUAD([0, 0], [2, 0], [1, 1], [3, 1])
    tangram6 = PRISM(tangram6, 0.01)
    COLOR(tangram6, PINK)
    return tangram6


def TANGRAM7():
    tangram7 = TRIANGLE([2, 0], [4, 0], [4, 2])
    tangram7 = PRISM(tangram7, 0.01)
    COLOR(tangram7, ORANGE)
    return tangram7


TANGRAM_GREEN = TANGRAM1()
TANGRAM_YELLOW = TANGRAM2()
TANGRAM_BLUE = TANGRAM3()
TANGRAM_RED = TANGRAM4()
TANGRAM_CYAN = TANGRAM5()
TANGRAM_PINK = TANGRAM6()
TANGRAM_ORANGE = TANGRAM7()
