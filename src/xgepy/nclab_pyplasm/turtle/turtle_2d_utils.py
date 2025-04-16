"""
NCLab Turtle 2D Utilities Module

This module provides utilities for the NCLab Turtle 2D graphics system.
"""

from numpy import pi, sqrt, arctan2

from ..utils.constants import Z
from ..geometry.circle import CIRCLE
from ..geometry.ring import RING
from ..geometry.rectangle import RECTANGLE
from ..geometry.triangle import TRIANGLE
from ..geometry.quad import QUAD
from ..geometry.point import POINT
from ..operations.color import COLOR
from ..operations.move import MOVE
from ..operations.rotate import ROTATE
from ..operations.scale import SCALE
from ..geometry.prism import PRISM
from ..operations.copy_objects import COPY
from ..operations.show import SHOW
from ..colors.color_constants import BLACK


# Rectangle given via start point, distance,
# angle, width and color):
def NCLabTurtleRectangle(l, layer):
    dx = l.endx - l.startx
    dy = l.endy - l.starty
    dist = sqrt(dx * dx + dy * dy)
    angle = arctan2(dy, dx) * 180 / pi
    rect = RECTANGLE(dist + 2 * layer, l.linewidth + 2 * layer)
    MOVE(rect, -layer, -0.5 * l.linewidth - layer)
    ROTATE(rect, angle)
    COLOR(rect, l.linecolor)
    MOVE(rect, l.startx, l.starty)
    return rect


# Dots to set area size:
def NCLabTurtleCanvas(turtle):
    r = turtle.canvassize
    r /= 2
    dot1 = CIRCLE(0.1, 4)
    MOVE(dot1, r, 0)
    dot2 = COPY(dot1)
    ROTATE(dot2, 90)
    dot3 = COPY(dot2)
    ROTATE(dot3, 90)
    dot4 = COPY(dot3)
    ROTATE(dot4, 90)
    return [dot1, dot2, dot3, dot4]


def NCLabTurtleWedge(l1, l2):
    ux = l1.endx - l1.startx
    uy = l1.endy - l1.starty
    usize = sqrt(ux**2 + uy**2)
    vx = l2.endx - l2.startx
    vy = l2.endy - l2.starty
    vsize = sqrt(vx**2 + vy**2)
    # Points for the triangle:
    p1x = l1.endx
    p1y = l1.endy
    p2x = None
    p2y = None
    p3x = None
    p3y = None
    # Decide if left turn or right turn using vector product:
    val = ux * vy - uy * vx
    if val > 0:  # left turn
        # unit normal vector to l1, pointing right
        nux = uy / usize
        nuy = -ux / usize
        # second point for the triangle:
        p2x = l1.endx + nux * l1.linewidth / 2
        p2y = l1.endy + nuy * l1.linewidth / 2
        # unit normal vector to l2, pointing right
        nvx = vy / vsize
        nvy = -vx / vsize
        # third point for the triangle:
        p3x = l2.startx + nvx * l2.linewidth / 2
        p3y = l2.starty + nvy * l2.linewidth / 2
        return TRIANGLE(POINT(p1x, p1y), POINT(p2x, p2y), POINT(p3x, p3y))
    else:  # right turn
        # unit normal vector to l1, pointing right
        nux = -uy / usize
        nuy = ux / usize
        # second point for the triangle:
        p2x = l1.endx + nux * l1.linewidth / 2
        p2y = l1.endy + nuy * l1.linewidth / 2
        # unit normal vector to l2, pointing right
        nvx = -vy / vsize
        nvy = vx / vsize
        # third point for the triangle:
        p3x = l2.startx + nvx * l2.linewidth / 2
        p3y = l2.starty + nvy * l2.linewidth / 2
        return TRIANGLE(POINT(p1x, p1y), POINT(p2x, p2y), POINT(p3x, p3y))

    # Return trace as list of PLaSM objects. Line segments with height 0 will become


