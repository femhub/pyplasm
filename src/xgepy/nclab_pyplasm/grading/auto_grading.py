"""
AUTOGRADING Module
"""


from ..utils.common import flatten
from ..geometry.base import BASEOBJ, EMPTYSET
from ..geometry.box import BOX
from ..operations.difference import DIFFERENCE
from ..operations.intersection import INTERSECTION
from ..operations.move import MOVE
from ..geometry.bounds import *
from ..geometry.brick import BRICK
from ..operations.sizes import *
from ..operations.subtract import SUBTRACT

__all__ = [
    # Dimension testing
    "IS2D",
    "IS3D",
    # Set operations
    "SUBSET",
    "DISJOINT",
    # Box testing (2D)
    "HASBOX2D",
    "HASNTBOX2D",
    "ISINBOX2D",
    # Box testing (3D)
    "HASBOX3D",
    "HASNTBOX3D",
    "ISINBOX3D",
    # Size testing
    "SIZETEST2D",
    "SIZETEST3D",
    "SIZEMATCH2D",
    "SIZEMATCH3D",
    # Position testing
    "POSITIONTEST2D",
    "POSITIONTEST3D",
    "POSITIONMATCH2D",
    "POSITIONMATCH3D",
    # Position adjustment
    "ADJUSTPOSITION3D",
    "ALIGNOBJECTS2D",
    "ALIGNOBJECTS3D",
    # Bounding box testing
    "BBTEST2D",
    "BBTEST3D",
    "BBOXTEST2D",
    "BBOXTEST3D",
    # Frame generation
    "FRAME2D",
    "FRAME3D",
]


# Is the object "tested" two-dimensional?
def IS2D(tested):
    if not isinstance(tested, list):
        return tested.dim == 2
    else:
        result = True
        flat = flatten(tested)
        for obj in flat:
            if obj.dim != 2:
                result = False
        return result


# Is the object "tested" three-dimensional?


def IS3D(tested):
    if not isinstance(tested, list):
        return tested.dim == 3
    else:
        result = True
        flat = flatten(tested)
        for obj in flat:
            if obj.dim != 3:
                result = False
        return result


def SUBSET(small, big):
    emptysetwarning = False
    difference = DIFFERENCE(small, big, emptysetwarning)
    if EMPTYSET(difference):
        return True
    else:
        return False


# Base function. Returns True if object "tested" has an empty
# intersection with object "obj":


def DISJOINT(obj1, obj2):
    emptysetwarning = False
    test = INTERSECTION(obj1, obj2, emptysetwarning)
    if EMPTYSET(test):
        return True
    else:
        return False


# Returns True if the entire 2D box "box2d" lies in object "tested":


def HASBOX2D(tested, centerx, centery, sizex, sizey):
    box2d = BOX(sizex, sizey)
    MOVE(box2d, centerx - 0.5 * sizex, centery - 0.5 * sizey)
    return SUBSET(box2d, tested)


# Returns True if no part of the 2D box "box2d" lies in object "tested":


def HASNTBOX2D(tested, centerx, centery, sizex, sizey):
    box2d = BOX(sizex, sizey)
    MOVE(box2d, centerx - 0.5 * sizex, centery - 0.5 * sizey)
    return DISJOINT(tested, box2d)


# Returns True if object "tested" lies within a 2D box of given dimensions:


def ISINBOX2D(tested, minx, maxx, miny, maxy, tol=1e-8):
    xok = (MINX(tested) >= minx - tol) and (MAXX(tested) <= maxx + tol)
    yok = (MINY(tested) >= miny - tol) and (MAXY(tested) <= maxy + tol)
    return xok and yok


# Returns True if entire 3D box "box3d" lies in object "tested":


def HASBOX3D(tested, centerx, centery, centerz, sizex, sizey, sizez):
    box3d = BOX(
        centerx - 0.5 * sizex,
        centerx + 0.5 * sizex,
        centery - 0.5 * sizey,
        centery + 0.5 * sizey,
        centerz - 0.5 * sizez,
        centerz + 0.5 * sizez,
    )
    return SUBSET(box3d, tested)


# Returns True if no part of the 3D box "box3d" lies in object "tested":


def HASNTBOX3D(tested, centerx, centery, centerz, sizex, sizey, sizez):
    brick = BRICK(sizex, sizey, sizez)
    MOVE(brick, centerx - 0.5 * sizex, centery - 0.5 * sizey, centerz - 0.5 * sizez)
    return DISJOINT(brick, tested)


