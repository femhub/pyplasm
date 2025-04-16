"""
NCLAB TURTLE 2D - CLASSES
"""
from numpy import cos, sin, pi, sqrt, arctan2
from random import random, randint

from nclab.tools import ExceptionWT
from ..geometry.point import POINT
from ..operations.color import COLOR
from ..operations.show import SHOW
from ..colors.color_constants import BLUE, ANY
from ..operations.revolve import REVOLVE
from ..geometry.spiral import SPIRAL
from ..geometry.surfaces.rotational_surface import ROSURF
from ..geometry.solids.rotational_solid import ROSOL
from ..turtle.turtle_2d_utils import (
    NCLabTurtleExtremes,
    NCLabTurtleShowTrace,
    NCLabTurtleTrace,
    NCLAB_TURTLE_TRACE_H,
    NCLAB_TURTLE_WALL_H,
    NCLAB_TURTLE_WALLS,
    distance,
)
from ...fenvs import PI, SIN, COS, nclabinst


class NCLabTurtleLine:
    def __init__(self, sx, sy, ex, ey, w, h, c, angle, continued=False):
        self.startx = sx
        self.starty = sy
        self.endx = ex
        self.endy = ey
        self.linewidth = w
        self.lineheight = h
        self.linecolor = c
        self.angle = angle
        self.continued = continued


