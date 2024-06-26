def fibfib(n: int):
    if n < 3:
        return [0, 0, 1][n]
    a, b, c = 0, 0, 1
    for _ in range(n - 2):
        a, b, c = b, c, a + b + c
    return c