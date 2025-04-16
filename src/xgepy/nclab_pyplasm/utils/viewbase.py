"""
View Base Module

This module provides visualization functionality for geometric objects.
It depends on BASEOBJ for type checking and object handling, and uses
the NCLab instance for actual visualization.
"""

from nclab.tools import ExceptionWT
from ..geometry.base import BASEOBJ
from ...fenvs import nclabinst


def VIEWBASE(objects):
    geoms = []
    for x in objects:
        if not isinstance(x, BASEOBJ):
            raise ExceptionWT("The arguments must be objects!")
        geoms.append(x.geom)
    nclabinst.visualize(nclabinst.converter(geoms))