# Class Turtle:
class NCLabTurtle:
    _instances = []

    def __init__(self, px=0, py=0, user_created=True):
        # Safe a reference to the newly created instance for
        # autograding. There are turtle instances created internally
        # so we need an extra information held in user_created
        # whether this instance should be included into set
        # of turtles created by user.
        if user_created:
            self._instances.append(self)

        self.posx = px
        self.posy = py
        self.turtleangle = 0
        self.linecolor = [0, 0, 255]
        self.draw = True
        self.linewidth = 1
        self.lineheight = 0
        self.canvassize = 100
        self.lines = []
        self.walls = []

        # Try to import walls from NCLAB_TURTLE_WALLS:
        self.importwalls()  # lines, made by another Turtle, to serve as obstacles
        self.wallminx = 0  # Extremes for the walls
        self.wallmaxx = 0
        self.wallminy = 0
        self.wallmaxy = 0
        # Calculate the extremes:
        (
            self.wallminx,
            self.wallmaxx,
            self.wallminy,
            self.wallmaxy,
        ) = NCLabTurtleExtremes(self.walls)

        self.tracelength = 0  # measures how many steps the Turtle
        # made during her lifetime, but only when she was drawing
        self.heightused = False  # If any line height is set
        # to nonzero, this will be True
        self.isvisible = True
        self.isspiral = False
        self.isrosol = False
        self.isrosurf = False
        self.isroshell = False
        self.geom = None
        # These commands can be called only once:
        self.rosolcalled = False
        self.rosurfcalled = False
        self.roshellcalled = False
        self.spiralcalled = False
        self.revolvecalled = False
        self.extrudecalled = False
        self.showcalled = False
        self.programended = False

    # Detects whether the Turtle stands on a wall or on its own trace of the given color
    # (for line-following purposes). Returns either True or False:
    def oncolor(self, col=ANY):
        ax = self.posx
        ay = self.posy
        # Is it one of the wall end points?
        for l in self.walls:
            sx = l.startx
            sy = l.starty
            ex = l.endx
            ey = l.endy
            if (
                distance(ax, ay, sx, sy) < 0.5 * l.linewidth
                or distance(ax, ay, ex, ey) < 0.5 * l.linewidth
            ):
                if col == ANY:
                    return True
                # if [round(l.linecolor[0]*255), round(l.linecolor[1]*255), round(l.linecolor[2]*255)] == col:
                if l.linecolor == col:
                    return True
        # Is it one of the line end points?
        # WARNING - when she has the pen down, her own trace will always be detected!
        # This makes sense only when she is not drawing and just walking.
        for l in self.lines:
            sx = l.startx
            sy = l.starty
            ex = l.endx
            ey = l.endy
            if (
                distance(ax, ay, sx, sy) < 0.5 * l.linewidth
                or distance(ax, ay, ex, ey) < 0.5 * l.linewidth
            ):
                if col == ANY:
                    return True
                # if [round(l.linecolor[0]*255), round(l.linecolor[1]*255), round(l.linecolor[2]*255)] == col:
                if l.linecolor == col:
                    return True
        # Is it inside of a wall?
        for l in self.walls:
            sx = l.startx
            sy = l.starty
            ex = l.endx
            ey = l.endy
            ux = ex - sx
            uy = ey - sy
            # Length of the line (squared):
            ulen2 = ux**2 + uy**2
            if ulen2 > 0.00000001:
                # Calculate parameter:
                z = (ax * ux + ay * uy - sx * ux - sy * uy) / ulen2
                # Is z between 0 and 1?
                if 0 <= z and z <= 1:
                    # This is the projection to the line:
                    px = sx + z * ux
                    py = sy + z * uy
                    # Is the Turtle less than 0.5*linewidth from it?
                    if distance(ax, ay, px, py) <= 0.5 * l.linewidth:
                        if col == ANY:
                            return True
                        # if [round(l.linecolor[0]*255), round(l.linecolor[1]*255), round(l.linecolor[2]*255)] == col:
                        if l.linecolor == col:
                            return True
        # Is it inside of a line?
        for l in self.lines:
            sx = l.startx
            sy = l.starty
            ex = l.endx
            ey = l.endy
            ux = ex - sx
            uy = ey - sy
            # Length of the line (squared):
            ulen2 = ux**2 + uy**2
            if ulen2 > 0.00000001:
                # Calculate parameter:
                z = (ax * ux + ay * uy - sx * ux - sy * uy) / ulen2
                # Is z between 0 and 1?
                if 0 <= z and z <= 1:
                    # This is the projection to the line:
                    px = sx + z * ux
                    py = sy + z * uy
                    # Is the Turtle less than 0.5*linewidth from it?
                    if distance(ax, ay, px, py) <= 0.5 * l.linewidth:
                        if col == ANY:
                            return True
                        # if [round(l.linecolor[0]*255), round(l.linecolor[1]*255), round(l.linecolor[2]*255)] == col:
                        if l.linecolor == col:
                            return True
        # Nothing found:
        return False

    # Detects whether the Turtle stands on a wall or its own trace.
    # Returns the color of the wall or False.
    def colorprobe(self):
        ax = self.posx
        ay = self.posy
        # Is it one of the wall end points?
        for l in self.walls:
            sx = l.startx
            sy = l.starty
            ex = l.endx
            ey = l.endy
            if (
                distance(ax, ay, sx, sy) < 0.5 * l.linewidth
                or distance(ax, ay, ex, ey) < 0.5 * l.linewidth
            ):
                # return [round(l.linecolor[0]*255), round(l.linecolor[1]*255), round(l.linecolor[2]*255)]
                return l.linecolor[:]
        # Is it one of the line end points?
        for l in self.lines:
            sx = l.startx
            sy = l.starty
            ex = l.endx
            ey = l.endy
            if (
                distance(ax, ay, sx, sy) < 0.5 * l.linewidth
                or distance(ax, ay, ex, ey) < 0.5 * l.linewidth
            ):
                # return [round(l.linecolor[0]*255), round(l.linecolor[1]*255), round(l.linecolor[2]*255)]
                return l.linecolor[:]
        # Is it inside of a wall?
        for l in self.walls:
            sx = l.startx
            sy = l.starty
            ex = l.endx
            ey = l.endy
            ux = ex - sx
            uy = ey - sy
            # Length of the line (squared):
            ulen2 = ux**2 + uy**2
            if ulen2 > 0.00000001:
                # Calculate parameter:
                z = (ax * ux + ay * uy - sx * ux - sy * uy) / ulen2
                # Is z between 0 and 1?
                if 0 <= z and z <= 1:
                    # This is the projection to the line:
                    px = sx + z * ux
                    py = sy + z * uy
                    # Is the Turtle less than 0.5*linewidth from it?
                    if distance(ax, ay, px, py) <= 0.5 * l.linewidth:
                        # return [round(l.linecolor[0]*255), round(l.linecolor[1]*255), round(l.linecolor[2]*255)]
                        return l.linecolor[:]
        # Is it inside of a line?
        for l in self.lines:
            sx = l.startx
            sy = l.starty
            ex = l.endx
            ey = l.endy
            ux = ex - sx
            uy = ey - sy
            # Length of the line (squared):
            ulen2 = ux**2 + uy**2
            if ulen2 > 0.00000001:
                # Calculate parameter:
                z = (ax * ux + ay * uy - sx * ux - sy * uy) / ulen2
                # Is z between 0 and 1?
                if 0 <= z and z <= 1:
                    # This is the projection to the line:
                    px = sx + z * ux
                    py = sy + z * uy
                    # Is the Turtle less than 0.5*linewidth from it?
                    if distance(ax, ay, px, py) <= 0.5 * l.linewidth:
                        # return [round(l.linecolor[0]*255), round(l.linecolor[1]*255), round(l.linecolor[2]*255)]
                        return l.linecolor[:]
        # Nothing found:
        return None

    # Perform intersection of the laser beam with all walls, one by one, and all line segments
    # drawn by the Turtle. The valid ones are put into a list. Select closest point to the Turtle,
    # and return the distance. Or return None if there is no intersection
    def lidar(self, wallcolor=ANY, raycolor=None, raywidth=1):
        # Sanity checks:
        if wallcolor != ANY:
            if not isinstance(wallcolor, list):
                raise ExceptionWT(
                    "In lidar(wallcolor=ANY, raycolor=None, raywidth=1): Invalid wall color."
                )
            if len(wallcolor) != 3:
                raise ExceptionWT(
                    "In lidar(wallcolor=ANY, raycolor=None, raywidth=1): Invalid wall color."
                )
            if (
                (not isinstance(wallcolor[0], int))
                or (not isinstance(wallcolor[1], int))
                or (not isinstance(wallcolor[2], int))
            ):
                raise ExceptionWT(
                    "In lidar(wallcolor=ANY, raycolor=None, raywidth=1): Invalid wall color."
                )
            if wallcolor[0] < 0 or wallcolor[1] < 0 or wallcolor[2] < 0:
                raise ExceptionWT(
                    "In lidar(wallcolor=ANY, raycolor=None, raywidth=1): Invalid wall color."
                )
        if raycolor != None:
            if not isinstance(raycolor, list):
                raise ExceptionWT(
                    "In lidar(wallcolor=ANY, raycolor=None, raywidth=1): Invalid ray color."
                )
            if len(raycolor) != 3:
                raise ExceptionWT(
                    "In lidar(wallcolor=ANY, raycolor=None, raywidth=1): Invalid ray color."
                )
            if (
                (not isinstance(raycolor[0], int))
                or (not isinstance(raycolor[1], int))
                or (not isinstance(raycolor[2], int))
            ):
                raise ExceptionWT(
                    "In lidar(wallcolor=ANY, raycolor=None, raywidth=1): Invalid ray color."
                )
            if raycolor[0] < 0 or raycolor[1] < 0 or raycolor[2] < 0:
                raise ExceptionWT(
                    "In lidar(wallcolor=ANY, raycolor=None, raywidth=1): Invalid ray color."
                )
        if not isinstance(raywidth, int) and not isinstance(raywidth, float):
            raise ExceptionWT(
                "In lidar(wallcolor=ANY, raycolor=None, raywidth=1): Ray width must be a number."
            )
        if raywidth <= 0:
            raise ExceptionWT(
                "In lidar(wallcolor=ANY, raycolor=None, raywidth=1): Ray width must be positive."
            )

        found = False
        ax = self.posx
        ay = self.posy
        mindist = 100000.0
        # Check all walls:
        for l in self.walls:
            # if col == ANY or [round(l.linecolor[0]*255), round(l.linecolor[1]*255), round(l.linecolor[2]*255)] == col:
            if wallcolor == ANY or l.linecolor == wallcolor:
                p = self.intersect(l.startx, l.starty, l.endx, l.endy)
                if p != None:  # Point valid, calculate distance
                    d = distance(ax, ay, p[0], p[1])
                    if d < mindist:
                        mindist = d
                        found = True
        # Check all lines:
        for l in self.lines:
            # if col == ANY or [round(l.linecolor[0]*255), round(l.linecolor[1]*255), round(l.linecolor[2]*255)] == col:
            if wallcolor == ANY or l.linecolor == wallcolor:
                p = self.intersect(l.startx, l.starty, l.endx, l.endy)
                if p != None:  # Point valid, calculate distance
                    d = distance(ax, ay, p[0], p[1])
                    if d < mindist:
                        mindist = d
                        found = True
        if found:
            d = round(mindist, 4)
            if raycolor != None:  # Draw the ray
                width0 = self.linewidth  # Store original line width
                self.width(raywidth)  # Set ray width
                col0 = self.linecolor[:]  # Store original line color
                self.color(raycolor)  # Set ray color
                draw0 = self.draw  # Store original draw flag
                self.draw = True
                self.go(d)
                self.back(d)
                self.draw = draw0  # Restore original draw flag
                self.linewidth = width0  # Restore original line width
                self.color(col0)  # Restore original color
            return d
        else:
            return None

    # Calculate intersection of line (ax, ay) <-> (bx, by) with line (cx, cy) <-> (dx, dy)
    # Here (ax, ay) is the Turtle, (bx, by) is the point at the end of maxlaserline,
    # (cx, cy) <-> (dx, dy) is a segment of the wall:
    def intersect(self, cx, cy, dx, dy, eps=0.001):
        ax = self.posx
        ay = self.posy
        bx, by = self.maxlaserline()
        # First, are C, D on different sides of AB?
        ux = bx - ax
        uy = by - ay
        vx = cx - ax
        vy = cy - ay
        vect1 = ux * vy - uy * vx
        if abs(vect1) < eps:  # C lies on AB
            return None
        vx = dx - ax
        vy = dy - ay
        vect2 = ux * vy - uy * vx
        if abs(vect2) < eps:  # D lies on AB
            return None
        if vect1 * vect2 > 0:  # C, D are on the same side AB
            return None
        # Second, are A, B on different sides of CD?
        ux = dx - cx
        uy = dy - cy
        vx = bx - cx
        vy = by - cy
        vect1 = ux * vy - uy * vx
        if abs(vect1) < eps:  # B lies on CD
            return None
        vx = ax - cx
        vy = ay - cy
        vect2 = ux * vy - uy * vx
        if abs(vect2) < eps:  # A lies on CD
            return None
        if vect1 * vect2 > 0:  # A, B are on the same side of CD
            return None

        # Woo-hoo! The two segments intersect:
        def line(p1, p2):
            A = p1[1] - p2[1]
            B = p2[0] - p1[0]
            C = p1[0] * p2[1] - p2[0] * p1[1]
            return A, B, -C

        def intersection(L1, L2):
            D = L1[0] * L2[1] - L1[1] * L2[0]
            Dx = L1[2] * L2[1] - L1[1] * L2[2]
            Dy = L1[0] * L2[2] - L1[2] * L2[0]
            if D != 0:
                x = Dx / D
                y = Dy / D
                return x, y
            else:
                return None

        L1 = line([ax, ay], [bx, by])
        L2 = line([cx, cy], [dx, dy])
        result = intersection(L1, L2)
        return result

    # Go through all vertices in the walls and lines, and calculate the maximum
    # distance from the Turtle. This is the maxlaserradius.
    def maxlaserradius(self):
        radius = 0
        # Check all walls:
        for l in self.walls:
            r = distance(l.startx, l.starty, self.posx, self.posy)
            if r > radius:
                radius = r
            if l.continued == False:
                r = distance(l.endx, l.endy, self.posx, self.posy)
                if r > radius:
                    radius = r
        # Check all lines:
        for l in self.lines:
            r = distance(l.startx, l.starty, self.posx, self.posy)
            if r > radius:
                radius = r
            if l.continued == False:
                r = distance(l.endx, l.endy, self.posx, self.posy)
                if r > radius:
                    radius = r
        return radius

    # This is the end point of the laser line that will be used to intersect with walls:
    def maxlaserline(self):
        r = self.maxlaserradius()
        r += 10  # make it a bit longer
        endx = self.posx + r * COS(self.turtleangle * PI / 180)
        endy = self.posy + r * SIN(self.turtleangle * PI / 180)
        return endx, endy

    # Import walls from NCLAB_TURTLE_WALLS:
    def importwalls(self):
        self.walls = []
        for line in NCLAB_TURTLE_WALLS:
            self.walls.append(line)

    # Export lines into NCLAB_TURTLE_WALLS:
    def exportwalls(self):
        for line in self.lines:
            NCLAB_TURTLE_WALLS.append(line)

    # Draw (xmin, xmax) x (ymin, ymax) rectangle:
    def rectangle(self, xmin, xmax, ymin, ymax, col=ANY):
        if self.extrudecalled:
            raise ExceptionWT(
                "In rectangle(xmin, xmax, ymin, ymax, col = ANY): Once extrude() is called, you can't keep drawing."
            )
        # Remember color, position, angle, penup:
        if col != ANY:
            savecol = self.linecolor
            self.linecolor = col
        savex = self.posx
        savey = self.posy
        saveangle = self.turtleangle
        savedraw = self.draw
        # Draw:
        self.pu()
        self.goto(xmin, ymin)
        self.angle(0)
        self.pd()
        dx = xmax - xmin
        dy = ymax - ymin
        for i in range(2):
            self.go(dx)
            self.left(90)
            self.go(dy)
            self.left(90)
        # Restore color, position, angle, penup:
        if col != ANY:
            self.linecolor = savecol
        self.pu()
        self.goto(savex, savey)
        self.angle(saveangle)
        self.draw = savedraw

    # Draw a line from (ax, ay) to (bx, by):
    def line(self, ax, ay, bx, by, col=BLUE):
        if self.extrudecalled:
            raise ExceptionWT(
                "In line(ax, ay, bx, by, col = BLUE): Once extrude() is called, you can't keep drawing."
            )
        # Remember color, position, angle, penup:
        if col != BLUE:
            savecol = self.linecolor
            self.linecolor = col
        savex = self.posx
        savey = self.posy
        saveangle = self.turtleangle
        savedraw = self.draw
        # Draw:
        self.pu()
        self.goto(ax, ay)
        self.pd()
        self.goto(bx, by)
        # Restore color, position, angle, penup:
        if col != BLUE:
            self.linecolor = savecol
        self.pu()
        self.goto(savex, savey)
        self.angle(saveangle)
        self.draw = savedraw

        # Draw a polyline, here L is a list of points:

    def polyline(self, L, col=BLUE):
        if self.extrudecalled:
            raise ExceptionWT(
                "In polyline(L, col = BLUE): Once extrude() is called, you can't keep drawing."
            )
        # Remember color, position, angle, penup:
        if col != BLUE:
            savecol = self.linecolor
            self.linecolor = col
        savex = self.posx
        savey = self.posy
        saveangle = self.turtleangle
        savedraw = self.draw
        # Draw:
        self.pu()
        p = L[0]
        self.goto(p[0], p[1])
        self.pd()
        del L[0]
        for p in L:
            self.goto(p[0], p[1])
        # Restore color, position, angle, penup:
        if col != BLUE:
            self.linecolor = savecol
        self.pu()
        self.goto(savex, savey)
        self.angle(saveangle)
        self.draw = savedraw

        # Draw a series of dots, here L is a list of points:

    def polydots(self, L, col=BLUE):
        # Remember color, position, angle, penup:
        if col != BLUE:
            savecol = self.linecolor
            self.linecolor = col
        savex = self.posx
        savey = self.posy
        saveangle = self.turtleangle
        savedraw = self.draw
        # Draw:
        p = L[0]
        self.pu()
        self.goto(p[0], p[1])
        self.pd()
        self.angle(0)
        self.go(0.1)
        del L[0]
        for p in L:
            self.pu()
            self.goto(p[0], p[1])
            self.pd()
            self.angle(0)
            self.go(0.1)
        # Restore color, position, angle, penup:
        if col != BLUE:
            self.linecolor = savecol
        self.pu()
        self.goto(savex, savey)
        self.angle(saveangle)
        self.draw = savedraw

    @staticmethod
    def get_user_instances():
        """
        Return instances of all NCLabTurtle objects created
        in this interpreter session
        """
        return NCLabTurtle._instances

    def angle(self, a):
        # Sanity checks:
        if not isinstance(a, int) and not isinstance(a, float):
            raise ExceptionWT("In angle(a): Angle a must be a number.")
        # Body of function:
        if self.extrudecalled:
            raise ExceptionWT(
                "In angle(a): Once extrude() is called, you can't keep drawing."
            )
        self.turtleangle = a

    # Spanish:
    def angulo(self, a):
        self.angle(a)

    def color(self, col):
        # Sanity checks:
        if not isinstance(col, list):
            raise ExceptionWT("In color(c): Invalid color c.")
        if len(col) != 3:
            raise ExceptionWT("In color(c): Invalid color c.")
        if (
            (not isinstance(col[0], int))
            or (not isinstance(col[1], int))
            or (not isinstance(col[2], int))
        ):
            raise ExceptionWT("In color(c): Invalid color c.")
        if col[0] < 0 or col[1] < 0 or col[2] < 0:
            raise ExceptionWT("In color(c): Invalid color c.")
        # Body of function:
        if self.extrudecalled:
            raise ExceptionWT(
                "In color(c): Once extrude() is called, you can't keep drawing."
            )
        if not isinstance(col, list) and not isinstance(col, tuple):
            raise ExceptionWT(
                "In color(c): Attempt to set invalid color. Must be a list or a tuple."
            )
        if len(col) != 3:
            raise ExceptionWT(
                "In color(c): Attempt to set invalid color. Have you used three integers between 0 and 255?"
            )
        for i in range(3):
            if col[i] < 0 or col[i] > 255:
                raise ExceptionWT(
                    "In color(c): Attempt to set invalid color. Have you used three integers between 0 and 255?"
                )
        self.linecolor = col[:]

    def width(self, w):
        # Sanity checks:
        if not isinstance(w, int) and not isinstance(w, float):
            raise ExceptionWT("In width(w): Line width w must be a number.")
        if w <= 0:
            raise ExceptionWT("In width(w): Line width w must be positive.")
        # Body of function:
        if self.extrudecalled:
            raise ExceptionWT(
                "In width(w): Once extrude() is called, you can't keep drawing."
            )
        if w < 0.1:
            raise ExceptionWT("In width(w): Line width must be between 0.1 and 10.0.")
        if w > 10.0:
            raise ExceptionWT("In width(w): Line width must be between 0.1 and 10.0.")
        self.linewidth = w

    # Spanish:
    def ancho(self, w):
        self.width(w)

    def height(self, h):
        # Sanity checks:
        if not isinstance(h, int) and not isinstance(h, float):
            raise ExceptionWT("In height(h): Line height must be a number.")
        if h <= 0:
            raise ExceptionWT("In height(h): Line height h must be positive.")
        # Body of function
        if self.extrudecalled:
            raise ExceptionWT(
                "In height(h): Once extrude() is called, you can't keep drawing."
            )
        self.lineheight = h
        self.heightused = True

    # Spanish:
    def altura(self, w):
        self.height(w)

    def penup(self):
        if self.extrudecalled:
            raise ExceptionWT(
                "In penup(): Once extrude() is called, you can't keep drawing."
            )
        self.draw = False

    def pu(self):
        if self.extrudecalled:
            raise ExceptionWT(
                "In pu(): Once extrude() is called, you can't keep drawing."
            )
        self.draw = False

    # Spanish:
    def levantarpluma(self):
        self.penup()

    def lp(self):
        self.penup()

    def pendown(self):
        if self.extrudecalled:
            raise ExceptionWT(
                "In pendown(): Once extrude() is called, you can't keep drawing."
            )
        self.draw = True

    def pd(self):
        if self.extrudecalled:
            raise ExceptionWT(
                "In pd(): Once extrude() is called, you can't keep drawing."
            )
        self.draw = True

    # Spanish:
    def bajarpluma(self):
        self.pendown()

    def bp(self):
        self.pendown()

    def isdown(self):
        return self.draw

    def up(self):
        raise ExceptionWT(
            "Command up() is reserved for spatial drawing with NCLabTurtle3D. Please use penup() or pu()."
        )

    def down(self):
        raise ExceptionWT(
            "Command down() is reserved for spatial drawing with NCLabTurtle3D. Please use pendown() or pd()."
        )

    def snapshot(self):
        return (
            int(self.tracelength + 0.5),
            int(self.turtleangle + 0.5),
            int(self.linewidth + 0.5),
            self.linecolor,
            self.draw,
        )

    # Every new line will get continued = False by default. Then we look at the
    # last one before it. If its ending position is the same as the starting
    # position of the new line, and if the width / height / color match, we
    # will change its 'continued' flag to True:
    def go(self, dist):
        # Sanity checks:
        if not isinstance(dist, int) and not isinstance(dist, float):
            raise ExceptionWT("In go(d): Distance d must be a number.")
        if abs(dist) < 0.00000001:  # if turtle has not moved, just return
            return
        if dist < 0:
            raise ExceptionWT("In go(d): Distance d must be positive.")
        # Body of function:
        if self.extrudecalled:
            raise ExceptionWT(
                "In go(d): Once extrude() is called, you can't keep drawing."
            )
        if self.draw:
            self.tracelength += dist
        newx = self.posx + dist * cos(self.turtleangle * pi / 180)
        newy = self.posy + dist * sin(self.turtleangle * pi / 180)
        if self.draw == True:
            # Is it a continuation (posx, posy = last point, same width/height/color) ?
            if len(self.lines) != 0:
                lastline = self.lines[-1]
                gap = distance(self.posx, self.posy, lastline.endx, lastline.endy)
                if gap < 0.0001:  # line uninterrupted
                    if lastline.linecolor == self.linecolor:
                        if abs(lastline.linewidth - self.linewidth) < 0.0001:
                            if abs(lastline.lineheight - self.lineheight) < 0.0001:
                                lastline.continued = True

            # Create and append the new line:
            continued = False
            newline = NCLabTurtleLine(
                self.posx,
                self.posy,
                newx,
                newy,
                self.linewidth,
                self.lineheight,
                self.linecolor,
                self.turtleangle,
                continued,
            )
            self.lines.append(newline)
        self.posx = newx
        self.posy = newy

    # Spanish:
    def avanzar(self, dist):
        self.go(dist)

    def printlines(self):
        for line in self.lines:
            print("---")
            print("Start:", line.startx, line.starty)
            print("End:", line.endx, line.endy)
            print(
                "Width:",
                line.linewidth,
                "Height:",
                line.lineheight,
                "Color:",
                line.linecolor,
            )
            print("Angle:", line.angle, "Continued:", line.continued)

    def printwalls(self):
        for line in self.walls:
            print("---")
            print("Start:", line.startx, line.starty)
            print("End:", line.endx, line.endy)
            print(
                "Width:",
                line.linewidth,
                "Height:",
                line.lineheight,
                "Color:",
                line.linecolor,
            )
            print("Angle:", line.angle, "Continued:", line.continued)

    def forward(self, dist):
        self.go(dist)

    def fd(self, dist):
        self.go(dist)

    def left(self, da):
        # Sanity checks:
        if not isinstance(da, int) and not isinstance(da, float):
            raise ExceptionWT("In left(a): Angle a must be a number.")
        # Body of function:
        if self.extrudecalled:
            raise ExceptionWT(
                "In left(a): Once extrude() is called, you can't keep drawing."
            )
        self.turtleangle += da

    # Spanish:
    def izquierda(self, da):
        self.left(da)

    def lt(self, da):
        self.left(da)

    def right(self, da):
        # Sanity checks:
        if not isinstance(da, int) and not isinstance(da, float):
            raise ExceptionWT("In right(a): Angle a must be a number.")
        # Body of function:
        if self.extrudecalled:
            raise ExceptionWT(
                "In right(a): Once extrude() is called, you can't keep drawing."
            )
        self.turtleangle -= da

    # Spanish:
    def derecha(self, da):
        self.right(da)

    def rt(self, da):
        self.right(da)

    def back(self, dist):
        # Sanity checks:
        if not isinstance(dist, int) and not isinstance(dist, float):
            raise ExceptionWT("In back(d): Distance d must be a number.")
        if abs(dist) < 0.00000001:  # if turtle has not moved, just return
            return
        if dist < 0:
            raise ExceptionWT("In back(d): Distance d must be positive.")
        # Body of function:
        if self.extrudecalled:
            raise ExceptionWT(
                "In back(d): Once extrude() is called, you can't keep drawing."
            )
        draw0 = self.draw  # remember the flag
        self.draw = False
        self.left(180)
        self.go(dist)
        self.right(180)
        self.draw = draw0  # restore the original flag

    # Spanish:
    def regresar(self, dist):
        self.back(dist)

    def backward(self, dist):
        self.back(dist)

    def bk(self, dist):
        self.back(dist)

    def goto(self, newx, newy):
        # Sanity checks:
        if not isinstance(newx, int) and not isinstance(newx, float):
            raise ExceptionWT("In goto(x, y): x must be a number.")
        if not isinstance(newy, int) and not isinstance(newy, float):
            raise ExceptionWT("In goto(x, y): y must be a number.")
        # Body of function:
        if self.extrudecalled:
            raise ExceptionWT(
                "In goto(x, y): Once extrude() is called, you can't keep drawing."
            )
        dx = newx - self.posx
        dy = newy - self.posy
        # If Tina has not moved, just return:
        if abs(self.posx - newx) < 0.000001 and abs(self.posy - newy) < 0.000001:
            return
        # Increase step counter:
        dist = sqrt(dx * dx + dy * dy)
        if self.draw:
            self.tracelength += dist
        # Angle:
        self.turtleangle = arctan2(dy, dx) * 180 / pi
        if self.draw == True:
            # Is it a continuation (posx, posy = last point, same width/height/color) ?
            if len(self.lines) != 0:
                lastline = self.lines[-1]
                gap = distance(self.posx, self.posy, lastline.endx, lastline.endy)
                if gap < 0.0001:  # line uninterrupted
                    if lastline.linecolor == self.linecolor:
                        if abs(lastline.linewidth - self.linewidth) < 0.0001:
                            if abs(lastline.lineheight - self.lineheight) < 0.0001:
                                lastline.continued = True
            continued = False  # the last line always has that
            newline = NCLabTurtleLine(
                self.posx,
                self.posy,
                newx,
                newy,
                self.linewidth,
                self.lineheight,
                self.linecolor,
                self.turtleangle,
                continued,
            )
            self.lines.append(newline)
        self.posx = newx
        self.posy = newy

    #####  Random versions of some functions  #####
    def rango(self, x):
        # Sanity checks:
        if not isinstance(x, int) and not isinstance(x, float):
            raise ExceptionWT("In rango(d): Distance d must be a number.")
        if abs(dist) < 0.00000001:  # if turtle has not moved, just return
            return
        if dist < 0:
            raise ExceptionWT("In rango(d): Distance d must be positive.")
        # Body of function:
        if self.extrudecalled:
            raise ExceptionWT(
                "In rango(d): Once extrude() is called, you can't keep drawing."
            )
        self.go(random() * x)

    def ranleft(self, x):
        # Sanity checks:
        if not isinstance(x, int) and not isinstance(x, float):
            raise ExceptionWT("In ranleft(a): Angle a must be a number.")
        # Body of function:
        if self.extrudecalled:
            raise ExceptionWT(
                "In ranleft(a): Once extrude() is called, you can't keep drawing."
            )
        self.left(random() * x)

    def ranright(self, x):
        # Sanity checks:
        if not isinstance(da, int) and not isinstance(da, float):
            raise ExceptionWT("In ranright(a): Angle a must be a number.")
        # Body of function:
        if self.extrudecalled:
            raise ExceptionWT(
                "In ranright(a): Once extrude() is called, you can't keep drawing."
            )
        self.right(random() * x)

    def ranturn(self, x):
        # Sanity checks:
        if not isinstance(x, int) and not isinstance(x, float):
            raise ExceptionWT("In ranturn(a): Angle a must be a number.")
        if self.extrudecalled:
            raise ExceptionWT(
                "In ranturn(a): Once extrude() is called, you can't keep drawing."
            )
        self.left(random() * 2 * x - x)

    def ranwidth(self, x):
        # Sanity checks:
        if not isinstance(x, int) and not isinstance(x, float):
            raise ExceptionWT("In ranwidth(w): Line width w must be a number.")
        if x <= 0:
            raise ExceptionWT("In ranwidth(w): Line width w must be positive.")
        if self.extrudecalled:
            raise ExceptionWT(
                "In ranwidth(w): Once extrude() is called, you can't keep drawing."
            )
        self.linewidth(random() * x)

    def ranheight(self, x):
        # Sanity checks:
        if not isinstance(x, int) and not isinstance(x, float):
            raise ExceptionWT("In ranheight(h): Line height h must be a number.")
        if x <= 0:
            raise ExceptionWT("In ranheight(h): Line height h must be positive.")
        if self.extrudecalled:
            raise ExceptionWT(
                "In ranheight(h): Once extrude() is called, you can't keep drawing."
            )
        self.lineheight(random() * x)

    def ranback(self, x):
        # Sanity checks:
        if not isinstance(x, int) and not isinstance(x, float):
            raise ExceptionWT("In ranback(d): Distance d must be a number.")
        if x < 0.0000001:
            raise ExceptionWT("In ranback(d): Distance d must be positive.")
        if self.extrudecalled:
            raise ExceptionWT(
                "In ranback(d): Once extrude() is called, you can't keep drawing."
            )
        self.back(random() * x)

    def ranwalk(self, n, s, a):
        # Sanity checks:
        if not isinstance(n, int) and not isinstance(n, float):
            raise ExceptionWT(
                "In ranwalk(n, s, a): Number of steps n must be a number."
            )
        if not isinstance(s, int) and not isinstance(s, float):
            raise ExceptionWT(
                "In ranwalk(n, s, a): Number of steps s must be a number."
            )
        if not isinstance(a, int) and not isinstance(a, float):
            raise ExceptionWT("In ranwalk(n, s, a): Angle a must be a number.")
        if self.extrudecalled:
            raise ExceptionWT(
                "In ranwalk(n, s, a): Once extrude() is called, you can't keep drawing."
            )
        cycles = n // s
        rest = n % s
        for i in range(cycles):
            self.ranturn(a)
            self.go(s)
        self.go(rest)

    def rancolor(self, minim=100):
        r = randint(minim, 255)
        g = randint(minim, 255)
        b = randint(minim, 255)
        self.color([r, g, b])

    #####  END OF RANDOM FUNCTIONALITY  #####

    def setpos(self, newx, newy):
        self.goto(newx, newy)

    def setposition(self, newx, newy):
        self.goto(newx, newy)

    def setx(self, newx):
        self.goto(newx, self.posy)

    def sety(self, newy):
        self.goto(self.posx, newy)

    def home(self):
        if self.extrudecalled:
            raise ExceptionWT("Once extrude() is called, you can't keep drawing.")
        draw0 = self.draw  # remember this flag
        self.draw = False
        self.goto(0, 0)
        self.angle(0)
        self.draw = draw0  # restore the original flag

    # Spanish:
    def casa(self):
        self.home()

    def getx(self):
        return round(self.posx, 6)

    def gety(self):
        return round(self.posy, 6)

    def getangle(self):
        return round(self.turtleangle, 6)

    def getcolor(self):
        return self.linecolor

    def getwidth(self):
        return round(self.linewidth, 6)

    def getheight(self):
        return round(self.lineheight, 6)

    def visible(self):
        self.isvisible = True

    def reveal(self):
        self.isvisible = True

    def invisible(self):
        self.isvisible = False

    def hide(self):
        self.isvisible = False

    # Spanish:
    def esconder(self):
        self.hide()

    # Spanish:
    def linea(self, x1, y1, x2, y2):
        self.line(x1, y1, x2, y2)

    # If called, the extrude command will override individual
    # heights of line segments.
    def extrude(self, height=1):
        # Sanity checks:
        if not isinstance(height, int) and not isinstance(height, float):
            raise ExceptionWT("In extrude(h): Extrusion height h must be a number.")
        if height <= 0.000001:
            raise ExceptionWT("In extrude(h): Extrusion height h must be positive.")
        # Body of function:
        self.extrudecalled = True
        self.lineheight = height
        self.isspiral = False
        self.isrosol = False
        self.isrosurf = False
        self.isroshell = False
        for l in self.lines:
            l.lineheight = height
        layer = 0
        dots = True
        elev = 0
        self.geom = NCLabTurtleTrace(self.lines, layer, dots, elev)

    def export(self):
        is3D = (
            self.isrosol
            or self.isrosurf
            or self.isroshell
            or self.isspiral
            or self.extrudecalled
        )
        if (not is3D) and (not self.heightused):  # Trace is 2D:
            for l in self.lines:
                l.lineheight = NCLAB_TURTLE_TRACE_H
            layer = 0
            dots = True
            elev = 0
            return NCLabTurtleTrace(self.lines, layer, dots, elev)
        else:  # Trace is 3D:
            if self.heightused:
                layer = 0
                dots = True
                elev = 0
                self.geom = NCLabTurtleTrace(self.lines, layer, dots, elev)
            return self.geom

    # Revolves complete trace including width
    def revolve(self, angle=360, div=32):
        # Sanity checks:
        if not isinstance(angle, int) and not isinstance(angle, float):
            raise ExceptionWT("In roshell(): Invalid angle.")
        if angle <= 0:
            raise ExceptionWT("In roshell(): Invalid angle.")
        if not isinstance(div, int) and not isinstance(div, float):
            raise ExceptionWT("In roshell(): Invalid angular division.")
        if div <= 3:
            raise ExceptionWT("In roshell(): Invalid angular division.")
        # Body of function:
        if self.heightused:
            raise ExceptionWT(
                "Once you use the height() command, revolve() cannot be used!"
            )
        if self.revolvecalled == True:
            raise ExceptionWT("Command revolve() can be only called once!")
        self.revolvecalled = True
        if angle <= 0.000001:
            raise ExceptionWT("Angle 'a' in revolve(a) must be positive!")
        self.isspiral = False
        self.isrosol = False
        self.isrosurf = False
        self.isroshell = True
        layer = 0
        dots = True
        elev = 0
        base = NCLabTurtleTrace(self.lines, layer, dots, elev)
        self.geom = REVOLVE(base, angle, div)

    # Another name for revolve()
    def roshell(self, angle=360, div=32):
        # Sanity checks:
        if not isinstance(angle, int) and not isinstance(angle, float):
            raise ExceptionWT("In roshell(): Invalid angle.")
        if angle <= 0:
            raise ExceptionWT("In roshell(): Invalid angle.")
        if not isinstance(div, int) and not isinstance(div, float):
            raise ExceptionWT("In roshell(): Invalid angular division.")
        if div <= 3:
            raise ExceptionWT("In roshell(): Invalid angular division.")
        # Body of function:
        if self.extrudecalled:
            raise ExceptionWT(
                "Once you use the extrude() command, rosol() cannot be used!"
            )
        if self.heightused:
            raise ExceptionWT(
                "Once you use the height() command, roshell() cannot be used!"
            )
        if self.roshellcalled == True:
            raise ExceptionWT("Command roshell() can be only called once!")
        self.roshellcalled = True
        if angle <= 0.000001:
            raise ExceptionWT("Angle 'a' in roshell(a) must be positive!")
        self.revolve(angle, div)

    # Spiral
    def spiral(self, angle, elevation, div=48):
        # Sanity checks:
        if not isinstance(angle, int) and not isinstance(angle, float):
            raise ExceptionWT("In spiral(): Invalid angle.")
        if angle <= 0:
            raise ExceptionWT("In spiral(): Invalid angle.")
        if not isinstance(elevation, int) and not isinstance(elevation, float):
            raise ExceptionWT("In spiral(): Invalid elevation.")
        if elevation <= 0:
            raise ExceptionWT("In spiral(): Invalid elevation.")
        if not isinstance(div, int) and not isinstance(div, float):
            raise ExceptionWT("In spiral(): Invalid angular division.")
        if div <= 3:
            raise ExceptionWT("In spiral(): Invalid angular division.")
        # Body of function:
        if self.heightused:
            raise ExceptionWT(
                "Once you use the height() command, spiral() cannot be used!"
            )
        if self.spiralcalled == True:
            raise ExceptionWT("Command spiral() can be only called once!")
        self.spiralcalled = True
        if angle <= 0.000001:
            raise ExceptionWT("Angle 'a' in spiral(a, elevation) must be positive!")
        self.isspiral = True
        self.isrosol = False
        self.isrosurf = False
        self.isroshell = False
        layer = 0
        dots = True
        elev = 0
        base = NCLabTurtleTrace(self.lines, layer, dots, elev)
        self.geom = SPIRAL(base, angle, elevation, div)

    # Rotational solid
    def rosol(self, angle=360, div=32):
        # Sanity checks:
        if not isinstance(angle, int) and not isinstance(angle, float):
            raise ExceptionWT("In rosol(): Invalid angle.")
        if angle <= 0:
            raise ExceptionWT("In rosol(): Invalid angle.")
        if not isinstance(div, int) and not isinstance(div, float):
            raise ExceptionWT("In rosol(): Invalid angular division.")
        if div <= 3:
            raise ExceptionWT("In rosol(): Invalid angular division.")
        # Body of function:
        if self.extrudecalled:
            raise ExceptionWT(
                "Once you use the extrude() command, rosol() cannot be used!"
            )
        if self.heightused:
            raise ExceptionWT(
                "Once you use the height() command, rosol() cannot be used!"
            )
        if self.rosolcalled == True:
            raise ExceptionWT("Command rosol() can be only called once!")
        self.rosolcalled = True
        if angle <= 0.000001:
            raise ExceptionWT("Angle 'a' in rosol(a) must be positive!")
        self.isspiral = False
        self.isrosol = True
        self.isrosurf = False
        self.isroshell = False
        self.geom = []
        for line in self.lines:
            a = POINT(line.startx, line.starty)
            b = POINT(line.endx, line.endy)
            paralleltox = abs(line.endy - line.starty) < 0.00001
            minr = 0
            nx = 1
            na = div
            nr = 1
            if not paralleltox:
                s = ROSOL([a, b], angle, minr, nx, na, nr)
                COLOR(s, line.linecolor)
                self.geom.append(s)

    # Rotational surface
    def rosurf(self, angle=360, div=32):
        # Sanity checks:
        if not isinstance(angle, int) and not isinstance(angle, float):
            raise ExceptionWT("In rosurf(): Invalid angle.")
        if angle <= 0:
            raise ExceptionWT("In rosurf(): Invalid angle.")
        if not isinstance(div, int) and not isinstance(div, float):
            raise ExceptionWT("In rosurf(): Invalid angular division.")
        if div <= 3:
            raise ExceptionWT("In rosurf(): Invalid angular division.")
        # Body of function:
        if self.extrudecalled:
            raise ExceptionWT(
                "Once you use the extrude() command, rosol() cannot be used!"
            )
        if self.heightused:
            raise ExceptionWT(
                "Once you use the height() command, rosurf() cannot be used!"
            )
        if self.rosurfcalled == True:
            raise ExceptionWT("Command rosurf() can be only called once!")
        self.rosurfcalled = True
        if angle <= 0.000001:
            raise ExceptionWT("Angle 'a' in rosurf(a) must be positive!")
        self.isspiral = False
        self.isrosol = False
        self.isrosurf = True
        self.isroshell = False
        self.geom = []
        for line in self.lines:
            a = POINT(line.startx, line.starty)
            b = POINT(line.endx, line.endy)
            nx = 1
            na = div
            s = ROSURF([a, b], angle, nx, na)
            COLOR(s, line.linecolor)
            self.geom.append(s)

    def erase(self):
        del self.lines[:]

    def reset(self):
        del self.lines[:]
        self.posx = 0
        self.posy = 0
        self.turtleangle = 0
        self.linecolor = [0, 0, 255]
        self.draw = True
        self.tracelength = 0
        self.linewidth = 1
        self.lineheight = 0
        self.canvassize = 100
        self.isvisible = True
        self.isspiral = False
        self.isrosol = False
        self.isrosurf = False
        self.isroshell = False
        self.geom = None
        # These commands can be called only once:
        self.rosolcalled = False
        self.rosurfcalled = False
        self.roshellcalled = False
        self.spiralcalled = False
        self.revolvecalled = False
        self.extrudecalled = False
        self.showcalled = False
        self.programended = False

    def arc(self, angle, radius, direction="r"):
        # Sanity checks:
        if angle < 0.00001:
            raise ExceptionWT("In arc(a, r, direction='r'): Angle a must be positive.")
        if radius < 0.00001:
            raise ExceptionWT("In arc(a, r, direction='r'): Radius r must be positive.")
        if direction != "r" and direction != "l":
            raise ExceptionWT(
                "In arc(a, r, direction='r'): Direction must be either 'r' or 'l'."
            )
        # Body of function:
        if self.extrudecalled:
            raise ExceptionWT("Once extrude() is called, you can't keep drawing.")
        # CONTINUATION IS NOW SOLVED ON THE LEVEL OF THE GOTO() COMMAND
        # Is it a continuation (posx, posy = last point, same width/height/color) ?
        # if len(self.lines) != 0:
        #    lastline = self.lines[-1]
        #    gap = sqrt((self.posx - lastline.endx)**2 + (self.posy - lastline.endy)**2)
        #    if gap < 0.0001:   # line uninterrupted
        #        if lastline.linecolor == self.linecolor:
        #            if abs(lastline.linewidth - self.linewidth) < 0.0001:
        #                if abs(lastline.lineheight - self.lineheight) < 0.0001:
        #                    lastline.continued = True
        # The arc:
        n = (angle / 180) * 18
        n = round(n)
        if n == 0:
            n = 1
        # Calculate center of arc:
        from numpy import cos, sin, pi

        vx = cos(self.turtleangle * pi / 180)
        vy = sin(self.turtleangle * pi / 180)
        leftarc = False
        if direction == "r" or direction == "R" or direction == "right":
            wx = vy
            wy = -vx
        else:
            leftarc = True
            wx = -vy
            wy = vx
        centerx = self.getx() + radius * wx
        centery = self.gety() + radius * wy
        Wx = -radius * wx
        Wy = -radius * wy
        ainit = arctan2(Wy, Wx)
        da = angle / n * pi / 180
        for i in range(n):
            if leftarc:
                xnext = centerx + radius * cos(ainit + (i + 1) * da)
                ynext = centery + radius * sin(ainit + (i + 1) * da)
            else:
                xnext = centerx + radius * cos(-ainit + (i + 1) * da)
                ynext = centery - radius * sin(-ainit + (i + 1) * da)
            self.goto(xnext, ynext)
        if leftarc:
            afinal = angle * pi / 180.0 + ainit
        else:
            afinal = ainit - angle * pi / 180.0
            xfinal = centerx + radius * cos(afinal)
            yfinal = centery + radius * sin(afinal)
            # Last: set correct angle based
            # on the true circle:
        if leftarc:
            self.angle(afinal * 180 / pi + 90)
        else:
            self.angle(afinal * 180 / pi - 90)

    # Spanish:
    def arco(self, angle, radius, direction="d"):
        if direction == "d" or direction == "D":
            direc = "r"
        else:
            direc = "l"
        self.arc(angle, radius, direc)

    def geometry(self):
        return self.geom

    def show(self, layer=0, dots=True):
        if self.showcalled == True:
            raise ExceptionWT("Command show() can be only called once!")
        self.showcalled = True
        self.programended = True
        # If geom is not None, show geometry, else show trace:
        if self.geom != None:
            SHOW(self.geom)
        else:
            NCLabTurtleShowTrace(self, layer, dots, NCLAB_TURTLE_TRACE_H)
        self._plot_turtle_trace()

    # To be used with the Turtle which produces the walls:
    def showwalls(self, layer=0, dots=True):
        # If geom is not None, show geometry, else show lines with height NCLAB_TURTLE_WALL_H:
        if self.geom != None:
            raise ExceptionWT(
                "Internal: self.geom should not be defined in showwalls()."
            )
        else:
            NCLabTurtleShowTrace(self, layer, dots, NCLAB_TURTLE_WALL_H)
        self._plot_turtle_trace()

    # Spanish:
    def mostrar(self, layer=0, dots=True):
        self.show(layer, dots)

    def _plot_turtle_trace(self):
        """
        Plot turtle "lines" property as pickled object, to be saved
        as binary file. Later it can be loaded and used to plot SVG.
        """
        import pickle, base64

        try:
            # Create a turtle instance and copy just enough data to be
            # able to create SVG plots.
            turtle = NCLabTurtle(user_created=False)
            turtle.lines = list(self.lines)

            plot = {
                "type": "binary",
                "data": base64.b64encode(pickle.dumps(turtle)).decode("utf-8"),
                "dtype": "application/octet-stream:turtle",
                "encoding": "base64",
                "output": "none",
                "name": "turtle_pickle",
            }
            nclabinst._pipe_plot(plot)
        except:
            # Fail quitely so the turtle show-ing is not interrupted.
            return False
        else:
            return True


# Spanish:
class TortugaNCLab(NCLabTurtle):
    pass
