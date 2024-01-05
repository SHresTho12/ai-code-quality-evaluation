# This is a generated Python file.
def max_fill(grid, capacity):
    if not grid or not grid[0]:
        return 0

    m, n = len(grid), len(grid[0])
    dp = [[0]*n for _ in range(m)]
    dp[0][0] = capacity - grid[0][0]

    for i in range(1, m):
        dp[i][0] = dp[i-1][0] - grid[i][0] if dp[i-1][0] - grid[i][0] >= 0 else -1

    for j in range(1, n):
        dp[0][j] = dp[0][j-1] - grid[0][j] if dp[0][j-1] - grid[0][j] >= 0 else -1

    for i in range(1, m):
        for j in range(1, n):
            if dp[i-1][j] == -1 and dp[i][j-1] == -1:
                dp[i][j] = -1
            elif dp[i-1][j] == -1:
                dp[i][j] = dp[i][j-1] - grid[i][j]
            elif dp[i][j-1] == -1:
                dp[i][j] = dp[i-1][j] - grid[i][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) - grid[i][j]

    return max(0, dp[-1][-1])


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
