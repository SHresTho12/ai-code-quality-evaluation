
import math


def max_fill(grid, capacity):
    """
    Calculates the maximum water that can be filled in the grid given a capacity constraint.

    Args:
        grid: A 2D array representing the heights of the grid cells.
        capacity: The maximum capacity of water that can be filled in a single cell.

    Returns:
        The maximum amount of water that can be filled in the grid.
    """

    rows = len(grid)
    cols = len(grid[0])

    # Initialize a 2D array to store the maximum fillable water at each cell
    max_fillable = [[0] * cols for _ in range(rows)]

    # Calculate the maximum fillable water for each cell, considering the capacity constraint
    for i in range(rows):
        for j in range(cols):
            max_fillable[i][j] = min(capacity, grid[i][j])  # Limit fillable water to capacity

    # Iterate through the grid, considering potential water flow and accumulation
    total_water = 0
    for i in range(rows):
        for j in range(cols):
            # Check for surrounding walls or higher cells to contain water
            if (i == 0 or grid[i][j] >= grid[i - 1][j]) and (
                j == 0 or grid[i][j] >= grid[i][j - 1]
            ) and (i == rows - 1 or grid[i][j] >= grid[i + 1][j]) and (
                j == cols - 1 or grid[i][j] >= grid[i][j + 1]
            ):
                total_water += max_fillable[i][j]

    return total_water


def check(max_fill):
    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1) == 6, "Test 1"
    assert max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2) == 5, "Test 2"
    assert max_fill([[0,0,0], [0,0,0]], 5) == 0, "Test 3"

    # Check some edge cases that are easy to work out by hand
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert max_fill([[1,1,1,1], [1,1,1,1]], 2) == 4, "Test 4"
    assert max_fill([[1,1,1,1], [1,1,1,1]], 9) == 2, "Test 5"

# Check the function
check(max_fill)
