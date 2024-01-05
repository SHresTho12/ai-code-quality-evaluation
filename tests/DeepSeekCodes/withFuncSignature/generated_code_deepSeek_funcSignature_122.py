# This is a generated Python file.
def add_elements(arr, k):
    return [x + k for x in arr]



def check(add_elements):
    # Check some simple cases
    assert add_elements([1, -2, -3, 41, 57, 76, 87, 88, 99], 3) == -4, "Test 1"
    assert add_elements([111, 121, 3, 4000, 5, 6], 2) == 0, "Test 2"
    assert add_elements([11, 21, 3, 90, 5, 6, 7, 8, 9], 4) == 125, "Test 3"
    assert add_elements([111, 21, 3, 4000, 5, 6, 7, 8, 9], 4) == 24, "Test 4"

    # Check the function
    check(add_elements)
