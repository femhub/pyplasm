"""
NCLAB TURTLE 3D - UTILITIES
"""

from numpy import pi, cos, sin

from ..utils.constants import X, Y, Z
from ..geometry.box import BOX
from ..geometry.circle import CIRCLE
from ..geometry.quad import QUAD
from ..geometry.triangle import TRIANGLE
from ..geometry.sphere import SPHERE
from ..operations.color import COLOR
from ..operations.move import MOVE
from ..operations.rotate import ROTATE
from ..operations.scale import SCALE
from ..geometry.prism import PRISM
from ..operations.copy_objects import COPY
from ..operations.show import SHOW
from ..operations.erase import ERASE
from ..operations.union import UNION
from ..geometry.chull import CHULL
from ..operations.split import SPLIT
from ..colors.color_constants import BLACK


# The convex hull of these points will form the wire:
def NCLabTurtleBoxPoints3D(l, subdiv, layer=0):
    sx = l.startx
    sy = l.starty
    sz = l.startz
    u1 = l.u1
    u2 = l.u2
    u3 = l.u3
    v1 = l.v1
    v2 = l.v2
    v3 = l.v3
    w1 = l.w1
    w2 = l.w2
    w3 = l.w3
    width = l.linewidth
    da = 2 * pi / subdiv
    da0 = da / 2
    points = []
    for i in range(subdiv):
        p = [
            sx
            - layer * u1
            - (width / 2 + layer) * v1 * cos(da0 + i * da)
            - (width / 2 + layer) * w1 * sin(da0 + i * da),
            sy
            - layer * u2
            - (width / 2 + layer) * v2 * cos(da0 + i * da)
            - (width / 2 + layer) * w2 * sin(da0 + i * da),
            sz
            - layer * u3
            - (width / 2 + layer) * v3 * cos(da0 + i * da)
            - (width / 2 + layer) * w3 * sin(da0 + i * da),
        ]
        points.append(p)
    for i in range(subdiv):
        p = [
            sx
            + (l.dist + 2 * layer) * u1
            - (width / 2 + layer) * v1 * cos(da0 + i * da)
            - (width / 2 + layer) * w1 * sin(da0 + i * da),
            sy
            + (l.dist + 2 * layer) * u2
            - (width / 2 + layer) * v2 * cos(da0 + i * da)
            - (width / 2 + layer) * w2 * sin(da0 + i * da),
            sz
            + (l.dist + 2 * layer) * u3
            - (width / 2 + layer) * v3 * cos(da0 + i * da)
            - (width / 2 + layer) * w3 * sin(da0 + i * da),
        ]
        points.append(p)
    return points


# 3D Rectangle given via start point, distance,
# angle, width and color):
def NCLabTurtleBox3D(l, subdiv, layer):
    points = NCLabTurtleBoxPoints3D(l, subdiv, layer)
    box1 = CHULL(*points)
    COLOR(box1, l.linecolor)
    return box1


# Dots to set area size:
def NCLabTurtleCanvas3D(turtle):
    r = turtle.canvassize
    r /= 2
    dot1 = BOX(-0.05, 0.05, -0.05, 0.05, -0.05, 0.05)
    MOVE(dot1, r, 0, -r)
    dot2 = COPY(dot1)
    ROTATE(dot2, 90, Z)
    dot3 = COPY(dot2)
    ROTATE(dot3, 90, Z)
    dot4 = COPY(dot3)
    ROTATE(dot4, 90, Z)
    return [dot1, dot2, dot3, dot4]


# Return trace as list of PLaSM objects:
def NCLabTurtleTrace3D(turtle, layer=0, dots=True):
    out = []
    n = len(turtle.lines)
    # List of lines is empty - just return:
    if n == 0:
        return out
    # There is at least one line segment:
    for i in range(n):
        l = turtle.lines[i]
        # Add rectangle corresponding to the line:
        rect = NCLabTurtleBox3D(l, turtle.edgenum, layer)
        out.append(rect)
        # If dots == True, add connector at the end of line
        if dots == True:
            s = SPHERE(turtle.linewidth / 2 + layer, turtle.edgenum)
            ROTATE(s, 90, Y)
            ROTATE(s, 360 / turtle.edgenum / 2, X)
            s1, s2 = SPLIT(s, 0, X)
            COLOR(s1, l.linecolor)
            COLOR(s2, l.linecolor)
            MOVE(s1, l.startx, l.starty, l.startz)
            MOVE(
                s2,
                l.startx + l.dist * l.u1,
                l.starty + l.dist * l.u2,
                l.startz + l.dist * l.u3,
            )
            out.append(s1)
            out.append(s2)
    return out


# Shape of the turtle:
def NCLabTurtleImage3D(turtle):
    t = []
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
    t8 = PRISM(t, 1)
    t9 = SPHERE(5.5, 10)
    ROTATE(t9, 90, X)
    ERASE(t9, -10, 0, Z)
    SCALE(t9, 0.75, X)
    SCALE(t9, 0.75, Z)
    MOVE(t9, -0.01, Z)
    rt, gt, bt = turtle.linecolor
    COLOR(t9, [rt, gt, bt])
    t10 = UNION(t8, t9)
    ROTATE(t10, -90, Z)
    a1, a2, a3 = turtle.getangles()
    # print("Angles:", a1, a2, a3)
    ROTATE(t10, a3, X)
    ROTATE(t10, -a2, Y)
    ROTATE(t10, a1, Z)
    MOVE(t10, turtle.posx, turtle.posy, turtle.posz)
    return t10


def NCLabTurtleShow3D(turtle, layer=0):
    canvas = NCLabTurtleCanvas3D(turtle)
    trace = NCLabTurtleTrace3D(turtle, layer)
    image = NCLabTurtleImage3D(turtle)
    if turtle.isvisible:
        SHOW(image, canvas, trace)
    else:
        SHOW(canvas, trace)
