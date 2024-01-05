# This is a generated Python file.
def fibfib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    

    
METADATA = {}

def check(fibfib):
    assert fibfib(2) == 1
    assert fibfib(1) == 0
    assert fibfib(5) == 4
    assert fibfib(8) == 24
    assert fibfib(10) == 81
    assert fibfib(12) == 274
    assert fibfib(14) == 927

check(fibfib)
