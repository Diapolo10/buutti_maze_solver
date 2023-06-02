"""Configuration options for the maze solver"""

import importlib.resources as pkg_resources
from enum import Enum

from buutti_maze_solver import mazes

with pkg_resources.as_file(pkg_resources.files(mazes)) as mazes_dir:
    MAZES = mazes_dir

CHARACTER_NAME: str = "Pentti"
MOVES_TO_TEST: tuple[int, ...] = (20, 150, 200)


class MazeElement(str, Enum):
    BLOCK = '#'
    START = '^'
    EXIT = 'E'
    PATH = ' '
