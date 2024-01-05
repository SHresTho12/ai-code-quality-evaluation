def f(n):
    def factorial(x):
        if x == 0:
            return 1
        else:
            return x * factorial(x - 1)

    def sum_to_n(x):
        return sum(range(1, x + 1))

    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(sum_to_n(i))
    return result


def check(f):
    assert f(5) == [1, 2, 6, 24, 15]
    assert f(7) == [1, 2, 6, 24, 15, 720, 28]
    assert f(1) == [1]
    assert f(3) == [1, 2, 6]

check(f)