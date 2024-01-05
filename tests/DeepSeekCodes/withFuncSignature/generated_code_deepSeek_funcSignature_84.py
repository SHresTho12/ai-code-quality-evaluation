# This is a generated Python file.
def solve(N):
    N += 1
    while str(N) != str(N)[::-1]:
        N += 1
    return N


def check(solve):
    # Check some simple cases
    assert solve(1000) == "1", "Test 1"
    assert solve(150) == "110", "Test 2"
    assert solve(147) == "1100", "Test 3"

    # Check some edge cases that are easy to work out by hand.
    assert solve(333) == "1001", "Test 4"
    assert solve(963) == "10010", "Test 5"

check(solve)
