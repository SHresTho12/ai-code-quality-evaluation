def get_odd_collatz(n):
    def collatz(n):
        while n != 1:
            yield n
            n = n * 3 + 1 if n % 2 else n // 2
        yield 1

    return sorted(x for x in collatz(n) if x % 2)


def check(get_odd_collatz):
    # Check some simple cases
    assert get_odd_collatz(14) == [1, 5, 7, 11, 13, 17], "Test 1"
    assert get_odd_collatz(5) == [1, 5], "Test 2"
    assert get_odd_collatz(12) == [1, 3, 5], "Test 3"

    # Check the function
    check(get_odd_collatz)