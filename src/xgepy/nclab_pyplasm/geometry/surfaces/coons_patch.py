"""
Coons Patch Surface Module
"""

from ...domain.references import UNITSQUARE
from ...operations.map import MAP
from ....fenvs import PLASM_COONSPATCH

__all__ = ["COONSPATCH"]


def COONSPATCH(u1, u2, v1, v2, nx=32, ny=32):
    refdomain = UNITSQUARE(nx, ny)
    surf = PLASM_COONSPATCH([u1, u2, v1, v2])
    out = MAP(refdomain, surf)
    return out
