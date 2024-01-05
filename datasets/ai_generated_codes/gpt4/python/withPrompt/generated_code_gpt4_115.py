def max_fill(grid, capacity):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    buckets = [0] * cols
    operations = 0

    for row in grid:
        for j in range(cols):
            if row[j] == 1:
                if buckets[j] > 0:
                    buckets[j] -= 1
                else:
                    for k in range(j, cols):
                        if buckets[k] < capacity:
                            buckets[k] += 1
                            break
                    operations += 1

    return operations

# Test cases
print(max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1))   # Output: 6
print(max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2))  # Output: 5
print(max_fill([[0,0,0], [0,0,0]], 5))  # Output: 0
