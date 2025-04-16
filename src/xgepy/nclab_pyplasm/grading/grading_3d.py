"""
TEMPORARY FUNCTIONALITY FOR GRADING OF 3D COURSE
"""

from ..utils.constants import Z
from ..operations.color import COLOR
from ..operations.copy_objects import COPY
from ..operations.move import MOVE
from ..operations.show import SHOW
from ..grading.auto_grading import BBTEST2D, BBTEST3D, SUBSET
from ..grading.validate import VALIDATE
from ..geometry.bounds import MINX, MAXX, MINY, MAXY, MINZ, MAXZ

__all__ = [
    "SHOW2D",
    "BBTEST",
    "SHAPETEST",
    "MAINTEST",
]


def SHOW2D(o, zlift, color=[]):
    if color != []:
        COLOR(o, color)
    MOVE(o, zlift, Z)
    SHOW(o)


def BBTEST(lab, obj, objdim, extremes, digits, tol, verbose):
    if verbose:
        lab.grade(True, "Checking bounding box...")
    minx = extremes[0]
    maxx = extremes[1]
    miny = extremes[2]
    maxy = extremes[3]
    minz = 0
    maxz = 0
    if objdim == 3:
        minz = extremes[4]
        maxz = extremes[5]
    success = True
    if objdim == 2:
        success = BBTEST2D(obj, minx, maxx, miny, maxy, tol)
    else:
        success = BBTEST3D(obj, minx, maxx, miny, maxy, minz, maxz, tol)
    if not success:
        lab.grade(False, "Bounding box test failed.")
        bminx = round(MINX(obj), digits)
        bmaxx = round(MAXX(obj), digits)
        if abs(minx - bminx) > 1e-6 or abs(maxx - bmaxx) > 1e-6:
            msg1 = (
                "X-interval should be ("
                + str(minx)
                + ", "
                + str(maxx)
                + ") ... it is ("
                + str(bminx)
                + ", "
                + str(bmaxx)
                + ")"
            )
            lab.grade(False, msg1)
        bminy = round(MINY(obj), digits)
        bmaxy = round(MAXY(obj), digits)
        if abs(miny - bminy) > 1e-6 or abs(maxy - bmaxy) > 1e-6:
            msg2 = (
                "Y-interval should be ("
                + str(miny)
                + ", "
                + str(maxy)
                + ") ... it is ("
                + str(bminy)
                + ", "
                + str(bmaxy)
                + ")"
            )
            lab.grade(False, msg2)
        if objdim == 3:
            bminz = round(MINZ(obj), digits)
            bmaxz = round(MAXZ(obj), digits)
            if abs(minz - bminz) > 1e-6 or abs(maxz - bmaxz) > 1e-6:
                msg3 = (
                    "Z-interval should be ("
                    + str(minz)
                    + ", "
                    + str(maxz)
                    + ") ... it is ("
                    + str(bminz)
                    + ", "
                    + str(bmaxz)
                    + ")"
                )
                lab.grade(False, msg3)
        return False
    else:
        if verbose:
            lab.grade(True, "Bounding box test passed.")
        return True


def SHAPETEST(lab, obj, ins, ctest, verbose):
    if verbose:
        lab.grade(True, "Checking shape...")
    if not SUBSET(ins, obj):
        lab.grade(False, "Shape test failed.")
        return False
    if not SUBSET(obj, ctest):
        lab.grade(False, "Shape test failed.")
        return False
    if verbose:
        lab.grade(True, "Shape test passed.")
    return True


def MAINTEST(
    lab, testobj, extremes, tol, digits, testfns, colors, doshapetest, showsol, verbose
):
    obj = testobj[0]
    objname = testobj[1]
    objdim = testobj[2]

    insfn = testfns[0]
    ctestfn = testfns[1]
    solfn = testfns[2]

    errcol = colors[0]
    errcolname = colors[1]
    solcol = colors[2]
    solcolname = colors[3]

    lab.gradeInfo("Checking object '" + objname + "'...")

    ##### SANITY TEST #####
    success, errmsg = VALIDATE(obj, objname, objdim)
    if success == False:
        lab.grade(False, errmsg)

        ##### BB TEST #####

    if success:
        if not BBTEST(lab, obj, objdim, extremes, digits, tol, verbose):
            success = False

    ##### SHAPE TEST #####

    if doshapetest:
        if success:
            ins = insfn(tol)
            ctest = ctestfn(tol)
            if not SHAPETEST(lab, obj, ins, ctest, verbose):
                success = False

    ##### TEST RESULTS #####

    if success:
        return True
    else:
        # Here obj is the incorrect student's solution:
        err = COPY(obj)
        if objdim == 2:
            SHOW2D(err, 0.0004, errcol)
        else:
            COLOR(err, errcol)
            SHOW(err)
        # Here sol is the correct master solution:
        if showsol:
            sol = solfn()
            if objdim == 2:
                SHOW2D(sol, 0.0006, solcol)
            else:
                COLOR(sol, solcol)
                SHOW(sol)
        # Written message:
        lab.grade(
            False, "Your object '" + objname + "' is shown in " + errcolname + "."
        )
        lab.grade(False, "It may be hidden inside the correct solution.")
        lab.grade(
            False, "Correct object '" + objname + "' is shown in " + solcolname + "."
        )
        return False
