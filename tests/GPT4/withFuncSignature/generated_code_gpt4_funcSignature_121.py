#failed to generate code

def check(solution):
    # Check some simple cases
    assert solution([5, 8, 7, 1]) == 12, "Test 1"
    assert solution([3, 3, 3, 3, 3]) == 9, "Test 2"
    assert solution([30, 13, 24, 321]) == 0, "Test 3"
    assert solution([5, 9]) == 5, "Test 4"
    assert solution([2, 4, 8]) == 0, "Test 5"
    assert solution([30, 13, 23, 32]) == 23, "Test 6"
    assert solution([3, 13, 2, 9]) == 3, "Test 7"

    # Check the function
    check(solution)

