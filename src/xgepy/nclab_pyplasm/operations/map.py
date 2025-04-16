"""
Map Operation Module
"""

from ..geometry.base import BASEOBJ
from ...fenvs import PLASM_MAP


def MAP(refdomain, args):
    return BASEOBJ(PLASM_MAP(args)(refdomain.geom))
