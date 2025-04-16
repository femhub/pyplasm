"""
COLORBAR Module
"""

from ..utils.constants import X
from ..geometry.rectangle import RECTANGLE
from ..operations.move import MOVE
from ..operations.color import COLOR
from ..operations.copy_objects import COPY

__all__ = ["COLORBAR"]


def COLORBAR(*args):
    # Sanity checks:
    l = list(args)
    if len(l) < 3:
        print(
            "Function COLORBAR must have at least three arguments. Usage: COLORBAR(a, b, c1, c2, ...) where a, b are the dimensions of the color bar, and c1, c2, ... are colors in the [R, G, B] form."
        )
        return
    a = l[0]
    b = l[1]
    if not isinstance(a, int) and not isinstance(a, float):
        print("The first argument 'a' of COLORBAR(a, b, c1, c2, ...) must be a number.")
        return
    if a <= 0:
        print("The first argument 'a' of COLORBAR(a, b, c1, c2, ...) must be positive.")
        return
    if not isinstance(b, int) and not isinstance(b, float):
        print(
            "The second argument 'b' of COLORBAR(a, b, c1, c2, ...) must be a number."
        )
        return
    if b <= 0:
        print(
            "The second argument 'b' of COLORBAR(a, b, c1, c2, ...) must be positive."
        )
        return
    # How many colors:
    n = len(l) - 2
    # Test all the colors:
    for i in range(2, 2 + n):
        c = l[i]
        if not isinstance(c, list):
            print(
                "There was a problem with color #"
                + str(i - 1)
                + " in the COLORBAR() function. Make sure that every color has the form [R, G, B] where R, G, B are numbers between 0 and 255."
            )
            return
        if len(c) != 3:
            print(
                "There was a problem with color #"
                + str(i - 1)
                + " in the COLORBAR() function. Make sure that every color has the form [R, G, B] where R, G, B are numbers between 0 and 255."
            )
            return
        if not isinstance(c[0], int) and not isinstance(c[0], float):
            print(
                "There was a problem with color #"
                + str(i - 1)
                + " in the COLORBAR() function. The first component of the color is not a number."
            )
            return
        if c[0] < 0 or c[0] > 255:
            print(
                "There was a problem with color #"
                + str(i - 1)
                + " in the COLORBAR() function. The first component of the color is not a number between 0 and 255."
            )
            return
        if not isinstance(c[1], int) and not isinstance(c[1], float):
            print(
                "There was a problem with color #"
                + str(i - 1)
                + " in the COLORBAR() function. The second component of the color is not a number."
            )
            return
        if c[1] < 0 or c[1] > 255:
            print(
                "There was a problem with color #"
                + str(i - 1)
                + " in the COLORBAR() function. The second component of the color is not a number between 0 and 255."
            )
            return
        if not isinstance(c[2], int) and not isinstance(c[2], float):
            print(
                "There was a problem with color #"
                + str(i - 1)
                + " in the COLORBAR() function. The third component of the color is not a number."
            )
            return
        if c[2] < 0 or c[2] > 255:
            print(
                "There was a problem with color #"
                + str(i - 1)
                + " in the COLORBAR() function. The third component of the color is not a number between 0 and 255."
            )
            return
    # Define list of colors:
    cols = l[:]
    del cols[0]
    del cols[0]
    # Build the bar:
    w = a / n
    base = RECTANGLE(w, b)
    bars = []
    for i in range(n):
        bar = COPY(base)
        MOVE(bar, i * w, X)
        COLOR(bar, cols[i])
        bars.append(bar)
    return bars