# Returns True if object "tested" lies within a 3D box of given dimensions:


def ISINBOX3D(tested, minx, maxx, miny, maxy, minz, maxz, tol=1e-8):
    xok = (MINX(tested) >= minx - tol) and (MAXX(tested) <= maxx + tol)
    yok = (MINY(tested) >= miny - tol) and (MAXY(tested) <= maxy + tol)
    zok = (MINZ(tested) >= minz - tol) and (MAXZ(tested) <= maxz + tol)
    return xok and yok and zok


# Checks if 2D object "tested" has dimensions sizex, sizey
# with a given tolerance:


def SIZETEST2D(tested, sizex, sizey, eps=1e-8):
    a1 = abs(SIZEX(tested) - sizex) <= eps
    a2 = abs(SIZEY(tested) - sizey) <= eps
    return a1 and a2


# Checks if 3D object "tested" has dimensions sizex, sizey, sizez
# with a given tolerance:


def SIZETEST3D(tested, sizex, sizey, sizez, eps=1e-8):
    a1 = abs(SIZEX(tested) - sizex) <= eps
    a2 = abs(SIZEY(tested) - sizey) <= eps
    a3 = abs(SIZEZ(tested) - sizez) <= eps
    return a1 and a2 and a3


# Checks whether the bounding box of the 2D object "tested" is
# (minx, maxx) x (miny. maxy):


def BBTEST2D(tested, minx, maxx, miny, maxy, eps=1e-8):
    a1 = abs(MINX(tested) - minx) <= eps
    a2 = abs(MAXX(tested) - maxx) <= eps
    a3 = abs(MINY(tested) - miny) <= eps
    a4 = abs(MAXY(tested) - maxy) <= eps
    return a1 and a2 and a3 and a4


# Checks whether the bounding box of the 3D object "tested" is
# (minx, maxx) x (miny. maxy) x (minz. maxz):


def BBTEST3D(tested, minx, maxx, miny, maxy, minz, maxz, eps=1e-8):
    a1 = abs(MINX(tested) - minx) <= eps
    a2 = abs(MAXX(tested) - maxx) <= eps
    a3 = abs(MINY(tested) - miny) <= eps
    a4 = abs(MAXY(tested) - maxy) <= eps
    a5 = abs(MINZ(tested) - minz) <= eps
    a6 = abs(MAXZ(tested) - maxz) <= eps
    return a1 and a2 and a3 and a4 and a5 and a6


# Checks if 2D objects "tested" and "ref" have the same dimensions,
# with a given tolerance:


def SIZEMATCH2D(tested, ref, eps=1e-8):
    a1 = abs(SIZEX(tested) - SIZEX(ref)) <= eps
    a2 = abs(SIZEY(tested) - SIZEY(ref)) <= eps
    return a1 and a2


# Checks if 3D objects "tested" and "ref" have the same dimensions,
# with a given tolerance:


def SIZEMATCH3D(tested, ref, eps=1e-8):
    a1 = abs(SIZEX(tested) - SIZEX(ref)) <= eps
    a2 = abs(SIZEY(tested) - SIZEY(ref)) <= eps
    a3 = abs(SIZEZ(tested) - SIZEZ(ref)) <= eps
    return a1 and a2 and a3


# Checks if 2D object "tested" has given minx, miny
# coordinates in the x, y directions, with a given tolerance:


def POSITIONTEST2D(tested, minx, miny, eps=1e-8):
    b1 = abs(tested.minx() - minx) <= eps
    b2 = abs(tested.miny() - miny) <= eps
    return b1 and b2


# Checks if 3D object "tested" has given minx, miny, minz
# coordinates in the x, y, z directions, with a given tolerance:


def POSITIONTEST3D(tested, minx, miny, minz, eps=1e-8):
    b1 = abs(tested.minx() - minx) <= eps
    b2 = abs(tested.miny() - miny) <= eps
    b3 = abs(tested.minz() - minz) <= eps
    return b1 and b2 and b3


# Checks if 2D objects "tested" and "ref" have the same
# minimum coordinates in the x, y directions,
# with a given tolerance:


