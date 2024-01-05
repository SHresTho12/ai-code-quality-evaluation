def add(lst):
    return sum(value for index, value in enumerate(lst) if index % 2 != 0 and value % 2 == 0)


def check(add):
    # Check some simple cases
    assert add([4, 88]) == 88, "Test 1"
    assert add([4, 5, 6, 7, 2, 122]) == 122, "Test 2"
    assert add([4, 0, 6, 7]) == 0, "Test 3"
    assert add([4, 4, 6, 8]) == 12, "Test 4"

    # Check some edge cases that are easy to work out by hand.

check(add)