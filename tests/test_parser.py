"""Tests for parser functions"""

from pathlib import Path

import pytest

from buutti_maze_solver.parser import find_starting_point, parse_maze


def test_parse_maze_valid(mazes: list[Path]):
    """Tests parsing a valid maze"""

    assert isinstance(parse_maze(mazes[0]), list)


def test_parse_maze_no_start(maze_no_start: Path):
    """Tests parsing an invalid maze"""

    with pytest.raises(ValueError, match="No starting point found"):
        parse_maze(maze_no_start)


def test_parse_maze_no_exit(maze_no_exit: Path):
    """Tests parsing an invalid maze"""

    with pytest.raises(ValueError, match="No exits found"):
        parse_maze(maze_no_exit)


def test_find_starting_point_valid(parsed_maze):
    """Tests finding a starting point from a maze"""

    result = find_starting_point(parsed_maze)

    assert result == (20, 28), result


def test_find_starting_point_no_start(parsed_maze_no_start):
    """Tests parsing an invalid maze"""

    with pytest.raises(ValueError, match="No starting point found"):
        find_starting_point(parsed_maze_no_start)