# rectangles in the XY plane, line segments with nonzero height will become 3D prisms.
def NCLabTurtleTrace(lines, layer=0, dots=True, elev=0):
    out = []
    n = len(lines)
    # List of lines is empty - just return:
    if n == 0:
        return out
    # Now we know that there is at least one line segment:
    for i in range(n):
        l = lines[i]
        # Add rectangle corresponding to the line:
        rect = NCLabTurtleRectangle(l, layer)
        if abs(l.lineheight) < 0.000001:
            if elev < 0.000001:
                out.append(rect)
            else:
                MOVE(rect, elev, Z)  # strictly for visualization purposes
                out.append(rect)  # such trace will not work for grading
        else:
            out.append(PRISM(rect, l.lineheight))
        # If dots == True (we will be adding circles
        # to line end points):
        if dots == True:
            # Add circle to start point, if
            # the previous line does not have 'continued==True'
            # or if angle difference is greater than 45 degrees:
            addcircle = True
            if i == 0:
                addcircle = True
            else:
                lprev = lines[i - 1]
                addcircle = lprev.continued == False
                # also check if angle difference is greater than 45 degrees:
                lcurr = lines[i]
                if abs(lprev.angle - lcurr.angle) >= 45:
                    addcircle = True
            if addcircle:
                radius = 0.5 * l.linewidth + layer
                cir = CIRCLE(radius, 8)
                MOVE(cir, l.startx, l.starty)
                COLOR(cir, l.linecolor)
                if abs(l.lineheight) < 0.000001:
                    out.append(cir)
                else:
                    out.append(PRISM(cir, l.lineheight))
            else:  # we will be adding a wedge to the beginning of current line
                lprev = lines[i - 1]
                if abs(lprev.angle - l.angle) > 0.001:
                    wedge = NCLabTurtleWedge(lprev, l)
                    COLOR(wedge, lprev.linecolor)
                    if abs(lprev.lineheight) < 0.000001:
                        out.append(wedge)
                    else:
                        out.append(PRISM(wedge, lprev.lineheight))
            # Add circle to end point, but only if
            # 'continued==False':
            if l.continued == False:
                radius = 0.5 * l.linewidth + layer
                cir = CIRCLE(radius, 8)
                MOVE(cir, l.endx, l.endy)
                COLOR(cir, l.linecolor)
                if abs(l.lineheight) < 0.000001:
                    out.append(cir)
                else:
                    out.append(PRISM(cir, l.lineheight))
    return out


# Shape of the turtle:
def NCLabTurtleImage(turtle):
    t = []
    t1 = CIRCLE(5, 10)
    rt, gt, bt = turtle.linecolor
    COLOR(t1, [rt, gt, bt])
    SCALE(t1, 0.75, 1)
    t.append(t1)
    t2 = RING(5, 5.5, 10)
    COLOR(t2, BLACK)
    SCALE(t2, 0.75, 1)
    t.append(t2)
    t3 = CIRCLE(1.5, 8)
    MOVE(t3, 0, 6.25)
    COLOR(t3, BLACK)
    t.append(t3)
    t4a = QUAD([1, 5], [4, 5], [6, 3], [3, 3])
    COLOR(t4a, BLACK)
    t.append(t4a)
    t4b = TRIANGLE([4, 3], [6, 3], [6, 1])
    COLOR(t4b, BLACK)
    t.append(t4b)
    t5a = QUAD([-1, 5], [-4, 5], [-6, 3], [-3, 3])
    COLOR(t5a, BLACK)
    t.append(t5a)
    t5b = TRIANGLE([-4, 3], [-6, 3], [-6, 1])
    COLOR(t5b, BLACK)
    t.append(t5b)
    t6 = QUAD([2, -4], [3.25, -3], [4, -5], [3, -6])
    COLOR(t6, BLACK)
    t.append(t6)
    t7 = QUAD([-2, -4], [-3.25, -3], [-4, -5], [-3, -6])
    COLOR(t7, BLACK)
    t.append(t7)
    ROTATE(t, -90)
    ROTATE(t, turtle.turtleangle)
    MOVE(t, turtle.posx, turtle.posy)
    return t