def POSITIONMATCH2D(tested, ref, eps=1e-8):
    b1 = abs(tested.minx() - ref.minx()) <= eps
    b2 = abs(tested.miny() - ref.miny()) <= eps
    return b1 and b2


# Checks if 3D objects "tested" and "ref" have the same
# minimum coordinates in the x, y, z directions,
# with a given tolerance:


def POSITIONMATCH3D(tested, ref, eps=1e-8):
    b1 = abs(tested.minx() - ref.minx()) <= eps
    b2 = abs(tested.miny() - ref.miny()) <= eps
    b3 = abs(tested.minz() - ref.minz()) <= eps
    return b1 and b2 and b3


# Move 2D object "tested" so that it has given minx, miny:


def ADJUSTPOSITION3D(tested, minx, miny):
    xmintested = tested.minx()
    ymintested = tested.miny()
    MOVE(tested, minx - xmintested, miny - ymintested)
    return tested


# Move 3D object "tested" so that it has given minx, miny, minz:


def ADJUSTPOSITION3D(tested, minx, miny, minz):
    xmintested = tested.minx()
    ymintested = tested.miny()
    zmintested = tested.minz()
    return MOVE(tested, minx - xmintested, miny - ymintested, minz - zmintested)


# Move 2D object "tested" so that its minx coincides with minx of object ref,
# and its miny coincides with miny of object ref:


def ALIGNOBJECTS2D(tested, ref):
    xmintested = tested.minx()
    ymintested = tested.miny()
    xminref = ref.minx()
    yminref = ref.miny()
    MOVE(tested, xminref - xmintested, yminref - ymintested)
    return tested


# Move 3D object "tested" so that its minx coincides with minx of object ref,
# its miny coincides with miny of object ref. and its minz coincides
# with minz of object ref:


def ALIGNOBJECTS3D(tested, ref):
    xmintested = tested.minx()
    ymintested = tested.miny()
    zmintested = tested.minz()
    xminref = ref.minx()
    yminref = ref.miny()
    zminref = ref.minz()
    MOVE(tested, xminref - xmintested, yminref - ymintested, zminref - zmintested)
    return tested


# Returns a rectangle which is the bounding box of a 2D object "tested":


def BBOXTEST2D(tested, minx, maxx, miny, maxy, tol=1e-8):
    testminx = MINX(tested)
    testmaxx = MAXX(tested)
    testminy = MINY(tested)
    testmaxy = MAXY(tested)
    a1 = abs(testminx - minx) <= tol
    a2 = abs(testmaxx - maxx) <= tol
    a3 = abs(testminy - miny) <= tol
    a4 = abs(testmaxy - maxy) <= tol
    return a1 and a2 and a3 and a4


# Returns a brick which is the bounding box of a 3D object "tested":


def BBOXTEST3D(tested, minx, maxx, miny, maxy, minz, maxz, tol=1e-8):
    testminx = MINX(tested)
    testmaxx = MAXX(tested)
    testminy = MINY(tested)
    testmaxy = MAXY(tested)
    testminz = MINZ(tested)
    testmaxz = MAXZ(tested)
    a1 = abs(testminx - minx) <= tol
    a2 = abs(testmaxx - maxx) <= tol
    a3 = abs(testminy - miny) <= tol
    a4 = abs(testmaxy - maxy) <= tol
    a5 = abs(testminz - minz) <= tol
    a6 = abs(testmaxz - maxz) <= tol
    return a1 and a2 and a3 and a4 and a5 and a6


# Returns the frame of a 2D box. Bars of
# the frame will have thicknesses


def FRAME2D(x, y, hx, hy):
    box = BOX(x, y)
    rect = BOX(x - 2 * hx, y - 2 * hy)
    MOVE(rect, hx, hy)
    SUBTRACT(box, rect)
    return box


# Returns the frame of a 3D box. Bars of
# the frame will have thicknesses hx, hy, hz


def FRAME3D(x, y, z, hx, hy, hz):
    box = BOX(x, y, z)
    brickx = BOX(x, y - 2 * hy, z - 2 * hz)
    MOVE(brickx, 0, hy, hz)
    bricky = BOX(x - 2 * hx, y, z - 2 * hz)
    MOVE(bricky, hx, 0, hz)
    brickz = BOX(x - 2 * hx, y - 2 * hy, z)
    MOVE(brickz, hx, hy, 0)
    return DIFFERENCE(box, [brickx, bricky, brickz])
