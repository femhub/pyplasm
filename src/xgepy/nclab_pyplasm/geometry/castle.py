"""
CASTLES
"""

from ..utils.constants import Z
from ..geometry.box import BOX
from ..geometry.cube import CUBE
from ..geometry.cone import CONE
from ..geometry.cylinder import CYLINDER
from ..geometry.pyramid import PYRAMID
from ..geometry.sphere import SPHERE
from ..operations.color import COLOR
from ..operations.move import MOVE
from ..operations.rotate import ROTATE
from ..operations.erase import ERASE
from ..colors.color_constants import BEIGE, RED


__all__ = ["CASTLE1", "CASTLE2", "CASTLE3", "CASTLE4", "CASTLE5", "CASTLE6", "CASTLE7"]


def CASTLE1():
    cu = CUBE(1)
    COLOR(cu, BEIGE)
    MOVE(cu, 4, 2)
    return cu


def CASTLE2():
    co = CONE(0.5, 1)
    COLOR(co, RED)
    MOVE(co, 2.5, 1.5)
    return co


def CASTLE3():
    cy = CYLINDER(0.5, 1)
    COLOR(cy, BEIGE)
    MOVE(cy, 0.5, 2.5)
    return cy


def CASTLE4():
    py = PYRAMID(0.5 * 1.414214, 1)
    COLOR(py, RED)
    ROTATE(py, 45)
    MOVE(py, 3.5, 1.5)
    return py


def CASTLE5():
    hs = SPHERE(0.5)
    ERASE(hs, -1, 0, Z)
    COLOR(hs, RED)
    MOVE(hs, 1.5, 1.5)
    return hs


def CASTLE6():
    wy = BOX(0.25, 0.75, 0, 1, 0, 1)
    COLOR(wy, BEIGE)
    return wy


def CASTLE7():
    wx = BOX(4, 5, 0.25, 0.75, 0, 1)
    COLOR(wx, BEIGE)
    return wx
