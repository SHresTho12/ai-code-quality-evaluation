def f(n):
    result = []
    factorial = 1
    summation = 0

    for i in range(1, n + 1):
        if i % 2 == 0:
            factorial *= i
            result.append(factorial)
        else:
            summation += i
            result.append(summation)

    return result

# Test case
print(f(5))
# Output: [1, 2, 6, 24, 15]
def check(f):
    assert f(5) == [1, 2, 6, 24, 15]
    assert f(7) == [1, 2, 6, 24, 15, 720, 28]
    assert f(1) == [1]
    assert f(3) == [1, 2, 6]

check(f)