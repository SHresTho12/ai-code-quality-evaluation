def fib(n: int):
    if n <= 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b

    return b

# Example usage
print(fib(10))  # Output: 55

METADATA = {}

def check(fib):
    assert fib(10) == 55
    assert fib(1) == 1
    assert fib(8) == 21
    assert fib(11) == 89
    assert fib(12) == 144

check(fib)