# Goes through the turtle trace and looks
# for a pair of adjacent segments with the
# same angle, width, height and color. If found,
# returns index of the first. If not found,
# returns -1:
def NCLabTurtleFindPair(turtle):
    n = len(turtle.lines)
    if n <= 1:
        return -1
    for i in range(n - 1):
        l1 = turtle.lines[i]
        l2 = turtle.lines[i + 1]
        # End point is start point of next:
        f1 = abs(l2.startx - l1.endx) < 0.000001
        f2 = abs(l2.starty - l1.endy) < 0.000001
        # Angle:
        dx1 = l1.endx - l1.startx
        dy1 = l1.endy - l1.starty
        angle1 = arctan2(dy1, dx1)
        dx2 = l2.endx - l2.startx
        dy2 = l2.endy - l2.starty
        angle2 = arctan2(dy2, dx2)
        f3 = angle1 == angle2
        # Color:
        f4 = True
        for i in range(3):
            if l1.linecolor[i] != l2.linecolor[i]:
                f4 = False
                break
        # Line width:
        f5 = (l1.linewidth - l2.linewidth) < 0.000001
        # Line height:
        f6 = (l1.lineheight - l2.lineheight) < 0.000001
        if f1 and f2 and f3 and f4 and f5 and f6:
            return i
    return -1


# Merges adjacent segments that lie
# on the same line, and have the same
# width, height and color:
def NCLabTurtleCleanTrace(turtle):
    index = NCLabFindPair(turtle)
    while index != -1:
        l1 = turtle.lines[index]
        l2 = turtle.lines[index + 1]
        l1.endx = l2.endx
        l1.endy = l2.endy
        del turtle.lines[index + 1]
        index = NCLabFindPair(turtle)


# Extrusion heights for the turtle trace, the red (sol)
# (correct solution) trace and the turtle itself:
NCLAB_TURTLE_TRACE_H = 0.0005
NCLAB_TURTLE_WALL_H = 0.0002
NCLAB_TURTLE_ERR_H = 0.0006
NCLAB_TURTLE_RED_H = 0.0007
NCLAB_TURTLE_SOL_H = NCLAB_TURTLE_RED_H
NCLAB_TURTLE_IMAGE_H = 0.0009
NCLAB_TURTLE_EPS = 0.0001


def NCLabTurtleShowTrace(turtle, layer=0, dots=True, elev=0):
    image = NCLabTurtleImage(turtle)
    canvas = NCLabTurtleCanvas(turtle)
    trace = NCLabTurtleTrace(turtle.lines, layer, dots, elev)
    # Make the image and canvas 3D:
    image = PRISM(image, NCLAB_TURTLE_IMAGE_H)
    canvas = PRISM(canvas, NCLAB_TURTLE_TRACE_H)
    if turtle.isvisible:
        if not turtle.heightused:
            SHOW(image, canvas, trace)
        else:
            SHOW(canvas, trace)
    else:
        SHOW(canvas, trace)


# Return xmin, xmax, ymin, ymax:
def NCLabTurtleExtremes(lines):
    n = len(lines)
    if n == 0:
        return 0, 0, 0, 0
    # Initialize extremes:
    l = lines[0]
    minx = l.startx
    maxx = l.startx
    miny = l.starty
    maxy = l.starty
    # Calculate extremes:
    for i in range(n):
        l = lines[i]
        if minx > l.startx:
            minx = l.startx
        if maxx < l.startx:
            maxx = l.startx
        if miny > l.starty:
            miny = l.starty
        if maxy < l.starty:
            maxy = l.starty
        if minx > l.endx:
            minx = l.endx
        if maxx < l.endx:
            maxx = l.endx
        if miny > l.endy:
            miny = l.endy
        if maxy < l.endy:
            maxy = l.endy
    return minx, maxx, miny, maxy


# Return maximum line width:
def NCLabTurtleMaxLineWidth(turtle):
    n = len(turtle.lines)
    if n == 0:
        return 0
    # Initialize maximum:
    maxlw = 0
    # Calculate maximum:
    for i in range(n):
        l = turtle.lines[i]
        if maxlw < l.linewidth:
            maxlw = l.linewidth
    return maxlw


# Transform point (x, y) from original Turtle
# coordinate system to the SVG coordinates:
def NCLabTurtleSVGTrans(x, y, worig, horig, cxorig, cyorig, wincm, hincm, scaling):
    newcx = 0.5 * wincm * 100
    newcy = 0.5 * hincm * 100
    return int(round(newcx + scaling * (x - cxorig))), int(
        round(newcy - scaling * (y - cyorig))
    )


