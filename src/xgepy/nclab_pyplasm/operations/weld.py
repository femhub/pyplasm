"""
Weld Operations Module

This module provides functions for performing hard union operations on geometric objects.
The WELD function creates a single object by combining multiple objects through a
computationally expensive but precise boolean union operation.
"""


from nclab.tools import ExceptionWT
from ..utils.common import flatten
from ..geometry.base import BASEOBJ
from ...fenvs import plasm_config, Plasm, BOOL_CODE_OR


def weld(*args):
    raise ExceptionWT("Command weld() is undefined. Try WELD() instead?")


def WELD(*args):
    objs = list(args)
    objs = flatten(objs)
    geoms = []
    for x in objs:
        geoms.append(x.geom)
    color = objs[0].getcolor()
    result = BASEOBJ(
        Plasm.boolop(
            BOOL_CODE_OR,
            geoms,
            plasm_config.tolerance(),
            plasm_config.maxnumtry(),
            plasm_config.useOctreePlanes(),
        )
    )
    result.setcolor(color)
    return result


__all__ = [
    "weld",
    "WELD",
]
