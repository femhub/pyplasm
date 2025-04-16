"""
TEMPORARY FUNCTIONALITY FOR GRADING OF TURTLE COURSE
"""

from ..geometry.base import EMPTYSET
from ..turtle.turtle_2d import NCLabTurtle
from ..turtle.turtle_2d_utils import NCLabTurtleTrace, NCLAB_TURTLE_EPS
from ..grading.auto_grading import SUBSET
from ..operations.color import COLOR
from ..operations.show import SHOW


def TURTLETEST(
    lab,
    turtle,
    tsol,
    solcol,
    solcolname,
    solheight,
    errcol,
    errcolname,
    errheight,
    incltest,
    comptest,
    colortest,
    testcol,
    testcolname,
    extrusionflag,
    extrusionheight,
):
    if not isinstance(turtle, NCLabTurtle):
        lab.grade(False, "The turtle is not an NCLabTurtle!")
        return False

    ##### COLOR TEST #####

    if colortest:
        if turtle.getcolor() != testcol:
            lab.grade(False, "Please use " + testcolname + " color!")
            return False

    ##### EXTRUSION TEST #####

    if extrusionflag:
        if not turtle.extrudecalled or turtle.lineheight != extrusionheight:
            lab.grade(
                False, "Please use extrusion height " + str(extrusionheight) + "!"
            )
            return False

    ##### PREPARE TESTING DATA #####

    # Students trace without the circles:
    trace = NCLabTurtleTrace(turtle.lines, 0, False)

    # EMPTYSET?
    if EMPTYSET(trace):
        lab.grade(False, "The turtle did not draw any lines.")
        return False

    # Subset and superset:
    eps = NCLAB_TURTLE_EPS
    subset = NCLabTurtleTrace(tsol.lines, -eps, False)
    superset = NCLabTurtleTrace(tsol.lines, eps, False)

    ##### GEOMETRY TEST #####

    succ1 = True
    if incltest:
        succ1 = SUBSET(subset, trace)

    succ2 = True
    if comptest:
        succ2 = SUBSET(trace, superset)

    if not succ1 or not succ2:
        # Show wrong solution in 'errcol' color:
        err = None
        if extrusionflag and turtle.extrudecalled:
            turtle.extrude(extrusionheight + 0.01)
            err = turtle.geometry()
        else:
            if turtle.heightused:  # There are different heights:
                layer = 0.01
                dots = True
                err = NCLabTurtleTrace(turtle.lines, layer, dots)
            else:  # Genuinely 2D
                turtle.extrude(errheight)
                err = turtle.geometry()
        COLOR(err, errcol)
        SHOW(err)
        # Show correct solution in 'solcol' color:
        sol = None
        if extrusionflag and turtle.extrudecalled:
            tsol.extrude(extrusionheight + 0.02)
            sol = tsol.geometry()
        else:
            if turtle.heightused:  # There are different heights:
                layer = 0.02
                dots = True
                sol = NCLabTurtleTrace(tsol.lines, layer, dots)
            else:  # Genuinely 2D
                tsol.extrude(solheight)
                sol = tsol.geometry()
        COLOR(sol, solcol)
        SHOW(sol)
        lab.grade(False, "The trace is not correct.")
        lab.grade(False, "The correct trace is shown in " + solcolname + ".")
        lab.grade(False, "Your solution is shown in " + errcolname + ".")
        lab.grade(False, "It may be hidden inside the correct solution.")
        return False

    ##### ALL TESTS PASSED #####
    return True
