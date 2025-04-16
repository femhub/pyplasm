"""
 DEV-3528 changes for "3D modeling course"
"""

from ..utils.constants import X
from ..geometry.surfaces.rotational_surface import ROSURF
from ..operations.rotate import ROTATE
from ..operations.copy_objects import COPY
from ..operations.color import COLOR
from ..colors.color_constants import BLUE, YELLOW, GREEN, RED, PINK


ludo_pts = [
    [0.3, 0],
    [0.3, 0.5],
    [0.2, 0.6],
    [0.2, 0.7],
    [0.05, 0.79],
    [0, 0.8],
    [0.05, 0.81],
    [0.18, 0.85],
    [0.22, 0.9],
    [0.22, 1],
    [0.22, 1.1],
    [0.18, 1.19],
    [0, 1.2],
]

ludo_token = ROSURF(ludo_pts, 360, 24, 24)
ROTATE(ludo_token, 90, X)

# Blue Ludo piece:
LUDO_BLUE = COPY(ludo_token)
COLOR(LUDO_BLUE, BLUE)

# Yellow Ludo piece:
LUDO_YELLOW = COPY(ludo_token)
COLOR(LUDO_YELLOW, YELLOW)

# Green Ludo piece:
LUDO_GREEN = COPY(ludo_token)
COLOR(LUDO_GREEN, GREEN)

# Red Ludo piece:
LUDO_RED = COPY(ludo_token)
COLOR(LUDO_RED, RED)

# Pink Ludo piece:
LUDO_PINK = COPY(ludo_token)
COLOR(LUDO_PINK, PINK)
