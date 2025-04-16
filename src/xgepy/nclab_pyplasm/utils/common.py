"""
Utilities for nclab_pyplasm.
"""


def flatten(*args):
    """Takes lists (possibly including other lists) and returns one plain list."""

    output = []
    for arg in args:
        if hasattr(arg, "__iter__"):
            output.extend(flatten(*arg))
        else:
            output.append(arg)
    return output


def ISNUMBER(x):
    if not isinstance(x, int) and not isinstance(x, int) and not isinstance(x, float):
        return False
    else:
        return True
