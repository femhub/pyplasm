"""
Spherical Shell Module
"""

import math
from ...geometry.base import BASEOBJ
from ...operations.move import MOVE
from ....fenvs import PLASM_INSR, PLASM_PROD, PLASM_INTERVALS, PI, PLASM_MAP

__all__ = ["PLASM_SHELL"]


def PLASM_SHELL(r1, r2):
    def PLASM_SHELL0(subds):
        N, M = subds
        P = 1
        dom3d = PLASM_INSR(PLASM_PROD)(
            [
                PLASM_INTERVALS(PI)(N),
                PLASM_INTERVALS(2 * PI)(M),
                PLASM_INTERVALS(r2 - r1)(P),
            ]
        )
        dom3d = BASEOBJ(dom3d)
        MOVE(dom3d, -PI / 2, 0, r1)
        domain = dom3d.geom
        fx = lambda p: p[2] * math.cos(p[0]) * math.sin(p[1])
        fy = lambda p: p[2] * math.cos(p[0]) * math.cos(p[1])
        fz = lambda p: p[2] * math.sin(p[0])
        ret = PLASM_MAP([fx, fy, fz])(domain)
        return ret

    return PLASM_SHELL0
