"""
NCLAB TURTLE 3D - CLASSES
"""

from numpy import sqrt, sin, cos, pi, arctan2


from nclab.tools import ExceptionWT
from ..colors.color_constants import YELLOW
from ..turtle.turtle_3d_utils import NCLabTurtleShow3D


# Class Line3D:
class NCLabTurtleLine3D:
    def __init__(self, sx, sy, sz, dist, u1, u2, u3, v1, v2, v3, w1, w2, w3, width, c):
        self.startx = sx
        self.starty = sy
        self.startz = sz
        self.dist = dist
        # Unit vector in the direction of the line (local X)
        self.u1 = u1
        self.u2 = u2
        self.u3 = u3
        # Unit vector in the local Y direction
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        # Unit vector in the local Z direction
        self.w1 = w1
        self.w2 = w2
        self.w3 = w3
        self.linewidth = width
        self.linecolor = c


# Class Turtle3D:
class NCLabTurtle3D:
    def __init__(self, px=0, py=0, pz=0):
        self.posx = px
        self.posy = py
        self.posz = pz
        # Unit vector in local X direction:
        self.u1 = 1
        self.u2 = 0
        self.u3 = 0
        # Unit vector in local Y direction:
        self.v1 = 0
        self.v2 = 1
        self.v3 = 0
        # Unit vector in local Z direction:
        self.w1 = 0
        self.w2 = 0
        self.w3 = 1
        # Line color etc.
        self.linecolor = YELLOW
        self.draw = True
        self.linewidth = 1
        self.canvassize = 100
        self.lines = []
        self.isvisible = True
        self.edgenum = 8
        self.geom = None
        # These commands can be called only once:
        self.showcalled = False
        self.programended = False

    def color(self, col, col2=None):
        if not isinstance(col, list):
            raise ExceptionWT(
                "Attempt to set invalid color. Have you forgotten square brackets?"
            )
        if len(col) != 3:
            raise ExceptionWT(
                "Attempt to set invalid color. Have you used three integers between 0 and 255?"
            )
        for i in range(3):
            if col[i] < 0 or col[i] > 255:
                raise ExceptionWT(
                    "Attempt to set invalid color. Have you used three integers between 0 and 255?"
                )
        self.linecolor = col
        if col2 != None:  # Second color is defined
            if not isinstance(col2, list):
                raise ExceptionWT(
                    "Attempt to set invalid optional 2nd color. Have you forgotten square brackets?"
                )
            if len(col2) != 3:
                raise ExceptionWT(
                    "Attempt to set invalid optional 2nd color. Have you used three integers between 0 and 255?"
                )
            for i in range(3):
                if col2[i] < 0 or col2[i] > 255:
                    raise ExceptionWT(
                        "Attempt to set invalid optional 2nd color. Have you used three integers between 0 and 255?"
                    )
        self.linecolor2 = col2

    def width(self, w):
        # Sanity checks:
        if not isinstance(w, int) and not isinstance(w, float):
            raise ExceptionWT("In width(w): Line width w must be a number.")
        if w <= 0:
            raise ExceptionWT("In width(w): Line width w must be positive.")
        # Body of function:
        if w < 0.1:
            raise ExceptionWT("In width(w): Line width w must be between 0.1 and 10.0.")
        if w > 10.0:
            raise ExceptionWT("In width(w): Line width w must be between 0.1 and 10.0.")
        self.linewidth = w

    def angles(self, l, u, r):
        # Sanity checks:
        if not isinstance(l, int) and not isinstance(l, float):
            raise ExceptionWT("In angles(l, u, r): Angle l (left) must be a number.")
        if not isinstance(u, int) and not isinstance(u, float):
            raise ExceptionWT("In angles(l, u, r): Angle u (up) must be a number.")
        if not isinstance(r, int) and not isinstance(r, float):
            raise ExceptionWT("In angles(l, u, r): Angle r (roll) must be a number.")
        self.resetangles()
        self.left(l)
        self.up(u)
        self.roll(r, "l")

    def getangles(self):
        a1 = 0
        a2 = 0
        a3 = 0
        dd = sqrt(self.u1**2 + self.u2**2)
        # print("dd =", dd)
        # print("u1, u2, u3:", round(self.u1, 3), round(self.u2, 3), round(self.u3, 3))
        # print("v1, v2, v3:", round(self.v1, 3), round(self.v2, 3), round(self.v3, 3))
        # print("w1, w2, w3:", round(self.w1, 3), round(self.w2, 3), round(self.w3, 3))
        if dd > 1e-4:
            a1 = arctan2(self.u2, self.u1) * 180 / pi
            a2 = arctan2(self.u3, dd) * 180 / pi
            a3 = arctan2(self.v3, self.w3) * 180 / pi
        else:  # local X is vertical
            a1 = 0  # OK
            if self.u3 > 0:
                a2 = 90  # Local X points up
                a3 = arctan2(self.w2, self.w1) * 180 / pi - 180
            else:
                a2 = -90  # Local X points down
                a3 = -arctan2(self.w2, self.w1) * 180 / pi
        return a1, a2, a3

    def edges(self, e):
        if e < 3:
            raise ExceptionWT("The minimum number of edges is three.")
        self.edgenum = e

    def penup(self):
        self.draw = False

    def pu(self):
        self.draw = False

    def pendown(self):
        self.draw = True

    def pd(self):
        self.draw = True

    def isdown(self):
        return self.draw

    def up(self, da2):
        # Create new vector X by rotating (1, 0, 0) by da2 degrees about the Y axis:
        x1 = cos(da2 * pi / 180)
        x2 = 0
        x3 = sin(da2 * pi / 180)
        # Create new vector Z by rotating (0, 0, 1) by da2 degrees about the Y axis:
        z1 = -sin(da2 * pi / 180)
        z2 = 0
        z3 = cos(da2 * pi / 180)
        # Rotation matrix:
        # u1   v1   w1
        # u2   v2   w2
        # u3   v3   w3
        # Create new vector U: Multiply this matrix with new X:
        newu1 = self.u1 * x1 + self.v1 * x2 + self.w1 * x3
        newu2 = self.u2 * x1 + self.v2 * x2 + self.w2 * x3
        newu3 = self.u3 * x1 + self.v3 * x2 + self.w3 * x3
        # Create new vector Z: Multiply this matrix with new Z:
        neww1 = self.u1 * z1 + self.v1 * z2 + self.w1 * z3
        neww2 = self.u2 * z1 + self.v2 * z2 + self.w2 * z3
        neww3 = self.u3 * z1 + self.v3 * z2 + self.w3 * z3
        # Update vectors U (local X) and W (local Z):
        self.u1 = newu1
        self.u2 = newu2
        self.u3 = newu3
        self.w1 = neww1
        self.w2 = neww2
        self.w3 = neww3

    def pitch(self, da):
        self.up(da)

    def down(self, da):
        self.up(-da)

    def go(self, dist):
        # Sanity checks:
        if not isinstance(dist, int) and not isinstance(dist, float):
            raise ExceptionWT("In go(d): Distance d must be a number.")
        if abs(dist) < 0.00000001:  # if turtle has not moved, just return
            return
        if dist < 0:
            raise ExceptionWT("In go(d): Distance d must be positive.")
        # Body of function:
        if self.draw == True:
            newline = NCLabTurtleLine3D(
                self.posx,
                self.posy,
                self.posz,
                dist,
                self.u1,
                self.u2,
                self.u3,
                self.v1,
                self.v2,
                self.v3,
                self.w1,
                self.w2,
                self.w3,
                self.linewidth,
                self.linecolor,
            )
            self.lines.append(newline)
        # Update position:
        self.posx += dist * self.u1
        self.posy += dist * self.u2
        self.posz += dist * self.u3

    def printlines(self):
        for line in self.lines:
            print("---")
            print(
                "Start:",
                round(line.startx, 3),
                round(line.starty, 3),
                round(line.startz, 3),
            )
            d = line.dist
            print(
                "End:  ",
                round(line.startx + d * line.u1, 3),
                round(line.starty + d * line.u2, 3),
                round(line.startz + d * line.u3, 3),
            )
            print("X:", round(line.u1, 3), round(line.u2, 3), round(line.u3, 3))
            print("Y:", round(line.v1, 3), round(line.v2, 3), round(line.v3, 3))
            print("Z:", round(line.w1, 3), round(line.w2, 3), round(line.w3, 3))

    def forward(self, dist):
        self.go(dist)

    def fd(self, dist):
        self.go(dist)

    def left(self, da1):
        # Sanity checks:
        if not isinstance(da1, int) and not isinstance(da1, float):
            raise ExceptionWT("In left(a): Angle a must be a number.")
        # Body of function:
        # Create new vector X by rotating (1, 0, 0) by da1 degrees about the Z axis:
        x1 = cos(da1 * pi / 180)
        x2 = sin(da1 * pi / 180)
        x3 = 0
        # Create new vector Y by rotating (0, 1, 0) by da1 degrees about the Z axis:
        y1 = -sin(da1 * pi / 180)
        y2 = cos(da1 * pi / 180)
        y3 = 0
        # Rotation matrix:
        # u1   v1   w1
        # u2   v2   w2
        # u3   v3   w3
        # Create new vector U: Multiply this matrix with new X:
        newu1 = self.u1 * x1 + self.v1 * x2 + self.w1 * x3
        newu2 = self.u2 * x1 + self.v2 * x2 + self.w2 * x3
        newu3 = self.u3 * x1 + self.v3 * x2 + self.w3 * x3
        # Create new vector Z: Multiply this matrix with new Y:
        newv1 = self.u1 * y1 + self.v1 * y2 + self.w1 * y3
        newv2 = self.u2 * y1 + self.v2 * y2 + self.w2 * y3
        newv3 = self.u3 * y1 + self.v3 * y2 + self.w3 * y3
        # Update vectors U (local X) and V (local Y):
        self.u1 = newu1
        self.u2 = newu2
        self.u3 = newu3
        self.v1 = newv1
        self.v2 = newv2
        self.v3 = newv3

    def yaw(self, da1):
        self.left(da1)

    def lt(self, da1):
        self.left(da1)

    def right(self, da1):
        # Sanity checks:
        if not isinstance(da1, int) and not isinstance(da1, float):
            raise ExceptionWT("In right(a): Angle a must be a number.")
        # Body of function:
        self.left(-da1)

    def rt(self, da1):
        self.right(da1)

    def roll(self, da, direction="l"):
        if direction == "r" or direction == "R" or direction == "right":
            da *= -1
        # Create new vector Y by rotating (0, 1, 0) by da degrees about the X axis:
        y1 = 0
        y2 = cos(da * pi / 180)
        y3 = -sin(da * pi / 180)
        # Create new vector Z by rotating (0, 0, 1) by da degrees about the X axis:
        z1 = 0
        z2 = sin(da * pi / 180)
        z3 = cos(da * pi / 180)
        # Rotation matrix:
        # u1   v1   w1
        # u2   v2   w2
        # u3   v3   w3
        # Create new vector V: Multiply this matrix with new Y:
        newv1 = self.u1 * y1 + self.v1 * y2 + self.w1 * y3
        newv2 = self.u2 * y1 + self.v2 * y2 + self.w2 * y3
        newv3 = self.u3 * y1 + self.v3 * y2 + self.w3 * y3
        # Create new vector W: Multiply this matrix with new Z:
        neww1 = self.u1 * z1 + self.v1 * z2 + self.w1 * z3
        neww2 = self.u2 * z1 + self.v2 * z2 + self.w2 * z3
        neww3 = self.u3 * z1 + self.v3 * z2 + self.w3 * z3
        # Update vectors V (local Y) and W (local Z):
        self.v1 = newv1
        self.v2 = newv2
        self.v3 = newv3
        self.w1 = neww1
        self.w2 = neww2
        self.w3 = neww3

    def back(self, dist):
        if dist <= 0:
            raise ExceptionWT("The distance d in back(d) must be positive!")
        self.posx -= dist * self.u1
        self.posy -= dist * self.u2
        self.posz -= dist * self.u3

    def backward(self, dist):
        self.back(dist)

    def bk(self, dist):
        self.back(dist)

    def resetangles(self):
        self.u1 = 1
        self.u2 = 0
        self.u3 = 0
        self.v1 = 0
        self.v2 = 1
        self.v3 = 0
        self.w1 = 0
        self.w2 = 0
        self.w3 = 1

    # After goto(), all angles are reset to zero.
    def goto(self, newx, newy, newz):
        if self.draw == True:
            dx = newx - self.posx
            dy = newy - self.posy
            dz = newz - self.posz
            dist = sqrt(dx**2 + dy**2 + dz**2)
            if dist <= 1e-6:
                raise ExceptionWT(
                    "The distance in the goto() command must be positive!"
                )
            # Unit U vector
            u1 = dx / dist
            u2 = dy / dist
            u3 = dz / dist
            # Unit V vector (normal to U, third component zero)
            d0 = sqrt(u1**2 + u2**2)
            if d0 > 1e-4:
                v1 = -u2
                v2 = u1
                v3 = 0
                v1 /= d0  # Normalization
                v2 /= d0
            else:
                v1 = 0
                v2 = u3
                v3 = -u2
                d0 = sqrt(v2**2 + v3**2)
                v2 /= d0  # Normalization
                v3 /= d0
            # Unit W vector... cross product of U and V
            w1 = u2 * v3 - u3 * v2
            w2 = u3 * v1 - u1 * v3
            w3 = u1 * v2 - u2 * v1
            d0 = sqrt(w1**2 + w2**2 + w3**2)  # Normalization
            w1 /= d0
            w2 /= d0
            w3 /= d0
            newline = NCLabTurtleLine3D(
                self.posx,
                self.posy,
                self.posz,
                dist,
                u1,
                u2,
                u3,
                v1,
                v2,
                v3,
                w1,
                w2,
                w3,
                self.linewidth,
                self.linecolor,
            )
            self.lines.append(newline)
        # Update position:
        self.posx = newx
        self.posy = newy
        self.posz = newz
        # Reset angles:
        self.resetangles()

    def setpos(self, newx, newy, newz):
        self.goto(newx, newy, newz)

    def setposition(self, newx, newy, newz):
        self.goto(newx, newy, newz)

    def setx(self, newx):
        self.goto(newx, self.posy, self.posz)

    def sety(self, newy):
        self.goto(self.posx, newy, self.posz)

    def setz(self, newz):
        self.goto(self.posx, self.posy, newz)

    def home(self):
        self.posx = 0
        self.posy = 0
        self.posz = 0
        self.resetangles()

    def getx(self):
        return self.posx

    def gety(self):
        return self.posy

    def getz(self):
        return self.posz

    def getcolor(self):
        return self.linecolor

    def getwidth(self):
        return self.linewidth

    def visible(self):
        self.isvisible = True

    def reveal(self):
        self.isvisible = True

    def invisible(self):
        self.isvisible = False

    def hide(self):
        self.isvisible = False

    def export(self):
        return self.geom

    def erase(self):
        del self.lines[:]

    def reset(self):
        del self.lines[:]
        self.posx = 0
        self.posy = 0
        self.posz = 0
        self.u1 = 1
        self.u2 = 0
        self.u3 = 0
        self.v1 = 0
        self.v2 = 1
        self.v3 = 0
        self.w1 = 0
        self.w2 = 0
        self.w3 = 1
        self.linecolor = YELLOW
        self.draw = True
        self.linewidth = 1
        self.canvassize = 100
        self.isvisible = True
        self.geom = None
        # These commands can be called only once:
        self.showcalled = False

    def arc(self, angle, radius, direction="r"):
        if angle < 0.001:
            raise ExceptionWT("Angle 'a' in arc(a, r) must be positive!")
        if radius < 0.001:
            raise ExceptionWT("Radius 'r' in arc(a, r) must be positive!")
        n = (angle / 180) * 18
        n = round(n)
        step = 0.174977327052 * radius
        self.go(0.5 * step)
        if direction == "r" or direction == "R" or direction == "right":
            self.right(10)
        else:
            self.left(10)
        for j in range(n - 1):
            self.go(step)
            if direction == "r" or direction == "R" or direction == "right":
                self.right(10)
            else:
                self.left(10)
        self.go(0.5 * step)

    def geometry(self):
        return self.geom

    def show(self, layer=0, dots=True):
        if self.showcalled == True:
            raise ExceptionWT("Command show() can be only called once!")
        self.showcalled = True
        NCLabTurtleShow3D(self)
