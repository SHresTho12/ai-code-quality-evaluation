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