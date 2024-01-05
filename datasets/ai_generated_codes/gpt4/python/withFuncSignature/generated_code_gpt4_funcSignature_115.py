import math

def max_fill(grid, capacity):
    """
    Finds the maximum fill of a grid while respecting a capacity constraint.

    :param grid: The grid as a 2D list or matrix.
    :param capacity: The maximum capacity that each cell can hold.
    :return: The maximum fill achievable without exceeding the capacity.
    """
    if not grid:
        return 0
    
    # Define the dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])
    
    # Initialize a dynamic programming table to store maximum fill values
    dp = [[0] * cols for _ in range(rows)]
    
    # Iterate through the grid cells
    for i in range(rows):
        for j in range(cols):
            # Calculate the maximum fill for the current cell based on previous cells
            dp[i][j] = max(0, grid[i][j] + max(dp[i - 1][j], dp[i][j - 1]))
    
    # The maximum fill is stored in the bottom-right cell
    max_fill = dp[rows - 1][cols - 1]
    
    # Ensure the maximum fill does not exceed the capacity
    return min(max_fill, capacity)
