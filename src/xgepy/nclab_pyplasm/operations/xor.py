"""
XOR Module
"""

from nclab.tools import ExceptionWT
from ..operations.difference import DIFFERENCE

__all__ = ["xor", "XOR"]


def xor(*args):
    raise ExceptionWT("Command xor() is undefined. Try XOR() instead?")


def XOR(a, b):
    L = []
    L.append(DIFFERENCE(a, b))
    L.append(DIFFERENCE(b, a))
    return L
