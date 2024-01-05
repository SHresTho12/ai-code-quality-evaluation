def fib4(n: int):
    if n < 4:
        return [0, 0, 2, 0][n]
    a, b, c, d = 0, 0, 2, 0
    for _ in range(n - 3):
        a, b, c, d = b, c, d, a + b + c + d
    return d


METADATA = {} 
def check(fib4): 
    assert fib4(5) == 4 
    assert fib4(8) == 28 
    assert fib4(10) == 104 
    assert fib4(12) == 386 
    
check(fib4)