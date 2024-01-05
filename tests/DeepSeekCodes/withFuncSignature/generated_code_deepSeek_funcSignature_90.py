# This is a generated Python file.
def next_smallest(lst):
    if len(lst) < 2:
        return None
    return sorted(lst)[1]

def check(next_smallest):
    # Check some simple cases
    assert next_smallest([1, 2, 3, 4, 5]) == 2, "Error"
    assert next_smallest([5, 1, 4, 3, 2]) == 2, "Error"
    assert next_smallest([]) == None, "Error"
    assert next_smallest([1, 1]) == None, "Error"
    assert next_smallest([1, 1, 1, 1, 0]) == 1, "Error"
    assert next_smallest([1, 0**0]) == None, "Error"
    assert next_smallest([-35, 34, 12, -45]) == -35, "Error"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"

check(next_smallest)
