def max_fill(grid, capacity):
    # Calculate the total water in the grid
    total_water = sum(sum(row) for row in grid)
    
    # Calculate the number of times the buckets need to be lowered
    times = math.ceil(total_water / capacity)
    
    return times



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