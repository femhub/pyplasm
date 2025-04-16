"""
SIMPLEX
"""

from nclab.tools import ExceptionWT
from ..geometry.base import BASEOBJ
from ...fenvs import Plasm


def simplex(*args):
    raise ExceptionWT("Command simplex() is undefined. Try SIMPLEX() instead?")


def SIMPLEX(dim):
    return BASEOBJ(Plasm.simplex(dim))


__all__ = [
    "simplex",
    "SIMPLEX",
]
