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