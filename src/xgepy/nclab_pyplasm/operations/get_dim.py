"""
Dimension Operations Module
"""

from ..utils.common import flatten


__all__ = ["GETDIM"]


def GETDIM(obj):
    if isinstance(obj, list):
        obj = flatten(obj)
        dim = obj[0].dim
        n = len(obj)
        for i in range(1, n):
            if dim != obj[i].dim:
                return -1
        return dim
    else:
        return obj.dim
