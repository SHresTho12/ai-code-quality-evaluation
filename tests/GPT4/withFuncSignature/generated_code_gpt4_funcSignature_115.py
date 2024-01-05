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