# This is a generated Python file.
def fib4(n: int):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
    

METADATA = {} 
def check(fib4): 
    assert fib4(5) == 4 
    assert fib4(8) == 28 
    assert fib4(10) == 104 
    assert fib4(12) == 386 
    
check(fib4)