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
    """
    Prepares objects for visualization by packaging geometry, color, and material.
    """
    if not isinstance(objects, list):
        objects = [objects]

    items_for_converter = []
    for i, x in enumerate(objects):
        if not isinstance(x, BASEOBJ):
            raise ExceptionWT("The arguments must be objects!")

        obj_geom = x.geom
        obj_color = x.color
        obj_opacity = x.opacity
        obj_shininess = x.shininess
        item_data = (obj_geom, obj_color, obj_opacity, obj_shininess)
        items_for_converter.append(item_data)

    nclabinst.visualize(nclabinst.converter(items_for_converter))
