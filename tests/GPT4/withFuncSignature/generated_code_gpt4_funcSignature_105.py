def by_length(arr):
    """
    Sorts a list of strings based on their lengths in ascending order.

    :param arr: The list of strings to be sorted.
    :return: The sorted list of strings.
    """
    return sorted(arr, key=len)

def check(by_length):
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert by_length([2, 1, 1, 4, 5, 8, 2, 3]) == ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"], "Error"
    assert by_length([]) == [], "Error"
    assert by_length([1, -1 , 55]) == ['One'], "Error"

# Check some edge cases that are easy to work out by hand.
assert True, "This prints if this assert fails 2 (also good for debugging!)"
assert by_length([1, -1, 3, 2]) == ["Three", "Two", "One"]
assert by_length([9, 4, 8]) == ["Nine", "Eight", "Four"]

check(by_length)