# Return text string that can be saved as an SVG file:
# In this version, the color is black and line width is 1
# because we have a laser cutter in mind. Both can be
# adjusted:
def NCLabTurtleWriteSVG(turtle, wincm, hincm):
    # PREAMBLE:
    out = ""
    out += (
        '<svg width="'
        + str(wincm)
        + 'cm" height="'
        + str(hincm)
        + 'cm" viewBox="0 0 '
        + str(wincm * 100)
        + " "
        + str(hincm * 100)
        + '"\n'
    )
    out += 'xmlns="http://www.w3.org/2000/svg" version="1.1">\n'
    out += "<desc>Generated by NCLab (http://nclab.com)</desc>\n"
    # PREPARE DATA FOR TRANSFORMATION:
    minx, maxx, miny, maxy = NCLabTurtleExtremes(turtle.lines)
    maxlinewidth = NCLabTurtleMaxLineWidth(turtle)
    worig = maxx - minx
    horig = maxy - miny
    cxorig = 0.5 * (minx + maxx)
    cyorig = 0.5 * (miny + maxy)
    # CALCULATE SCALING COEFF:
    if maxx - minx < 0.0001 and maxy - miny < 0.0001:
        scaling = 1.0
    elif maxx - minx < 0.0001:
        scaling = hincm * 100 / (maxy - miny + maxlinewidth)
    elif maxy - miny < 0.0001:
        scaling = wincm * 100 / (maxx - minx + maxlinewidth)
    else:
        sx = wincm * 100 / (maxx - minx + maxlinewidth)
        sy = hincm * 100 / (maxy - miny + maxlinewidth)
        scaling = min(sx, sy)
    # WRITE TURTLE TRACE:
    n = len(turtle.lines)
    # List of lines is empty - just return:
    if n == 0:
        # Close the SVG file:
        out += "</svg>\n"
        return out
    # Now we know that there is at least one line segment.
    counter = 0
    while counter != n:
        l = turtle.lines[counter]
        lw = int(round(l.linewidth * scaling))
        if lw <= 0:
            lw = 1
        # Open the polyline:
        cr = int(round(l.linecolor[0] * 255))
        cg = int(round(l.linecolor[1] * 255))
        cb = int(round(l.linecolor[2] * 255))
        newstartx, newstarty = NCLabTurtleSVGTrans(
            l.startx, l.starty, worig, horig, cxorig, cyorig, wincm, hincm, scaling
        )
        newendx, newendy = NCLabTurtleSVGTrans(
            l.endx, l.endy, worig, horig, cxorig, cyorig, wincm, hincm, scaling
        )
        # Add a circle to the beginning:
        out += (
            '<circle cx="'
            + str(newstartx)
            + '" cy="'
            + str(newstarty)
            + '" r="'
            + str(0.5 * lw)
            + '" fill="rgb('
            + str(cr)
            + ","
            + str(cg)
            + ","
            + str(cb)
            + ')"/>\n'
        )
        # Start polyline:
        out += (
            '<polyline stroke-linejoin="round" fill="none" stroke="rgb('
            + str(cr)
            + ","
            + str(cg)
            + ","
            + str(cb)
            + ')" stroke-width="'
            + str(lw)
            + '" points="'
        )
        out += (
            str(newstartx)
            + ","
            + str(newstarty)
            + " "
            + str(newendx)
            + ","
            + str(newendy)
        )
        while l.continued:
            out += " "
            counter += 1
            l = turtle.lines[counter]
            newstartx, newstarty = NCLabTurtleSVGTrans(
                l.startx, l.starty, worig, horig, cxorig, cyorig, wincm, hincm, scaling
            )
            newendx, newendy = NCLabTurtleSVGTrans(
                l.endx, l.endy, worig, horig, cxorig, cyorig, wincm, hincm, scaling
            )
            out += (
                str(newstartx)
                + ","
                + str(newstarty)
                + " "
                + str(newendx)
                + ","
                + str(newendy)
            )
        # Close the polyline:
        out += '" />\n'
        # Add a circle to the end:
        out += (
            '<circle cx="'
            + str(newendx)
            + '" cy="'
            + str(newendy)
            + '" r="'
            + str(0.5 * lw)
            + '" fill="rgb('
            + str(cr)
            + ","
            + str(cg)
            + ","
            + str(cb)
            + ')"/>\n'
        )
        # update counter:
        counter += 1
    # Close the SVG file:
    out += "</svg>\n"
    return out


# Global variable for Turtle walls:
NCLAB_TURTLE_WALLS = []


# Distance of two points:
def distance(ax, ay, bx, by):
    dx = bx - ax
    dy = by - ay
    return sqrt(dx**2 + dy**2)
