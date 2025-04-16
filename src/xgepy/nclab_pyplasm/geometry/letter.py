"""
LETTER Module
"""

from nclab.tools import ExceptionWT
from ..utils.constants import X, Y, Z
from ..geometry.quad import QUAD
from ..geometry.box import BOX
from ..geometry.arc import ARC
from ..geometry.point import POINT
from ..operations.union import UNION
from ..operations.scale import SCALE
from ..operations.rotate import ROTATE
from ..operations.move import MOVE
from ..operations.copy_objects import COPY
from ..operations.flip import MIRROR
from ..operations.subtract import SUBTRACT

__all__ = [
    "LETTER",
    # Language variants
    "PISMENO",  # Czech
    "LITERA",  # Polish
    "BUCHSTABE",  # German
    "LETRA",  # Spanish
    "LETTERA",  # Italian
    "LETTRE",  # French
    # Individual letter functions
    "letterA",
    "letterB",
    "letterC",
    "letterD",
    "letterE",
    "letterF",
    "letterG",
    "letterH",
    "letterI",
    "letterJ",
    "letterK",
    "letterL",
    "letterM",
    "letterN",
    "letterO",
    "letterP",
    "letterQ",
    "letterR",
    "letterS",
    "letterT",
    "letterU",
    "letterV",
    "letterW",
    "letterX",
    "letterY",
    "letterZ",
]


def letterA():
    l1 = QUAD([0, 0], [30, 0], [35, 150], [65, 150])
    l2 = QUAD([70, 0], [100, 0], [35, 150], [65, 150])
    le = UNION(l1, l2)
    SCALE(le, 0.1, 0.1)
    return le


# B:
def letterB():
    hr = ARC(15, 45, 180)
    ROTATE(hr, -90, Z, POINT(50, 0))
    MOVE(hr, 5, 55)
    hr2 = COPY(hr)
    MOVE(hr2, -60, Y)
    l1 = BOX(0, 55, 120, 150)
    l2 = BOX(0, 55, 0, 30)
    l3 = BOX(0, 30, 0, 90)
    le = UNION(l1, l2, l3, hr, hr2)
    SCALE(le, 0.1, 0.1)
    return le


"""
# B: VERSION 2, LOOKS A BIT LIKE '3'
def letterB():
  hr = ARC(15, 45, 180)
  ROTATE(hr, -90, Z, POINT(50, 0))
  MOVE(hr, 5, 55)
  hr2 = COPY(hr)
  MOVE(hr2, -60, Y)
  l1 = BOX(0, 55, 120, 150)
  l2 = BOX(0, 55, 0, 30)
  l3 = BOX(0, 55, 60, 90)
  le = UNION(l1, l2, l3, hr, hr2)
  SCALE(le, 0.1, 0.1)
  return le
"""


# C:
def letterC():
    hr = ARC(20, 50, 180)
    ROTATE(hr, 180)
    MOVE(hr, 50, 50)
    b3 = BOX(0, 30, 50, 100)
    hr3 = MIRROR(COPY(hr), 75, Y)
    le = UNION(hr, b3, hr3)
    SCALE(le, 0.1, 0.1)
    return le


# D:
def letterD():
    hr = ARC(20, 50, 90)
    MOVE(hr, 50, 100)
    b3 = BOX(0, 30, 0, 150)
    b4 = BOX(70, 100, 50, 100)
    b5 = BOX(30, 50, 0, 30)
    b6 = BOX(30, 50, 120, 150)
    hr3 = MIRROR(COPY(hr), 75, Y)
    le = UNION(hr, b3, b4, b5, b6, hr3)
    SCALE(le, 0.1, 0.1)
    return le


# E:
def letterE():
    l1 = BOX(0, 30, 0, 150)
    l2 = BOX(0, 100, 0, 30)
    l3 = BOX(0, 70, 60, 90)
    l4 = BOX(0, 100, 120, 150)
    le = UNION(l1, l2, l3, l4)
    SCALE(le, 0.1, 0.1)
    return le


# F:
def letterF():
    l1 = BOX(0, 30, 0, 150)
    l3 = BOX(0, 70, 60, 90)
    l4 = BOX(0, 100, 120, 150)
    le = UNION(l1, l3, l4)
    SCALE(le, 0.1, 0.1)
    return le


