from nclab.tools import ExceptionWT
from ..utils.common import flatten
from ..colors.color_constants import STEEL
from ...fenvs import (
    PLASM_DIM,
    PLASM_MATERIAL,
    PLASM_COLOR,
    PLASM_DIFF,
    PLASM_TRANSLATE,
    PLASM_INTERSECTION,
    PLASM_SCALE,
    PLASM_HEX,
    MIN,
    MAX,
    PI,
    Plasm,
    Color4f,
)


class BASEOBJ:
    """
    Base class for all geometric objects for nclab_pyplasm.

    This class serves as the foundation for all geometric primitives and operations,
    providing common functionality for:
    - Material and color management
    - Geometric transformations (move, rotate, scale)
    - Boolean operations (subtract, difference)
    - Dimension and boundary queries
    """

    def __init__(self, basegeom):
        self.color = STEEL
        self.geom = basegeom
        self.dim = PLASM_DIM(basegeom)
        self.opacity = 1.0
        self.shininess = 0.3
        self.material = [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 100]

    def __getattr__(self, name):
        # special attributes are probably not searched by normal user
        if name[0:2] == "__" and name[-2:]:
            raise AttributeError
        raise ExceptionWT(
            'Did you want to write "," (comma) instead of "." (period) before "{}" or did you misspell "{}"?'.format(
                name, name
            )
        )

    def __coerce__(self, other):
        if isinstance(other, list):
            return [self], other

    def __repr__(self):
        return "Plasm %sD object" % self.dim

    def setmaterial(self, mat):
        # Check if the material is a list:
        if type(mat) is list:
            if len(mat) != 17:
                raise ExceptionWT(
                    "Material must be a list of 17 values: ambientRGBA, diffuseRGBA specularRGBA emissionRGBA shininess"
                )
            else:
                self.material = mat
                self.geom = PLASM_MATERIAL(mat)(self.geom)
        else:
            raise ExceptionWT(
                "Material must be a list of 17 values: ambientRGBA, diffuseRGBA specularRGBA emissionRGBA shininess"
            )

    def getmaterial(self):
        return self.material

    def _is_valid_hex(self, hex_color):
        hex_digits = hex_color.lstrip("#")
        return len(hex_digits) == 6 and all(
            c in "0123456789abcdefABCDEF" for c in hex_digits
        )

    def _validate_rgb_list(self, color):
        if len(color) != 3 and len(color) != 4:
            raise ExceptionWT(
                "Color must be a list of length 3 [R, G, B] or 4 [R, G, B, A]!"
            )
        if (
            color[0] < 0
            or color[0] > 255
            or color[1] < 0
            or color[1] > 255
            or color[2] < 0
            or color[2] > 255
        ):
            raise ExceptionWT(
                "RGB values in color definition must lie between 0 and 255!"
            )
        if len(color) == 4:
            if color[3] < 0 or color[3] > 1:
                raise ExceptionWT(
                    "Opacity value in color definition must be between 0 and 1!"
                )

    def setcolor(self, color=STEEL, opacity=None, shininess=None):
        if opacity is not None:
            self.opacity = opacity
        if shininess is not None:
            self.shininess = shininess

        if isinstance(color, str) and color.startswith("#"):
            if not self._is_valid_hex(color):
                raise ExceptionWT(
                    f"Invalid hex color format: {color}. Color must be a hex string (e.g. '#FF0000')."
                )
            hex_color = color.lstrip("#")
            rgb_color = [int(hex_color[i : i + 2], 16) for i in (0, 2, 4)]
            self.color = rgb_color
            self.geom = PLASM_HEX(color)(self.geom)
            return

        if isinstance(color, list):
            self._validate_rgb_list(color)
            self.color = color
            self.geom = PLASM_COLOR(color)(self.geom)
            return

        raise ExceptionWT(
            "Color must be a hex string (e.g., '#FF0000') or a list [R, G, B] or [R, G, B, A]!"
        )

    # Subtract a single object or list of objects from self, changing self's
    # geometry:

    def subtract(self, obj):
        geoms = [self.geom]
        if not isinstance(obj, list):
            if isinstance(obj, tuple):
                raise ExceptionWT("Use the UNION command to create unions of objects.")
            if not isinstance(obj, BASEOBJ):
                raise ExceptionWT("Invalid object found (subtract - 1).")
            if self.dim != obj.dim:
                raise ExceptionWT(
                    "Received a 3D object where a 2D object was expected, or vice versa."
                )
            geoms.append(obj.geom)
        else:
            for x in obj:
                if isinstance(x, tuple):
                    raise ExceptionWT(
                        "Use the UNION command to create unions of objects."
                    )
                if not isinstance(x, BASEOBJ):
                    raise ExceptionWT("Invalid object found (subtract - 2).")
                if self.dim != x.dim:
                    raise ExceptionWT(
                        "Received a 3D object where a 2D object was expected, or vice versa."
                    )
                geoms.append(x.geom)
        newgeom = PLASM_DIFF(geoms)
        self.geom = newgeom
        self.setcolor(self.color)

    # Subtract a single object or list of objects from self, NOT changing
    # self's geometry:

    def diff(self, obj):
        geoms = [self.geom]
        if not isinstance(obj, list):
            if isinstance(obj, tuple):
                raise ExceptionWT("Use the UNION command to create unions of objects.")
            if not isinstance(obj, BASEOBJ):
                raise ExceptionWT("Invalid object found (diff - 1).")
            if self.dim != obj.dim:
                raise ExceptionWT(
                    "Received a 3D object where a 2D object was expected, or vice versa."
                )
            geoms.append(obj.geom)
        else:
            for x in obj:
                if isinstance(obj, tuple):
                    raise ExceptionWT(
                        "Use the UNION command to create unions of objects."
                    )
                if not isinstance(x, BASEOBJ):
                    raise ExceptionWT("Invalid object found (diff - 2).")
                if self.dim != x.dim:
                    raise ExceptionWT(
                        "Received a 3D object where a 2D object was expected, or vice versa."
                    )
                geoms.append(x.geom)
        newgeom = PLASM_DIFF(geoms)
        newobj = BASEOBJ(newgeom)
        newobj.setcolor(self.color)
        return newobj

    def getcolor(self):
        return self.color

    def move(self, t1, t2, t3=0):
        if EMPTYSET(self):
            return
        if t3 == 0:
            self.geom = PLASM_TRANSLATE([1, 2])([t1, t2])(self.geom)
        else:
            # THIS CONDITION WAS IN THE WAY WHEN I MOVED CURVED SURFACES IN 3D:
            # if self.dim != 3:
            #    raise ExceptionWT("2D objects may be moved in the xy-plane only, not in 3D!")
            self.geom = PLASM_TRANSLATE([1, 2, 3])([t1, t2, t3])(self.geom)
        self.setcolor(self.color)

    def rotaterad(self, angle_rad, axis=3, point=[0, 0, 0]):
        if EMPTYSET(self):
            return
        if axis == "x" or axis == "X":
            axis = 1
        if axis == "y" or axis == "Y":
            axis = 2
        if axis == "z" or axis == "Z":
            axis = 3
        centerpoint = point
        # check the axis:
        if axis != 1 and axis != 2 and axis != 3:
            raise ExceptionWT(
                "The third argument of ROTATE must be either X (x-axis), Y (y-axis), or Z (z-axis)!"
            )
            # if self.dim == 2 and axis != 3:
            # THIS CONDITION WAS IN THE WAY WHEN I MOVED CURVED SURFACES IN 3D:
            # raise ExceptionWT("2D objects may be rotated in the xy-plane only, not in 3D!")
        if axis == 1:
            plane_indexes = [2, 3]
        elif axis == 2:
            plane_indexes = [3, 1]
        else:
            plane_indexes = [1, 2]
        # sanity check for the center point:
        if not isinstance(centerpoint, list):
            raise ExceptionWT("The optional center point in ROTATE must be a list!")
        centerpointdim = len(centerpoint)
        if centerpointdim != 2 and centerpointdim != 3:
            raise ExceptionWT(
                "The optional center point in ROTATE must be a list of either 2 or 3 coordinates!"
            )
        # if 3D object and 2D point, make third coordinate zero:
        if centerpointdim == 2 and self.dim == 3:
            centerpoint.append(0)
        # if 2D object and 3D point, ignore third coordinate:
        if centerpointdim == 3 and self.dim == 2:
            forgetlast = centerpoint.pop()
        # if point is not zero, move object first:
        if self.dim == 2:
            if centerpoint[0] != 0 or centerpoint[1] != 0:
                self.geom = PLASM_TRANSLATE([1, 2])([-centerpoint[0], -centerpoint[1]])(
                    self.geom
                )
        else:
            if centerpoint[0] != 0 or centerpoint[1] != 0 or centerpoint[2] != 0:
                self.geom = PLASM_TRANSLATE([1, 2, 3])(
                    [-centerpoint[0], -centerpoint[1], -centerpoint[2]]
                )(self.geom)
        # call the PLaSM rotate command:
        dim = max(plane_indexes)
        self.geom = Plasm.rotate(
            self.geom, dim, plane_indexes[0], plane_indexes[1], angle_rad
        )
        # if point is not zero, return object back:
        if self.dim == 2:
            if centerpoint[0] != 0 or centerpoint[1] != 0:
                self.geom = PLASM_TRANSLATE([1, 2])([centerpoint[0], centerpoint[1]])(
                    self.geom
                )
        else:
            if centerpoint[0] != 0 or centerpoint[1] != 0 or centerpoint[2] != 0:
                self.geom = PLASM_TRANSLATE([1, 2, 3])(
                    [centerpoint[0], centerpoint[1], centerpoint[2]]
                )(self.geom)
        # return color:
        self.setcolor(self.color)

    def rotate(self, angle_deg, axis=3, point=[0, 0, 0]):
        if EMPTYSET(self):
            return
        if axis == "x" or axis == "X":
            axis = 1
        if axis == "y" or axis == "Y":
            axis = 2
        if axis == "z" or axis == "Z":
            axis = 3
        angle_rad = PI * angle_deg / 180.0
        self.rotaterad(angle_rad, axis, point)
        self.setcolor(self.color)

    def getdimension(self):
        return self.dim

    def scale(self, a, b, c=1):
        if EMPTYSET(self):
            return
        # if a < 0 or b < 0 or c < 0:
        # THIS WAS IN THE WAY WHEN I DEFINED FLIP()
        #    raise ExceptionWT(
        #        "When scaling an object, all axial coefficients must be greater than zero!")
        if a == 0 or b == 0 or c == 0:
            raise ExceptionWT(
                "When scaling an object, all coefficients must be nonzero!"
            )
            # if self.dim == 2 and c != 1.0:
            # THIS CONDITION WAS IN THE WAY WHEN I MOVED CURVED SURFACES IN 3D:
            # raise ExceptionWT("2D objects may be scaled in the xy-plane only, not in 3D!")
        if self.dim == 3:
            self.geom = PLASM_SCALE([1, 2, 3])([a, b, c])(self.geom)
        else:
            # Important: When 2D objects such as a circle get scaled in all three
            # directions, even though c == 1, this caused problems.
            if abs(c - 1.0) < 0.0001:
                self.geom = PLASM_SCALE([1, 2])([a, b])(self.geom)
            else:
                self.geom = PLASM_SCALE([1, 2, 3])([a, b, c])(self.geom)
        self.setcolor(self.color)

    def minx(self):
        if EMPTYSET(self):
            raise ExceptionWT("Cannot calculate minx() of an empty set.")
        else:
            return MIN(1)(self.geom)

    def miny(self):
        if EMPTYSET(self):
            raise ExceptionWT("Cannot calculate miny() of an empty set.")
        else:
            return MIN(2)(self.geom)

    def minz(self):
        if EMPTYSET(self):
            raise ExceptionWT("Cannot calculate minz() of an empty set.")
        else:
            return MIN(3)(self.geom)

    def maxx(self):
        if EMPTYSET(self):
            raise ExceptionWT("Cannot calculate maxx() of an empty set.")
        else:
            return MAX(1)(self.geom)

    def maxy(self):
        if EMPTYSET(self):
            raise ExceptionWT("Cannot calculate maxy() of an empty set.")
        else:
            return MAX(2)(self.geom)

    def maxz(self):
        if EMPTYSET(self):
            raise ExceptionWT("Cannot calculate maxz() of an empty set.")
        else:
            return MAX(3)(self.geom)

    def sizex(self):
        if EMPTYSET(self):
            raise ExceptionWT("Cannot calculate sizex() of an empty set.")
        else:
            return MAX(1)(self.geom) - MIN(1)(self.geom)

    def sizey(self):
        if EMPTYSET(self):
            raise ExceptionWT("Cannot calculate sizey() of an empty set.")
        else:
            return MAX(2)(self.geom) - MIN(2)(self.geom)

    def sizez(self):
        if EMPTYSET(self):
            raise ExceptionWT("Cannot calculate sizez() of an empty set.")
        else:
            return MAX(3)(self.geom) - MIN(3)(self.geom)

    def erasex(self, erasexmin, erasexmax):
        from ..geometry.box import BOX
        from ..operations.move import MOVE

        minx = self.minx()
        if minx == None:
            return
        maxx = self.maxx()
        if maxx == None:
            return
        miny = self.miny()
        if miny == None:
            return
        maxy = self.maxy()
        if maxy == None:
            return
        if self.dim == 2:
            box = BOX(erasexmax - erasexmin, maxy - miny + 2)
            MOVE(box, erasexmin, miny - 1)
            self.geom = PLASM_DIFF([self.geom, box.geom])
            self.setcolor(self.color)
        else:
            minz = self.minz()
            if minz == None:
                return
            maxz = self.maxz()
            if maxz == None:
                return
            box = BOX(erasexmax - erasexmin, maxy - miny + 2, maxz - minz + 2)
            MOVE(box, erasexmin, miny - 1, minz - 1)
            self.geom = PLASM_DIFF([self.geom, box.geom])
            self.setcolor(self.color)

    def splitx(self, coord):
        from ..geometry.box import BOX
        from ..geometry.cube import CUBE
        from ..geometry.square import SQUARE
        from ..operations.move import MOVE
        from ..operations.difference import DIFFERENCE

        minx = self.minx()
        if minx == None:
            return None, None
        maxx = self.maxx()
        if maxx == None:
            return None, None
        miny = self.miny()
        if miny == None:
            return None, None
        maxy = self.maxy()
        if maxy == None:
            return None, None
        if self.dim == 2:
            # Cutplane goes past object:
            if coord >= maxx:
                emptysetwarning = False
                emptyset = DIFFERENCE(SQUARE(1), SQUARE(1), emptysetwarning)
                return self, emptyset
            if coord <= minx:
                emptyset = DIFFERENCE(SQUARE(1), SQUARE(1), emptysetwarning)
                return emptyset, self
            # Object will be split into two new objects:
            box1 = BOX(coord - minx, maxy - miny + 2)
            box2 = BOX(maxx - coord, maxy - miny + 2)
            MOVE(box1, minx, miny - 1)
            MOVE(box2, coord, miny - 1)
            obj1 = BASEOBJ(PLASM_INTERSECTION([self.geom, box1.geom]))
            obj2 = BASEOBJ(PLASM_INTERSECTION([self.geom, box2.geom]))
            obj1.setcolor(self.color)
            obj2.setcolor(self.color)
        else:
            minz = self.minz()
            if minz == None:
                return None, None
            maxz = self.maxz()
            if maxz == None:
                return None, None
            # Cutplane goes past object:
            if coord >= maxx:
                emptysetwarning = False
                emptyset = DIFFERENCE(CUBE(1), CUBE(1), emptysetwarning)
                return self, emptyset
            if coord <= minx:
                emptysetwarning = False
                emptyset = DIFFERENCE(CUBE(1), CUBE(1), emptysetwarning)
                return emptyset, self
            # Object will be split into two new objects:
            box1 = BOX(coord - minx, maxy - miny + 2, maxz - minz + 2)
            box2 = BOX(maxx - coord, maxy - miny + 2, maxz - minz + 2)
            MOVE(box1, minx, miny - 1, minz - 1)
            MOVE(box2, coord, miny - 1, minz - 1)
            obj1 = BASEOBJ(PLASM_INTERSECTION([self.geom, box1.geom]))
            obj2 = BASEOBJ(PLASM_INTERSECTION([self.geom, box2.geom]))
            obj1.setcolor(self.color)
            obj2.setcolor(self.color)
        return obj1, obj2


