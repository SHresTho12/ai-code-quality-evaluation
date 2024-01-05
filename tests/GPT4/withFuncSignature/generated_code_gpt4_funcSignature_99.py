def closest_integer(value):
    """
    Finds the closest integer to a given value.

    :param value: The value to round to the nearest integer.
    :return: The closest integer to the given value.
    """
    return round(value)


def check(closest_integer):
    assert closest_integer("10") == 10, "Test 1"
    assert closest_integer("14.5") == 15, "Test 2"
    assert closest_integer("-15.5") == -16, "Test 3"
    assert closest_integer("15.3") == 15, "Test 4"

# Check some edge cases that are easy to work out by hand.
assert closest_integer("0") == 0, "Test 0"

check(closest_integer)