# G:
def letterG():
    hr = ARC(20, 50, 180)
    ROTATE(hr, 180)
    MOVE(hr, 50, 50)
    b3 = BOX(0, 30, 50, 100)
    hr3 = MIRROR(COPY(hr), 75, Y)
    b1 = BOX(80, 100, 0, 60)
    b2 = BOX(60, 100, 40, 70)
    le = UNION(hr, b3, hr3, b1, b2)
    SCALE(le, 0.1, 0.1)
    return le


# H:
def letterH():
    l1 = BOX(0, 30, 0, 150)
    l2 = BOX(70, 100, 0, 150)
    l3 = BOX(0, 100, 60, 90)
    le = UNION(l1, l2, l3)
    SCALE(le, 0.1, 0.1)
    return le


# I:
def letterI():
    le = BOX(0, 30, 0, 150)
    SCALE(le, 0.1, 0.1)
    return le


# J:
def letterJ():
    hr = ARC(20, 50, 180)
    ROTATE(hr, 180)
    MOVE(hr, 50, 50)
    b1 = BOX(70, 100, 50, 150)
    b2 = BOX(30, 70, 120, 150)
    le = UNION(hr, b1, b2)
    SCALE(le, 0.1, 0.1)
    return le


# K:
def letterK():
    le0 = BOX(0, 30, 0, 150)
    q1 = QUAD([70, 150], [100, 150], [60, 70], [30, 70])
    q2 = QUAD([70, 0], [100, 0], [60, 70], [30, 70])
    le = UNION(le0, q1, q2)
    SCALE(le, 0.1, 0.1)
    return le


# L:
def letterL():
    l1 = BOX(0, 30, 0, 150)
    l2 = BOX(0, 80, 0, 30)
    le = UNION(l1, l2)
    SCALE(le, 0.1, 0.1)
    return le


# M:
def letterM():
    ml = BOX(0, 30, 0, 150)
    mr = BOX(90, 120, 0, 150)
    mm1 = QUAD([60, 30], [90, 80], [90, 150], [60, 90])
    mm2 = QUAD([60, 30], [30, 80], [30, 150], [60, 90])
    le = UNION(ml, mr, mm1, mm2)
    SUBTRACT(le, BOX(40, 80, 0, 50))
    SCALE(le, 0.1, 0.1)
    return le


# N:
def letterN():
    nl = BOX(0, 30, 0, 150)
    nr = BOX(70, 100, 0, 150)
    nm = QUAD([30, 80], [70, 0], [70, 70], [30, 150])
    le = UNION(nl, nr, nm)
    SCALE(le, 0.1, 0.1)
    return le


# O:
def letterO():
    hr = ARC(20, 50, 180)
    ROTATE(hr, 180)
    MOVE(hr, 50, 50)
    b3 = BOX(0, 30, 50, 100)
    b4 = BOX(70, 100, 50, 100)
    hr3 = MIRROR(COPY(hr), 75, Y)
    le = UNION(hr, b3, b4, hr3)
    SCALE(le, 0.1, 0.1)
    return le


# P:
def letterP():
    hr = ARC(20, 50, 180)
    ROTATE(hr, -90, Z, POINT(50, 0))
    MOVE(hr, 0, 50)
    l1 = BOX(0, 30, 0, 80)
    l2 = BOX(0, 50, 120, 150)
    l3 = BOX(30, 50, 50, 80)
    le = UNION(l1, l2, l3, hr)
    SCALE(le, 0.1, 0.1)
    return le


# Q:
def letterQ():
    hr = ARC(20, 50, 180)
    ROTATE(hr, 180)
    MOVE(hr, 50, 50)
    b3 = BOX(0, 30, 50, 100)
    b4 = BOX(70, 100, 50, 100)
    hr3 = MIRROR(COPY(hr), 75, Y)
    s = QUAD([70, 0], [100, 0], [80, 30], [50, 30])
    le = UNION(hr, b3, b4, hr3, s)
    SCALE(le, 0.1, 0.1)
    return le


# R:
def letterR():
    hr = ARC(20, 50, 180)
    ROTATE(hr, -90, Z, POINT(50, 0))
    MOVE(hr, 0, 50)
    l1 = BOX(0, 30, 0, 80)
    l2 = BOX(0, 50, 120, 150)
    l3 = BOX(30, 50, 50, 80)
    s = QUAD([70, 0], [100, 0], [40, 60], [70, 60])
    le = UNION(l1, l2, l3, hr, s)
    SCALE(le, 0.1, 0.1)
    return le


