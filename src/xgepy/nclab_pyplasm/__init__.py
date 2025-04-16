"""
NCLab PyPlasm package initialization.
Single file that imports all modules in the correct order to avoid circular dependencies.
"""

from .utils.step import StepAccumulator
from .utils.empty_list import *

# Then import domain as it's a basic dependency
from .domain.references import *

# Then import colors as it's used by both geometry and operations
from .colors.color_constants import *
from .colors.colorbar import *

# Then import geometry modules
from .geometry.base import BASEOBJ, EMPTYSET  # Do we want to expose EMPTYSET?
from .geometry.point import *
from .geometry.box import *
from .geometry.bounds import *
from .geometry.brick import *
from .geometry.cube import *
from .geometry.rectangle import *
from .geometry.square import *
from .geometry.triangle import *
from .geometry.quad import *
from .geometry.circle import *
from .geometry.ring import *
from .geometry.arc import *
from .geometry.ellipse import *
from .geometry.sphere import *
from .geometry.cylinder import *
from .geometry.cone import *
from .geometry.truncone import *
from .geometry.pyramid import *
from .geometry.torus import *
from .geometry.tube import *
from .geometry.elbow import *
from .geometry.spiral import *
from .geometry.revolve import *
from .geometry.prism import *
from .geometry.tetrahedron import *
from .geometry.dodecahedron import *
from .geometry.icosahedron import *
from .geometry.shell import *
from .geometry.simplex import *
from .geometry.chull import *
from .geometry.grid import *
from .geometry.arrangement import *
from .geometry.bezier import *
from .geometry.cubic_hermit import *
from .geometry.star import *
from .geometry.castle import *
from .geometry.tetris_3d import *
from .geometry.ludo import *
from .geometry.letter import *
from .geometry.tangram import *

# Import surfaces
from .geometry.surfaces.cylindrical_surface import *
from .geometry.surfaces.conical_surface import *
from .geometry.surfaces.profile_product_surface import *
from .geometry.surfaces.coons_patch import *
from .geometry.surfaces.rotational_surface import *
from .geometry.surfaces.ruled_surface import *

# Import shells
from .geometry.shells.rotational_shell import *
from .geometry.shells.spherical_shell import *

# Import solids
from .geometry.solids.rotational_solid import *

# Then import operations
from .operations.clean import *
from .operations.copy_objects import *
from .operations.cut import *
from .operations.difference import *
from .operations.erase import *
from .operations.flip import *
from .operations.get_dim import *
from .operations.intersection import *
from .operations.join import *
from .operations.move import *
from .operations.product import *
from .operations.rotate import *
from .operations.rotaterad import *
from .operations.scale import *
from .operations.show import *
from .operations.sizes import *
from .operations.struct import *
from .operations.union import *
from .operations.weld import *
from .operations.split import *
from .operations.revolve import *
from .operations.subtract import *
from .operations.material import *
from .operations.color import *
from .operations.extrude import *
from .operations.solidify import *
from .operations.map import *
from .operations.intervals import *
from .operations.xor import *

# Finally import turtle as it depends on both geometry and operations
from .turtle.turtle_2d import *
from .turtle.turtle_2d_utils import *
from .turtle.turtle_3d import *
from .turtle.turtle_3d_utils import *

# Import grading last as it might depend on all other modules
from .grading.grading_3d import *
from .grading.grading_turtle import *
from .grading.auto_grading import *
from .grading.validate import *
