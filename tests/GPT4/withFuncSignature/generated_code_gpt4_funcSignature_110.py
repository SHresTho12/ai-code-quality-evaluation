def exchange(lst1, lst2):
    """
    Exchanges the contents of two lists.

    :param lst1: The first list.
    :param lst2: The second list.
    """
    lst1[:], lst2[:] = lst2[:], lst1[:]


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