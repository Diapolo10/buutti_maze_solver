"""Tests generic functions"""

import pytest

from buutti_maze_solver.heatmap import tuple_sum


def test_tuple_sum_valid():
    """Tests with valid input"""

    results = (
        (tuple_sum((1, 2), (3, 4)), (4, 6)),
        (tuple_sum((7, 7, 7), (1, 2, 3), (3, 1, 4)), (11, 10, 14)),
    )

    for test_case, expected_result in results:
        assert test_case == expected_result, test_case


def test_tuple_sum_type_mismatch():
    """Tests with varying types"""

    with pytest.raises(TypeError):
        tuple_sum((3, 1, 4), ('hi', 'hello', 'world'))


def test_tuple_sum_length_mismatch():
    """Tests with varying tuple lengths"""

    with pytest.raises(ValueError, match="zip"):
        tuple_sum((3, 1, 4), (1, 5))
