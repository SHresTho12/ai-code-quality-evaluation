
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