def EMPTYSET(obj):
    """
    Check if a geometric object is empty by examining its batches.

    This function is tightly coupled with BASEOBJ as it specifically checks
    for empty geometric objects that are instances of BASEOBJ or lists of BASEOBJ.
    """

    # If it is an empty list, return True:
    if isinstance(obj, list):
        if obj == []:
            return True
    # Sanity test:
    if isinstance(obj, list):
        obj = flatten(obj)
        for oo in obj:
            if isinstance(oo, tuple):
                raise ExceptionWT("Use the UNION command to create unions of objects.")
            if not isinstance(oo, BASEOBJ):
                raise ExceptionWT("Invalid object found (emptyset - 1).")
    else:
        if isinstance(obj, tuple):
            raise ExceptionWT("Use the UNION command to create unions of objects.")
        if not isinstance(obj, BASEOBJ):
            raise ExceptionWT("Invalid object found (emptyset - 2).")
    # Emptyset test:
    l = 0
    if isinstance(obj, list):
        maxlen = 0
        flatobj = flatten(obj)
        for x in flatobj:
            if len(Plasm.getBatches(x.geom)) > maxlen:
                maxlen = len(Plasm.getBatches(x.geom))
        l = maxlen
    else:
        l = len(Plasm.getBatches(obj.geom))
    if l == 0:
        return True
    else:
        return False
