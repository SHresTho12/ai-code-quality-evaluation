# This is a generated Python file.
def exchange(lst1, lst2):
    lst1[0], lst2[0] = lst2[0], lst1[0]
    return lst1, lst2


def check(exchange):
    # Check some simple cases
    assert exchange([1, 2, 3, 4], [1, 2, 3, 4]) == "YES", "Test 1"
    assert exchange([1, 2, 3, 4], [1, 5, 3, 4]) == "NO", "Test 2"
    assert exchange([1, 2, 3, 4], [2, 1, 4, 3]) == "YES", "Test 3"
    assert exchange([5, 7, 3], [2, 6, 4]) == "YES", "Test 4"
    assert exchange([5, 7, 3], [2, 6, 3]) == "NO", "Test 5"
    assert exchange([3, 2, 6, 1, 8, 9], [3, 5, 5, 1, 1, 1]) == "NO", "Test 6"

    # Check some edge cases that are easy to work out by hand.
    assert exchange([100, 200], [200, 200]) == "YES", "Test 7"

check(exchange)
