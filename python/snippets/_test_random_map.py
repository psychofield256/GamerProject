#!/usr/bin/env python3
"""
Tests for the random_map generator
"""

from random_map import get_grid, get_walls

def test_get_grid():
    """
    Assert that:
    -the length is lines and columns are good
    -every cell contains "#" or "-".
    """
    grid = get_grid(40, 40)
    assert len(grid) == 40
    assert len(grid[0]) == 40
    for line in grid:
        for cell in line:
            assert cell == "#" or cell == "-"

def test_get_walls():
    """
    Assert that:
    -the walls are detected
    """
    grid = [
        ["-", "-", "#", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-"]
    ]
    assert get_walls(grid, (3, 3), 1) == 0
    assert get_walls(grid, (3, 3), 3) == 1
    assert get_walls(grid, (0, 0), 2) == 1
    assert get_walls(grid, (2, 1), 1) == 1