# S:
def letterS():
    hr = ARC(15, 45, 180)
    ROTATE(hr, -90, POINT(45, 0))
    MOVE(hr, 10, X)
    hr2 = COPY(hr)
    ROTATE(hr2, 180, POINT(50, 75))
    b1 = BOX(45, 55, 60, 90)
    a1 = ARC(15, 45, 90)
    a2 = COPY(a1)
    ROTATE(a1, 180)
    MOVE(a1, 45, 45)
    MOVE(a2, 55, 105)
    b2 = BOX(45, 55, 0, 30)
    b3 = BOX(45, 55, 120, 150)
    le = UNION(hr, hr2, b1, b2, b3, a1, a2)
    SCALE(le, 0.1, 0.1)
    return le


# T:
def letterT():
    le1 = BOX(35, 65, 0, 150)
    le2 = BOX(0, 100, 120, 150)
    le = UNION(le1, le2)
    SCALE(le, 0.1, 0.1)
    return le


# U:
def letterU():
    hr = ARC(20, 50, 180)
    ROTATE(hr, 180)
    MOVE(hr, 50, 50)
    b3 = BOX(0, 30, 50, 150)
    b4 = BOX(70, 100, 50, 150)
    le = UNION(hr, b3, b4)
    SCALE(le, 0.1, 0.1)
    return le


# V:
def letterV():
    l1 = QUAD([0, 150], [30, 150], [35, 0], [65, 0])
    l2 = QUAD([70, 150], [100, 150], [35, 0], [65, 0])
    le = UNION(l1, l2)
    SCALE(le, 0.1, 0.1)
    return le


# W:
def letterW():
    l1 = QUAD([0, 150], [30, 150], [35, 0], [65, 0])
    l2 = QUAD([60, 100], [90, 100], [35, 0], [65, 0])
    l3 = QUAD([60, 100], [90, 100], [95, 0], [125, 0])
    l4 = QUAD([120, 150], [150, 150], [95, 0], [125, 0])
    le = UNION(l1, l2, l3, l4)
    SCALE(le, 0.1, 0.1)
    return le


# X:
def letterX():
    x1 = QUAD([0, 150], [30, 150], [70, 0], [100, 0])
    x2 = QUAD([0, 0], [30, 0], [70, 150], [100, 150])
    le = UNION(x1, x2)
    SCALE(le, 0.1, 0.1)
    return le


# Y:
def letterY():
    y1 = QUAD([0, 150], [30, 150], [35, 75], [65, 75])
    y2 = QUAD([35, 75], [65, 75], [70, 150], [100, 150])
    y3 = BOX(35, 65, 0, 75)
    le = UNION(y1, y2, y3)
    SCALE(le, 0.1, 0.1)
    return le


# Z:
def letterZ():
    x1 = BOX(0, 100, 120, 150)
    x2 = QUAD([0, 30], [40, 30], [60, 120], [100, 120])
    x3 = BOX(0, 100, 0, 30)
    le = UNION(x1, x2, x3)
    SCALE(le, 0.1, 0.1)
    return le


# Main function:
def LETTER(c):
    if not isinstance(c, str):
        raise ExceptionWT(
            "In LETTER(c): c must be a character (text string of length 1)."
        )
    if len(c) != 1:
        raise ExceptionWT(
            "In LETTER(c): c must be a character (text string of length 1)."
        )
    c = c.upper()
    if c == "A":
        return letterA()
    if c == "B":
        return letterB()
    if c == "C":
        return letterC()
    if c == "D":
        return letterD()
    if c == "E":
        return letterE()
    if c == "F":
        return letterF()
    if c == "G":
        return letterG()
    if c == "H":
        return letterH()
    if c == "I":
        return letterI()
    if c == "J":
        return letterJ()
    if c == "K":
        return letterK()
    if c == "L":
        return letterL()
    if c == "M":
        return letterM()
    if c == "N":
        return letterN()
    if c == "O":
        return letterO()
    if c == "P":
        return letterP()
    if c == "Q":
        return letterQ()
    if c == "R":
        return letterR()
    if c == "S":
        return letterS()
    if c == "T":
        return letterT()
    if c == "U":
        return letterU()
    if c == "V":
        return letterV()
    if c == "W":
        return letterW()
    if c == "X":
        return letterX()
    if c == "Y":
        return letterY()
    if c == "Z":
        return letterZ()
    raise ExceptionWT(
        "Unknown character '"
        + c
        + "' detected in LETTER()!\nPlease use English alphabet letters only."
    )


PISMENO = LETTER

# Polish:
LITERA = LETTER

# German:
BUCHSTABE = LETTER

# Spanish:
LETRA = LETTER

# Italian:
LETTERA = LETTER

# French:
LETTRE = LETTER
