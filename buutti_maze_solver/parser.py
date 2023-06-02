"""Parses maze files"""

from pathlib import Path

from buutti_maze_solver.config import MazeElement


def parse_maze(path: Path) -> list[str]:
    """
    Parses a given maze file into a list of strings

    Raises ValueErrors on missing starting locations and exits.
    """

    raw_text = path.read_text(encoding='utf-8')

    if MazeElement.START not in raw_text:
        raise ValueError("No starting point found")

    if MazeElement.EXIT not in raw_text:
        raise ValueError("No exits found")

    return list(raw_text.splitlines())


def find_starting_point(maze: list[str]) -> tuple[int, ...]:
    """
    Finds the starting point from the maze

    Raises ValueError if a starting point cannot be found.
    """

    for row_idx, row in enumerate(maze):
        for col_idx, cell in enumerate(row):
            if cell == MazeElement.START:
                return row_idx, col_idx

    raise ValueError("No starting point found")
